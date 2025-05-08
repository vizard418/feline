#!usr/bin/python3
# -*- coding: utf-8 -*-

from google.genai import Client


class Gemini(Client):
    api_varname = 'GEMINI_API_KEY'

    def __init__(self, api_key:str):
        super().__init__(api_key=api_key)
        self.chat = None


    def get_response(self, model:str, *args):
        return self.models.generate_content_stream(model=model,
            contents=[*args])


    def get_chat_response(self, model:str, message:str):
        if not self.chat:
            self.chat = self.chats.create(model=model)

        return self.chat.send_message_stream(message)