# RedditShorts
The goal of this project is to create Short videos that read Reddit posts and comments.

> [!Note]
> Current Status: Reddit data scraping, tts, and video captions are in working minimal mode. Video generation, text to speech, and other functionality are still being built out further

## Usage
data_scraper.py: scrape posts from different subreddit
- currently supports scraping top n posts and top n comments (through the use of job files)
```
usage: data_scraper.py [-h] [-j JOB] [-o OUT]

Scrape data from reddit.

optional arguments:
  -h, --help         show this help message and exit
  -j JOB, --job JOB  Path to job file
  -o OUT, --out OUT  Output directory
```

a job example file can be seen below:
```
{
    "jobs": [
        {
            "subreddit": "AmItheAsshole",
            "num_comments": 10,
            "num_posts": 10
        },
        {
            "subreddit": "AskReddit",
            "num_comments": 10,
            "num_posts": 10
        }
    ]
}
```

Example usage: `python3 data_scraper.py -j jobs.json -o data-folder`

Currently jobs support getting `num_comments` best comments (sorted by best), and `num_posts` top posts for the defined `subreddit`. Jobs run one at a time in order of the json.

> [!IMPORTANT]  
> In order to connect to the Reddit API through praw you will need a `secret.json` file that has the following info:
> ``` 
> {
>     "client_id": "...",
>     "client_secret": "...",
>     "user_agent": "..."
> } 
> ```
> To find out how to create the API credentials see this [video tutorial](https://www.youtube.com/watch?v=r5ifZgbsMok&ab_channel=RunThat)

## TODO

- text to speech
    - blog of different options: https://ulife.ai/stories/top-free-text-to-speech-tts-libraries-for-python
    - using VIT model
- caption generation ?
    - how to make word level captions
- movie generation ?
    - what format do we want exactly?


## TTS Modelst
Models are saved under /Users/"user"/Library/Application Support/tts/"model name"