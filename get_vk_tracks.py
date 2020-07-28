import config

from providers.vk_audio_provider import VkProvider

provider = VkProvider(config.vk_token)
tracks = provider.get_tracks()

with open('tracks.txt', 'w+', encoding='utf8') as file:
    for track in tracks:
        file.write(track.to_string() + '\n')
