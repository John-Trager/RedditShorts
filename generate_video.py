'''
create video using moviepy
- adds narration audio and subtitles to video

This script is still being built out.

TODO: make subtitles appear a few words at a time, or only 1 word at a time
'''

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.all import crop

import os
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', required=True, help='path to audio file')
    parser.add_argument('--video', required=True, help='path to video file')
    parser.add_argument('--subtitles', required=True, help='path to subtitles file')
    parser.add_argument('--output', required=True, help='path to output file')
    args = parser.parse_args()

    # load audio
    audio = AudioFileClip(args.audio)

    # load video
    video = VideoFileClip(args.video)

    #crop(video, width=1080, height=1920, x_center=1080/2, y_center=1920/2)

    # load subtitles
    generator = lambda txt: TextClip(txt, 
                                     font="mrbeast", 
                                     fontsize=25, 
                                     stroke_width=2,
                                     stroke_color="black",
                                     color="white",
                                     method='caption',
                                     size=(1080, None))
    subtitles = SubtitlesClip(args.subtitles, generator)

    # add subtitles to video
    video = video.set_audio(audio)

    result = CompositeVideoClip([video, subtitles.set_pos(('center'))])

    # save video
    result.write_videofile(args.output, codec='libx264', audio_codec='aac', fps=30)
