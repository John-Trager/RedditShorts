'''
This file will be used to scrape data from reddit and output it into a json file.
'''
import os
import json
from utils import *
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Scrape data from reddit.')
    parser.add_argument('-j', '--job', type=str, default='jobs.json', help="Path to job file")
    parser.add_argument('-o', '--out', type=str, default='data', help="Output directory")
    args = parser.parse_args()

    if not os.path.exists(args.out):
        log(f'Creating output directory {args.out}')
        os.makedirs(args.out)

    reddit = get_redis_instance()

    with open(args.job) as f:
        job = json.load(f)
        jobs = job['jobs']

    for job in jobs:

        if os.path.exists(f'{args.out}/{job["subreddit"]}.json'):
            log_warn(f'{args.out}/{job["subreddit"]}.json already exists. Skipping...')
            continue 

        subreddit = reddit.subreddit(job['subreddit'])
        top_subreddit = subreddit.top(limit=job['num_posts'])

        posts = []
        for post in top_subreddit:
            log(subreddit.display_name, post.title)

            comments = get_best_comments(post, job['num_comments'])
            
            posts.append(
                {
                "title": post.title,
                "body": post.selftext,
                "score": post.score,
                "id": post.id,
                "url": post.url,
                "num_comments": post.num_comments,
                "created": post.created,
                "top_comments": comments
                })

        with open(f'{args.out}/{job["subreddit"]}.json', 'w') as f:
            json.dump(posts, f, indent=4)

                        