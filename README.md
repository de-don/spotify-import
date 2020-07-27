# Install requirements
To install nessesary requirements, run next command:
```
pip install -r requirements.txt
```

# Fetch tracks from VK.com:
Set `access_token` in `./config.py` and run the command:
```
python3 ./get_vk_tracks.py
```
It will create the file `tracks.txt` with information about our tracks.

# Import tracks to Spotify:
Run the command:
```
python3 ./import_tracks.py
```
After authentication, it will import all tracks from the file `tracks.txt` to your playlist.