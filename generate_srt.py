'''
Generates subtitle "srt" file from audio file and text file.

Some sources:
https://www.reddit.com/r/learnpython/comments/znidrx/is_there_a_way_to_get_wordlevel_timestamps_that/
https://www.youtube.com/watch?v=Zbze7zs8Kyk&ab_channel=PracticalAIbyRamsri
https://picovoice.ai/blog/how-to-create-subtitles-for-any-video-with-python/
'''

import stable_whisper

#  aligning audio to text
# load model
model = stable_whisper.load_model('large')

# load audio
audio_path = 'test-data/audio/ocx94s.wav'

# load text (TODO: need to process text to remove new lines and etc)
text_path = 'test-data/ocx94s.txt'
with open(text_path) as f:
    text = f.read()

# align audio to text
result = model.align(audio_path, text, 'en')

# save result as srt
result.to_srt_vtt('audio-ocx94s.srt')

# TODO: there are some issues with the srt file (like random color flags being generated
# also timestamps are sentence level not word level)