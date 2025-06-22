# דרישות: pip install yt-dlp
import yt_dlp
import zipfile
import os

# כתובת הסרטון
video_url = "https://www.youtube.com/watch?v=oXi-hFVZZ_o"

# שם קובץ ה-MP4 שיווצר
output_filename = "video.mp4"

# בדוק אם קיים קובץ cookies.txt בתיקייה הנוכחית
cookiefile = "cookies.txt" if os.path.exists("cookies.txt") else None

# הורדת הסרטון
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': output_filename,
    'merge_output_format': 'mp4'
}
if cookiefile:
    ydl_opts['cookiefile'] = cookiefile

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# דחיסת הקובץ ל-ZIP
zip_filename = "video.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(output_filename)

# מחיקת קובץ ה-MP4 המקורי (אופציונלי)
os.remove(output_filename)

print(f"נוצר קובץ ZIP בשם: {zip_filename}")
