from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with open("urls.txt", "r") as f:
    for link in f:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])