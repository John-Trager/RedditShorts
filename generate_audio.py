'''
Take in json of reddit posts and output audio file for each post
'''
from tts import get_vit_synthesizer, gen_and_save_audio
import os
import json
from utils import log
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser("Generate narration audio files for reddit posts")
    parser.add_argument('-d','--data', type=str, default='test-data', help='Directory containing json files of reddit posts', required=True)
    parser.add_argument('-o','--out', type=str, default='test-data/audio', help='Directory to save audio files')
    args = parser.parse_args()
    data_dir = args.data
    audio_dir = args.out

    # check if data directory exists
    if not os.path.isdir(data_dir):
        raise Exception(f'Could not find data directory: {data_dir}')
    
    # check if audio directory exists
    if not os.path.isdir(audio_dir):
        os.mkdir(audio_dir)

    syn = get_vit_synthesizer()

    # loop through all json files in data_dir
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            with open(os.path.join(data_dir, filename)) as f:
                posts = json.load(f)

            # loop through all posts in json file
            for post in posts:
                # generate audio file
                text = post['title'] + ' ' + post['body']

                # TODO: process the text based on some rules (e.g. remove links, remove emojis, etc. and expand shorthand words/sayings)

                gen_and_save_audio(syn, text, f'{audio_dir}/{post["id"]}.wav')
                log(f'Generated audio for {post["id"]}')
