"""
This code allows you extract an audio file from a video that you have stored on your desktop.
I personally love Backstreet boys, so I can extract the audio from the videos and listen to them. 

MoviePy Documentation: https://pypi.org/project/moviepy/
Check out the YouTube video: https://www.youtube.com/watch?v=W0gau9E-Exo
"""

# Path: audio.py
import moviepy.editor
video = moviepy.editor.VideoFileClip("video.mp4")
video.audio.write_audiofile("final.mp3")
print("Done")
