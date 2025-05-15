#!/usr/bin/python3
# -*- coding: utf-8 -*-

from prompt_toolkit import prompt
from colorama import Fore, Style
from sys import stdout


def overwrite() -> None:
    stdout.write('\x1b[1A')
    stdout.write('\x1b[2K')


def print_input_header() -> None:
    print(Fore.GREEN + '\n<- [PROMPT INPUT]' + Style.RESET_ALL)


def print_output_header() -> None:
    print(Fore.YELLOW + '\n-> [PROMPT OUTPUT]' + Style.RESET_ALL)


def handle_input(text: str) -> str:
    print('> ' + text)
    return text.rstrip()


def input_multiline_input() -> str:
    answer = ''
    count_empty = 0

    while True:
        prompt_line = prompt('> ')

        if prompt_line == '':
            count_empty += 1
            if count_empty == 2:
                for i in range(2): overwrite()
                break
        else:
            count_empty = 0

        answer += prompt_line + '\n'

    return answer.rstrip()


def format_in(input_text=None) -> str:
    print_input_header()

    if input_text is not None:
        return handle_input(input_text)

    return input_multiline_input()

