import urllib.request
from moviepy.editor import VideoFileClip


VIDEO_FILE_NAME = "video.mp4"
url_link = input("Enter video url: ")
try:
    urllib.request.urlretrieve(url_link, VIDEO_FILE_NAME)
except ValueError:
    print("Impossible to download this video")
    exit()
try:
    videoClip = VideoFileClip(VIDEO_FILE_NAME)
    videoClip.write_gif("test.gif")
except:
    print("Invalid video. GIF was not created")
else:
    print("GIF created successfully")
