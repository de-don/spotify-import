import config
from utils.vk import get_audio_list

audios = get_audio_list(config.vk_token)

with open('tracks.txt', 'w+', encoding='utf8') as file:
    for artist, title in audios:
        file.write(f'{artist} // {title}\n')
