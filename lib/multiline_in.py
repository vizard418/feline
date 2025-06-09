#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory                                
from colorama import Fore, Style
from sys import stdout
from pathlib import Path


class MultilineIn():
    LABEL_IN = Fore.GREEN + '$> [PROMPT]' + Style.RESET_ALL
    LABEL_OUT = Fore.YELLOW + '$> [FELINE]' + Style.RESET_ALL
    LABEL_ERROR = Fore.RED + '+ [ERROR!]' + Style.RESET_ALL
    LABEL_EXIT = '**Press Return 2 times to exit**'

    @staticmethod
    def get_user_input(history_file:str) ->str:
        history = FileHistory(history_file)
        answer = ''
        count_empty = 0

        while True:
            prompt_line = prompt('$> ', history=history)

            if prompt_line == '':
                count_empty += 1

                if count_empty == 2:
                    stdout.write('\x1b[1A')
                    stdout.write('\x1b[2K')
                    break
            else:
                count_empty = 0

            answer += prompt_line + '\n'
        return answer.rstrip()

