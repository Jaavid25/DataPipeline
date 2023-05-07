import subprocess
import os
# set the video URL
def download_audio_from_yt_link(url,output_dir_path = "."):
    if not os.path.exists(output_dir_path):
        print("Folder not found at path, Creating new folder...")
        os.makedirs(output_dir_path)


    # set the download options
    options = [
        'yt-dlp', '-P',
        output_dir_path,
        '--format', 'bestaudio',
        '--audio-format', 'mp3',
        '--output', '%(title)s.%(ext)s',
        '-x',
        url
    ]
    # start the download in a separate process
    subprocess.run(options)

