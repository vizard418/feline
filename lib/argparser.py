#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

class ArgParser(ArgumentParser):
    def __init__(self, models):
        super().__init__()

        self.description = 'An interactive command-line AI agent.'
        self.add_argument('--model', type=str, choices=models, required=False,
            help='Specify model. Availables: %s' % models)
        self.add_argument('--clear-history', action='store_true', required=False,
            help='Clear input history.')

