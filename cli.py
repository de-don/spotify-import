from __future__ import print_function, unicode_literals

import logging

from PyInquirer import prompt

from providers.vk_audio_provider import VkProvider
from utils.import_tracks import import_tracks

logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_FILE_NAME = 'tracks.txt'


class Action:
    Export = 'export'
    Import = 'import'


class Source:
    Vk = 'vk'
    Yandex = 'yandex'


def is_export(_answers: dict) -> bool:
    return _answers.get('action') == Action.Export


def is_import(_answers: dict) -> bool:
    return _answers.get('action') == Action.Import


questions = [
    dict(
        type='list',
        name='action',
        message='What do you want to do?',
        choices=[
            {'value': Action.Export, 'name': 'Export tracks from some service to text file'},
            {'value': Action.Import, 'name': 'Import tracks from text file to Spotify'},
        ]
    ),
    # Export branch
    dict(
        when=is_export,
        type='list',
        name='source',
        message='From what service?',
        choices=[
            {'value': Source.Vk, 'name': 'vk.com'},
            {'value': Source.Yandex, 'name': 'Yandex Music'},
        ],
    ),
    dict(
        when=is_export,
        type='input',
        name='file_path',
        message='Please enter an output file name',
        default=DEFAULT_FILE_NAME,
        # TODO: add file path validation
    ),

    # Import branch
    dict(
        when=is_import,
        type='input',
        name='file_path',
        message='Please enter an input file name',
        default=DEFAULT_FILE_NAME,
        # TODO: add file path validation
        # TODO: add file existence validation
    ),
]

if __name__ == '__main__':
    answers = prompt(questions)

    file_path = answers['file_path']

    if is_import(answers):
        import_tracks(file_path)

    if is_export(answers):
        source = answers.get('source')
        if source == Source.Vk:
            provider = VkProvider()

            tracks_list = provider.get_tracks()
            tracks_list.to_file(file_path=file_path)

            logger.info(f"Exported {len(tracks_list)} track(s), you can check them in {file_path}")

        if source == Source.Yandex:
            logger.info("Not implemented yet")
