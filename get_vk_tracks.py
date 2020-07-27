import config
from utils.vk import get_audio_list

audios = get_audio_list(config.token, 7738880)

with open('vk_tracks.txt', 'w+', encoding='utf8') as file:
    for artist, title in audios:
        file.write(f'{artist} - {title}\n')
