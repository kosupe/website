from moviepy.editor import VideoFileClip

video = VideoFileClip("Z:\\動画\\icra.mp4").subclip(8, 19)

video.write_videofile("Z:\\動画\\py__icra.mp4", fps=40)