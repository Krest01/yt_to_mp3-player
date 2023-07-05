import os
import time
import yt_dlp
from pydub import AudioSegment
from pydub.playback import play


def nowa_piosenka():
    SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
    }
    url = input("Proszę podać url utworu ")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def graj_piosenkę():
    piosenki = os.listdir('./Downloads')
    for piosenka in piosenki:
        if piosenka == 'desktop.ini':
            pass
        else:
            print(f"{piosenka}\n")
    piosenka = input("Proszę podać utwór który ma zostać odtworzony ")
    song = AudioSegment.from_file(piosenka)
    song.converter = r"C:\\Users\\Jakub\\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
    play(song)
    time.sleep(10)
    return None

graj_piosenkę()
