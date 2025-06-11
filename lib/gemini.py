#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.genai import Client

class Gemini(Client):

    API_VARNAME = 'GEMINI_API_KEY'

    AVAILABLE_MODELS = {
        'flash' : 'gemini-2.0-flash',
        'lite' : 'gemini-2.0-flash-lite',
        'preview' : 'gemini-2.5-flash-preview-05-20'
    }

    DEFAULT_MODEL = AVAILABLE_MODELS['lite']


    def __init__(self, api:str):
        super().__init__(api_key=api)

        self.model = self.DEFAULT_MODEL
        self.chat = None


    def get_chat_stream(self, message:str):
        if not self.chat:
            self.chat = self.chats.create(model=self.model)

        return self.chat.send_message_stream(message)
