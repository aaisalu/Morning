from pytube.cli import on_progress 
from pytube import Playlist
import pytube
import os,re
import time

t1 = time.perf_counter()
def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    Path=rf"{desktop}\Youtube\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path

def mp3(url):
    yt=pytube.YouTube(url)
    print(f"Title: {yt.title} ")
    print(f"Views: {yt.views} Duration:{yt.length}")
    try: 
        out_file = pytube.YouTube(url,on_progress_callback=on_progress).streams.filter(only_audio=True).first().download(folder("Audios"))
        print(":) \n")        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    except FileExistsError:
        print(f"Looks like {yt.title} music is already present. \n")

def solo_video(url):
    yt=pytube.YouTube(url)
    print(f"Title: {yt.title}")
    print(f"Views: {yt.views} Duration: {yt.length}") 
    pytube.YouTube(url,on_progress_callback=on_progress).streams.get_highest_resolution().download(folder("Videos"))     
    print(":) \n")

def playlists(link,ask):
    urls=[]
    playlist = Playlist(link)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    if re.search("audio|mp3|music|flac|wav|aac|ogg|audios",ask,flags=re.IGNORECASE):
        print("Starting to download MP3s of the videos \n")
        for music_url in playlist.video_urls:
            mp3(music_url)
    else:
        print("Starting to download videos in 720p\n")
        for video_url in playlist.video_urls:
            solo_video(video_url)     

def checkbox(link):
    ask=input("Which type do you prefer mp3 or mp4: ")
    if "list" in link:
        playlists(link,ask)      
    else:
        if re.search("audio|mp3|music|flac|wav|aac|ogg|audios",ask,flags=re.IGNORECASE):
            print("Starting to download MP3s of the video \n")
            mp3(link)
        else:
            print("Starting to download video in 720p \n")
            solo_video(link)

url=checkbox(str(input("Enter the url of the video: ")))               
t2 =time.perf_counter()
print(f"Saved at {Path} took {t2-t1} seconds")


