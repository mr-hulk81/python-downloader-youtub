import yt_dlp

def download_youtube_video(link):
    options = {
        'format': 'bestvideo+bestaudio/best',  # Best quality
        'outtmpl': '/downloads/%(title)s.%(ext)s',  # Save in /downloads directory
        'cookies': './cookies.txt'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            print(f"Downloading: {link}")
            ydl.download([link])
            print("Download completed!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube video link: ")
    download_youtube_video(link)
