import config

from providers.vk_audio_provider import VkProvider

provider = VkProvider(config.vk_token)
tracks_list = provider.get_tracks()

tracks_list.to_file(file_path='tracks.txt')
