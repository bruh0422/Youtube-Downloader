import os, yt_dlp

ydl_opts = {
    'format': 'wav/bestaudio/best',
    'outtmpl': 'output/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }],
    'ignoreerrors': True
}

for name in ['output']:
    if name not in os.listdir():
        os.mkdir(name)
        print(f"創建 {name} 資料夾...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(input('輸入影片或播放清單連結: ').split())