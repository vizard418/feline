#!usr/bin/python3
# -*- coding: utf-8 -*-

from lib.argparser import ArgParser
from lib.imageparser import ImageParser
from lib.gemini import Gemini
from os import getenv
from lib.prompt_io import format_in
from lib.prompt_io import print_output_header

if __name__ == '__main__':
    # Arguments
    parser = ArgParser()
    args = parser.parse_args()

    # Api validation
    api_key = getenv(Gemini.api_varname)
    
    if not api_key:
        raise NameError('Enviroment variable "%s" was not found.'
            % Gemini.api_varname)
    
    else:
        gemini = Gemini(api_key=api_key)
    
    # Processing
    prompt = args.message

    # Image recognition
    if args.image:
        model = 'gemini-2.0-flash'
            
        contents = [ImageParser.image_resolve(x) for x in args.image]
        contents.insert(0, args.message)

        response = gemini.get_response(model, contents)

        # Output
        print_output_header()
        for chunk in response:
            print(chunk.text, end='')
        
    else:
        # Text recognition
        if args.deeper: model='gemini-2.0-flash'
        else: model = 'gemini-2.0-flash-lite'

        while True:
            response = gemini.get_chat_response(model, prompt)
            print_output_header()
                
            for chunk in response:
                print(chunk.text, end='')
                
            print('\n**Press Return 2 times to exit**\n')
            prompt = format_in()

            if not prompt:
                break
