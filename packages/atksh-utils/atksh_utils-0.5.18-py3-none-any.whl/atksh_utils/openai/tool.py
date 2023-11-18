import json
import os
import random
import subprocess
import tempfile
import time
from code import InteractiveConsole
from contextlib import redirect_stdout
from io import StringIO
from itertools import islice
from threading import Lock, Semaphore

import requests
from bs4 import BeautifulSoup as bs4
from duckduckgo_search import DDGS

from .prompt import SEARCH_RESULT_SUMMARIZE_PROMPT, VISIT_PAGE_SUMMARIZE_PROMPT

# Create a temporary directory for storing files to $HOME/.cache/askgpt/
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "askgpt")
os.makedirs(CACHE_DIR, exist_ok=True)
SESSION_PATH = os.path.join(CACHE_DIR, "session.pkl")

Print_LOCK = Lock()
API_LOCK = Semaphore(12)
Python_LOCK = Lock()
Console_LOCK = Lock()
Shell_LOCK = Lock()
UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"


CONSOLE = InteractiveConsole()
MAX_ATTEMPTS = 3
MAX_SEARCH_RESULTS = 30


__all__ = [
    "get_browser_functions",
    "exec_python_code",
    "pip_install",
    "bash",
    "clear_all_python_session",
    "parse_args",
    "cb",
]


def random_sleep():
    time.sleep(random.uniform(0.01, 0.2))


def parse_args(arguments: str) -> dict:
    try:
        return json.loads(arguments)
    except json.decoder.JSONDecodeError:
        try:
            return json.loads(arguments, strict=False)
        except:
            return arguments


def cb(chunk, _):
    with Print_LOCK:
        light_cyan = "\033[96m"
        reset = "\033[0m"
        if (finish_reason := chunk.choices[0].dict().get("finish_reason")) is not None:
            if finish_reason == "stop":
                print("\n")
        token = chunk.choices[0].delta.content
        if token:
            print(f"{light_cyan}{token}{reset}", end="")


def get_browser_functions(ai: "OpenAI"):
    # model_name = ai.model_name
    model_name = "gpt-3.5-turbo-1106"
    max_context_length = 60000 if "gpt-4-1106-preview" in model_name else 10000
    search_result_child = ai.make_child(model_name)
    search_result_child.set_system_prompt(SEARCH_RESULT_SUMMARIZE_PROMPT)
    visit_page_child = ai.make_child(model_name)
    visit_page_child.set_system_prompt(VISIT_PAGE_SUMMARIZE_PROMPT)

    def _search_summarize(query_text: str, results: str) -> str:
        """Summarizes the query text and results."""
        with API_LOCK:
            for i in range(MAX_ATTEMPTS):
                for _ in range(i + 1):
                    random_sleep()
                try:
                    return search_result_child(
                        f"Query: {query_text}\nResults: {results}\nSummary: ", stream_callback=cb
                    )[1]
                except Exception as e:
                    continue
            return f"Error: {e}.\nPlease try again or try another query."

    def _page_summarize(query_text: str, page: str) -> str:
        """Summarizes the query text and page."""
        with API_LOCK:
            for i in range(MAX_ATTEMPTS):
                for _ in range(i + 1):
                    random_sleep()
                try:
                    return visit_page_child(
                        f"Query: {query_text}\nPage: {page}\nSummary: ",
                    )[1]
                except Exception as e:
                    continue
            return f"Error: {e}.\nPlease try again or try another url or wait for a while."

    def web_search(query_text: str, lang: None | str = None) -> str:
        """Searches the web for the query text.

        :param query_text: The keywords to query. For example, `The capital of Japan` or `首都 日本`.
        :type query_text: str
        :param lang: The language of the query text. `en` or `ja` is supported. If None, the language is automatically detected.
        :type lang: str, optional
        :return: json dumped results (string)
        :rtype: str
        """
        attempts = 0
        search_results = []
        if lang is None:
            region = None
        elif lang == "en":
            region = "us-en"
        elif lang == "ja":
            region = "ja-ja"
        else:
            return "Error: lang must be either 'en' or 'ja'."
        while attempts < MAX_ATTEMPTS:
            ddgs = DDGS()
            time.sleep(1 + attempts)
            random_sleep()
            result = ddgs.text(query_text, region=region, safesearch="Off")
            search_results = list(islice(result, MAX_SEARCH_RESULTS))
            if search_results:
                break
            attempts += 1

        results = json.dumps(search_results, ensure_ascii=False, indent=2)
        ret = _search_summarize(query_text, results)
        return ret

    def visit_page(query_text: str, url: str) -> str:
        """Visits the page at the url and summarizes the text with respect to the query text. Recommended to use after web_search for each url.

        :param query_text: The text to query for summarization.
        :type query_text: str
        :param url: The url to visit (must be a valid url like `https://www.google.com`).
        :type url: str
        :return: The summarized text of the page.
        :rtype: str
        """
        try:
            random_sleep()
            response = requests.get(url, timeout=10, headers={"User-Agent": UserAgent})
            soup = bs4(response.text, "html.parser")
            body = soup.find("body").text.strip()
            ret = _page_summarize(query_text, body[:max_context_length])
        except Exception as e:
            ret = f"Error: {e}.\nPlease try again or try another url."
        return ret

    return web_search, visit_page


