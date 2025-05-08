#!usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


class ArgParser(ArgumentParser):
    def __init__(self):
        super().__init__()

        self.description = 'LLM on the command line: a client for intelligent conversations.'
        self.add_argument('message', help='Prompt message')
        self.add_argument('--image', nargs='*', help='Image path')
        self.add_argument('--deeper', action='store_true', help='More complex tasks')

