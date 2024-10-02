import requests
import urllib3
import asyncio
#import libtorrent as lt
#from torrentp import TorrentDownloader
from AnilistPython import Anilist
#anime download
anilist = Anilist()

anime_data = anilist.get_anime("Tokyo Ghoul")
print(anime_data)
if anime_data['airing_status'] == "FINISHED":
    #torrent download from nyaa
    pass
else:
    pass
#response = requests.get("https://nyaaapi.onrender.com/nyaa?q=Tokyo%20Ghoul", verify=False)
#dic = response.json()
#animeTitle = dic["data"][0]["title"]
#torrentLink = dic["data"][0]["torrent"]
#magnetLink = dic["data"][0]["magnet"]
#print(anilist.get_anime("Make Heroine ga Oosugiru!"))
#torrentFile = TorrentDownloader(torrentLink, ".")
#asyncio.run(torrentFile.start_download())
