# atksh-utils

This is my collection of utilities.


## Development

To install this for development, run the following commands in your terminal:

```bash
python -m pip install -e '.[dev]'
pre-commit install
```

## OpenAI

```python
ai = OpenAI(key, "gpt-3.5-turbo-1106")

print(ai("Just answer the value of (5243 + 642) x (5314 - 4231) // 100"))
# The value of the expression (5243 + 642) x (5314 - 4231) // 100 is 7112.


def mul(a: int, b: int) -> int:
    """This is a multiplication function.

    :param a: An integer.
    :type a: int
    :param b: An integer.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a * b


def add(a: int, b: int) -> int:
    """This is an addition function.

    :param a: An integer.
    :type a: int
    :param b: An integer.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a + b


def sub(a: int, b: int) -> int:
    """This is a subtraction function.

    :param a: An integer.
    :type a: int
    :param b: An integer.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a - b


def div(a: int, b: int) -> int:
    """This is a division function.

    :param a: An integer.
    :type a: int
    :param b: An integer.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a // b

ai.set_function(mul)
ai.set_function(add)
ai.set_function(sub)
ai.set_function(div)

print(ai("Just answer the value of (5243 + 642) x (5314 - 4231) // 100")[1])
# The value of (5243 + 642) x (5314 - 4231) // 100 is 63734.


ai = OpenAI(key, "gpt-3.5-turbo-1106")
ai.set_browser_functions()
print(ai("How the weather in Tokyo?")[1])
# The current weather in Tokyo varies depending on the source. According to AccuWeather, it is partly sunny with a temperature of 89°F. BBC Weather predicts thundery showers tonight with a low temperature of 22°C. Timeanddate.com reports an overcast sky with a temperature of 82°F. The Weather Network and The Weather Channel provide forecasts for the next 7 and 13 days respectively. Weather Underground also offers weather conditions for Tokyo and other cities.
```
