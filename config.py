import os

from dotenv import load_dotenv

load_dotenv()

# https://oauth.vk.com/authorize?client_id=6121396&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1
token = os.getenv('TOKEN')
user_id = os.getenv('USER_ID')
