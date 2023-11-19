#!/usr/bin/env python3
import argparse
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
                print(f"\n{bold}{blue}Calling {n_calls} function(s){reset}{blue}:")
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
    ai.set_python_functions()
    ai.set_bash_function()
    return ai


def ask():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpt4", action="store_true", help="Enable GPT-4.")
    args = parser.parse_args()
    ai = setup_ai(use_gpt4=args.gpt4)
    not_called = True
    try:
        while True:
            empty_input_count = 0
            lines = []
            lines.append(
                input(
                    "Continue the conversation. To send your reply, "
                    "please press Enter more than three times.\n>>> "
                )
            )
            while empty_input_count < 3:
                try:
                    lines.append(input(">>> "))
                    user_prompt = "\n".join(lines).strip()
                    if not lines[-1].strip():
                        empty_input_count += 1
                        continue
                except (KeyboardInterrupt, EOFError):
                    break
            if user_prompt:
                if not_called:
                    print(f"\n{bold}{red}AI{reset}{red}: {bold}{blue}Thinking...{reset}\n")
                    messages, _ = ai(user_prompt, stream_callback=cb, is_question=True)
                    not_called = False
                else:
                    messages.append({"role": "user", "content": user_prompt})
                    print(f"\n{bold}{red}AI{reset}{red}: {bold}{blue}Thinking...{reset}\n")
                    ai.try_call(user_prompt, stream_callback=cb, messages=messages)
            else:
                while True:
                    y_or_n = input("Do you want to quit? (y/n): ").strip().lower()
                    if y_or_n == "y":
                        print("\n")
                        print("Bye!")
                        return
                    elif y_or_n == "n":
                        break
                    else:
                        print(f"{y_or_n} is not a valid input. Please try again.")
    except (KeyboardInterrupt, EOFError):
        print("\n")
        print("Bye!")
        return
