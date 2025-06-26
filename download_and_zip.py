# דרישות: pip install yt-dlp
import yt_dlp
import zipfile
import os
import sys
import shutil

# קבלת כתובת הסרטון או הפלייליסט
if len(sys.argv) > 1:
    video_url = sys.argv[1]
else:
    print("יש לספק כתובת סרטון או פלייליסט כפרמטר.")
    sys.exit(1)

download_folder = "downloads"
zip_filename = "videos.zip"
cookiefile = "cookies.txt" if os.path.exists("cookies.txt") else None

# יצירת תיקיית הורדה
os.makedirs(download_folder, exist_ok=True)

# הגדרות yt-dlp
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'merge_output_format': 'mp4'
}
if cookiefile:
    ydl_opts['cookiefile'] = cookiefile

# הורדת סרטונים
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# יצירת קובץ ZIP
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(download_folder):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, download_folder)
            zipf.write(filepath, arcname)

# ניקוי קבצים זמניים
shutil.rmtree(download_folder)

print(f"נוצר קובץ ZIP בשם: {zip_filename}")