def exec_python_code(code: str) -> str:
    """This is a function that executes Python code and returns the stdout. Don't forget to print the result. Note that this session is saved so you can use variables in the previous session.

    :param code: Python code of multiple lines. You must print the result. For example, `value = 2 + 3; print(value)`.
    :type code: str
    :return: The result of the execution of the Python code (stdout by print)
    :rtype: str
    """
    with Python_LOCK:
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py") as f:
                f.write("import dill\n")
                f.write(f"try:\n    dill.load_session('{SESSION_PATH}')\nexcept:\n    pass\n")
                f.write(code)
                f.write(f"\ndill.dump_session('{SESSION_PATH}')\n")
                f.flush()
                result = subprocess.check_output(["python", f.name])
            result = result.decode("utf-8").strip()
            if not result:
                result = "NotPrintedError('The result is not printed.')\nPlease print the result in your code."
        except Exception as e:
            result = f"Error: {e}.\nPlease try again or try another code."
    return result


def python_interpreter(lines: str) -> str:
    """Run the given Python lines and return the result like CLI with the command `python`.

    :param lines: lines (splitted by `\n') of Python code. For example, `value = 2 + 3\nvalue, value * 2`.
    :type lines: str
    :return: The result of the execution of the Python lines.
    :rtype: str
    """
    global CONSOLE
    lines = lines.split("\n")
    lines = [line for line in lines if line]

    with Console_LOCK:
        try:
            with StringIO() as buf, redirect_stdout(buf):
                for line in lines:
                    CONSOLE.push(line)
                result = buf.getvalue()
        except Exception as e:
            result = f"Error: {e}.\nPlease try again."
    return result


def pip_install(args: str) -> str:
    """Execute pip install {args} and return the result.

    :param args: The arguments to pass to pip install. For example, `torch==1.9.0+cu111`.
    :type args: str
    """
    with Python_LOCK, Shell_LOCK:
        try:
            ret = subprocess.check_output(["pip", "install", args])
        except subprocess.CalledProcessError as e:
            return_code = e.returncode
            output = e.output
            ret = f"Error: return_code={return_code}, output={output}"
        except Exception as e:
            ret = f"Error: {e}.\nPlease try again or try another command."
        return str(ret)


def bash(command: str) -> str:
    """Execute the given command and return the result.

    :param command: The command to execute. For example, `ls -l`.
    :type command: str
    :return: The result of the execution of the command.
    :rtype: str
    """
    with Shell_LOCK:
        try:
            ret = subprocess.check_output(command)
        except subprocess.CalledProcessError as e:
            return_code = e.returncode
            output = e.output
            ret = f"Error: return_code={return_code}, output={output}"
        except Exception as e:
            ret = f"Error: {e}.\nPlease try again or try another command."
    return str(ret)


def clear_all_python_session():
    """Clears the exec_python_code session and resets the python_interpreter.

    :return: True if the session is cleared successfully.
    :rtype: bool
    """
    global CONSOLE
    try:
        if os.path.exists(SESSION_PATH):
            os.remove(SESSION_PATH)
        CONSOLE = InteractiveConsole()
        return True
    except:
        return False
