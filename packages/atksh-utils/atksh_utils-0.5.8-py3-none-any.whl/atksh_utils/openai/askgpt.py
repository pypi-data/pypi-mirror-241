#!/usr/bin/env python3
import argparse
import json
import os
import readline

from atksh_utils.openai import OpenAI
from atksh_utils.openai.tool import parse_args

blue = "\033[34m"
green = "\033[32m"
red = "\033[31m"
bold = "\033[1m"
reset = "\033[0m"


def cb(chunk, message):
    if (finish_reason := chunk.choices[0].dict().get("finish_reason")) is not None:
        if finish_reason == "stop":
            print("\n")
        else:
            info = chunk.choices[0].dict()
            if info["finish_reason"] == "tool_calls":
                n_calls = len(message.tool_calls)
                print(f"{bold}{blue}Calling {n_calls} function(s){reset}{blue}:")
                for i in range(len(message.tool_calls)):
                    function_name = message.tool_calls[i].function.name
                    print(message.tool_calls[i].function)
                    try:
                        function_call_args = parse_args(message.tool_calls[i].function.arguments)
                    except ValueError:
                        print("Error: JSONDecodeError", end=": ")
                        print(message.tool_calls[i].function.arguments)
                    else:
                        pretty_args = []
                        if isinstance(function_call_args, str):
                            print(f"{bold}{red}Error{reset}{red}: {function_call_args}{reset}")
                        else:
                            for arg, value in function_call_args.items():
                                value = str(value).replace("\n", "\n" + " " * len(arg) + " " * 3)
                                pretty_args.append(f"  {arg}={value}")
                            pretty_args = ",\n".join(pretty_args)
                            text = f"\n{reset}{bold}{blue}{function_name}{reset}{blue}(\n{pretty_args}\n)\n\n"
                            print(text + reset)
    token = chunk.choices[0].delta.content
    if token:
        print(f"{green}{token}{reset}", end="")


def setup_ai(use_gpt4: bool = False) -> OpenAI:
    key = os.getenv("OPENAI_API_KEY")
    ai = OpenAI(key, "gpt-4-1106-preview" if use_gpt4 else "gpt-3.5-turbo-1106")
    ai.set_browser_functions()
    ai.set_run_python_code_function()
    ai.set_bash_function()
    return ai


def ask():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="The query to ask to the AI.")
    parser.add_argument("--disable-gpt4", action="store_true", help="Disable GPT-4.")
    args = parser.parse_args()
    ai = setup_ai(use_gpt4=not args.disable_gpt4)
    messages, _ = ai(args.query, stream_callback=cb, is_question=True)
    try:
        while True:
            user_prompt = input("Continue the conversation or press :q! to quit:\n>>> ")
            if user_prompt == ":q!":
                break
            print()
            messages.append({"role": "user", "content": user_prompt})
            ai.try_call(user_prompt, stream_callback=cb, messages=messages)
    except (KeyboardInterrupt, EOFError):
        print("\n")
        print("Bye!")
        return
