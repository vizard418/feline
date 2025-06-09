#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import check_output
from re import search, findall

class CmdHandler:

    @staticmethod
    def get_expand(text) ->str:
        match = search(r'\$\(([^)]*)\)', text)

        if match:
            command = match.group(1)
            return check_output(command, shell=True, text=True).strip()

    @staticmethod
    def get_file_locations(text: str) ->list[str]:
        return findall(r'\$\[([^\]]*)\]', text)
