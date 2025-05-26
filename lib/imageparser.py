#!usr/bin/python3
#-*- coding: utf-8 -*-

from PIL import Image
from requests import get as r_get
from urllib.parse import urlparse
from io import BytesIO


class ImageParser():
    @staticmethod
    def image_resolve(source:str) ->bytes:
        if urlparse(source).scheme:
            request = r_get(source)
            image = Image.open(BytesIO(request.content))

        else:
            image = Image.open(source)

        return image
