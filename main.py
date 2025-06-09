#/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.argparser import ArgParser
from lib.gemini import Gemini
from os import getenv
from lib.multiline_in import MultilineIn
from lib.cmdhandler import CmdHandler
from lib.imageparser import ImageParser
from lib.history import History


def get_api_key(varname:str) ->str:
    api_key = getenv(varname)

    if not api_key:
        raise NameError('Error loading %s' % varname)

    else: return api_key


def get_input(history_file) ->str:
    print('\n' + MultilineIn.LABEL_IN, MultilineIn.LABEL_EXIT)
    return MultilineIn.get_user_input(history_file)


def parse_instructions(prompt_text:str) ->tuple[str, str]:
    try:
        command_expand = CmdHandler.get_expand(prompt_text)
    except:
        print(MultilineIn.LABEL_ERROR, 'Shell: Unrecognized command.')
        command_expand = None

    images_locations = CmdHandler.get_file_locations(prompt_text)
    return command_expand, images_locations


def load_images(images_filenames:list) ->list[bytes]:
    try:
        images = [ImageParser.image_resolve(x) for x in images_filenames]
    except:
        print(MultilineIn.LABEL_ERROR, 'Image: Error loading.')
        return
    return images


def display_response(response) ->None:
    print('\n' + MultilineIn.LABEL_OUT)

    for chunk in response:
        print(chunk.text, end='')

    print('\n---')


def get_response(agent, prompt):
    try:
        response = agent.get_chat_stream(prompt_contents)
    except ServerError:
        print(MultilineIn.LABEL_ERROR, 'Server Error')
    else:
        display_response(response)


if __name__ == '__main__':
    # arguments
    parser = ArgParser(Gemini.AVAILABLE_MODELS.keys())
    args = parser.parse_args()

    # history
    if args.clear:
        History.clear_input()

    # agent init
    feline = Gemini(api=get_api_key(Gemini.API_VARNAME))

    if args.model:
        feline.model = Gemini.AVAILABLE_MODELS[args.model]

    # chat
    loop = True

    while loop:
        History.check_dir()

        # non-interactive mode
        if args.message:
            user_input = args.message
            loop = False

        else:
            user_input = get_input(History.HISTORY_INPUT)

            if not user_input:
                print(); break

        # prompt instructions handler
        command_expand, images_locations = parse_instructions(user_input)
        if command_expand:
            user_input = '%s\n%s' % (user_input, command_expand)

        # image recognition
        if images_locations:
            prompt_contents = load_images(images_locations)

            if not prompt_contents:
                prompt_contents = user_input
            else:
                prompt_contents.insert(0, user_input)
        
        # text recognition
        else:
            prompt_contents = user_input

        # text generation
        response = get_response(feline, prompt_contents)

