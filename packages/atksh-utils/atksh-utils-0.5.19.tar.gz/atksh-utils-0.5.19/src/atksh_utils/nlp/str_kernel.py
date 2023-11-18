# This implementation is based on https://aclanthology.org/2021.acl-long.512.pdf
from typing import List, Tuple

import numba as nb
import numpy as np
import numpy.typing as npt


def ssk(s: str, t: str, n: int, lam: float) -> float:
    s_tokens = np.array([ord(c) for c in s], dtype=np.int64)
    t_tokens = np.array([ord(c) for c in t], dtype=np.int64)
    return ssk_array(s_tokens, t_tokens, n, lam)


@nb.njit("f8(i8[:], i8[:], i8, f8)", fastmath=True)
def ssk_array(s: npt.NDArray, t: npt.NDArray, n: int, lam: float) -> float:
    lens = len(s)
    lent = len(t)
    k_prim = np.zeros((n, lens, lent), dtype=nb.float32)  # pyre-ignore
    k_prim[0, :, :] = 1

    for i in range(1, n):
        for sj in range(i, lens):
            toret = 0.0
            for tk in range(i, lent):
                if s[sj - 1] == t[tk - 1]:
                    toret = lam * (toret + lam * k_prim[i - 1, sj - 1, tk - 1])
                else:
                    toret *= lam
                k_prim[i, sj, tk] = toret + lam * k_prim[i, sj - 1, tk]

    k = 0.0
    for i in range(n):
        for sj in range(i, lens):
            for tk in range(i, lent):
                if s[sj] == t[tk]:
                    k += lam * lam * k_prim[i, sj, tk]

    return k


@nb.njit(fastmath=True)
def log_add(x: npt.NDArray, y: npt.NDArray) -> npt.NDArray:
    return x + np.log1p(np.exp(y - x))


@nb.njit(fastmath=True)
def log_minus(x: npt.NDArray, y: npt.NDArray) -> npt.NDArray:
    return x + np.log1p(-np.exp(y - x))


@nb.njit("Tuple((i8, f8))(f8[:], f8[:], i8[:], i8[:])", fastmath=True)
def logsumexp(
    C1: npt.NDArray, C2: npt.NDArray, S1: npt.NDArray, S2: npt.NDArray
) -> Tuple[int, float]:
    s = 1
    log_inner = np.NINF
    for i in range(len(C1)):
        c1 = C1[i]
        c2 = C2[i]
        s1 = S1[i]
        s2 = S2[i]
        s_prime = s1 * s2
        if log_inner > c1 + c2:
            if s == s_prime:
                log_inner = log_add(log_inner, c1 + c2)
            else:
                log_inner = log_minus(log_inner, c1 + c2)
        else:
            if s == s_prime:
                log_inner = log_add(c1 + c2, log_inner)
            else:
                log_inner = log_minus(c1 + c2, log_inner)
            s = s_prime
    return s, log_inner


@nb.njit("i8[:](f8[:, :], i8)", fastmath=True)
def greedy_map_inference(L: npt.NDArray, k: int) -> npt.NDArray:
    n = len(L)
    d = np.diag(L)
    s = np.zeros((n, k), dtype=nb.int64)  # pyre-ignore
    c = np.zeros((n, k), dtype=nb.float64)  # pyre-ignore
    m = np.zeros(n, dtype=nb.boolean)  # pyre-ignore

    Y_g = -np.ones(k, dtype=nb.int64)  # pyre-ignore
    j = np.argmax(d)
    m[j] = True
    Y_g[0] = j
    for idx in range(k - 1):
        for i in range(n):
            if m[i]:
                continue
            s_i, log_inner = logsumexp(c[i, :idx], c[j, :idx], s[i, :idx], s[j, :idx])
            flag = s_i < 0
            if L[j, i] > log_inner:
                s_i = 1
                if flag:
                    e_i = log_add(L[j, i], log_inner) - 0.5 * d[j]
                else:
                    e_i = log_minus(L[j, i], log_inner) - 0.5 * d[j]
            else:
                s_i = -s_i
                if flag:
                    e_i = log_add(log_inner, L[j, i]) - 0.5 * d[j]
                else:
                    e_i = log_minus(log_inner, L[j, i]) - 0.5 * d[j]
            c[i, idx] = e_i
            d[i] -= 2 * e_i
            s[i, idx] = s_i
        j = np.argmax(np.where(m, np.NINF, d))
        Y_g[idx + 1] = j
        m[j] = True
    return Y_g


def build_kernel(s: List[str], n: int, lam: float, eps: float = 1e-1) -> npt.NDArray:
    """Build a Gram matrix with string subsequence kernel."""
    b = len(s)
    tokens = list()
    for i in range(b):
        tokens.append(np.array([ord(x) for x in s[i]], dtype=np.int64))
    lens = np.array([len(t) for t in tokens], dtype=np.int64)
    maxlen = np.max(lens)
    tokens = np.stack(
        [np.pad(t, (0, maxlen - len(t))) for t in tokens],  # pyre-ignore
        axis=0,
    )
    return _build_kernel(tokens, lens, n, lam, eps)


@nb.njit("f8[:, :](i8[:, :], i8[:], i8, f8, f8)", parallel=True)
def _build_kernel(
    tokens: npt.NDArray,
    lens: npt.NDArray,
    n: int,
    lam: float,
    eps: float = 1e-1,
) -> npt.NDArray:
    b = len(tokens)
    norm = np.zeros(b, dtype=nb.float64)  # pyre-ignore
    mat = np.zeros((b, b), dtype=nb.float64)  # pyre-ignore
    for i in nb.prange(b):  # pyre-ignore[16]
        for j in range(i, b):
            tmp = ssk_array(tokens[i, : lens[i]], tokens[j, : lens[j]], n, lam)
            tmp = (1 - eps) * tmp + eps
            mat[i, j] = tmp
            mat[j, i] = tmp
    norm = np.diag(mat).reshape(b, 1)
    return np.divide(mat, np.sqrt(norm.T * norm))
