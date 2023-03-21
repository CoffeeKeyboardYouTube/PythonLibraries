"""
This code can be used for downloading any YouTube video you want. All you have to do is enter the link of the youtube video you want. 
In a few seconds you will have the YouTube video downloaded. 

Pytube Documentation: https://pypi.org/project/pytube/
YouTube Tutorial: https://www.youtube.com/watch?v=5s2urYqLjjM
"""






from  pytube import YouTube

def Download(link):
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution();
    youtube_video.download()
    print("YouTube video has been downloaded")


link = input("enter the video link you want to install: ")
Download(link)
