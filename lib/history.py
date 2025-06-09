#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

class History:
    CACHE_DIR = Path.home() / '.cache' / 'FeLine'
    HISTORY_INPUT = CACHE_DIR / '.input-history'

    @staticmethod
    def check_dir():
        History.CACHE_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def clear_input():
        try:
            with open(History.HISTORY_INPUT, 'w') as f:
                print('~ History input clean ~')
        except:
            History.check_dir()

