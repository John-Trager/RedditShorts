'''
script with helper and utility functions
'''
import praw
import json
from datetime import datetime

### Reddit specific util functions ###

def get_redis_instance() -> praw.Reddit:
    """Returns a reddit instance"""
    # Reddit API credentials (get from secret.json)
    with open('secret.json') as f:
        secret = json.load(f)
        client_id = secret['client_id']
        client_secret = secret['client_secret']
        user_agent = secret['user_agent']
        username = secret['username']
        password = secret['password']

    # Create reddit instance
    reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username, 
                     password=password
                    )
    
    return reddit

def get_best_comments(post, limit: int):
    # Set comment sort to best before retrieving comments
    comments = []
    post.comment_sort = 'best'
    
    # TODO: currently dirty way to set comment limit
    # and potentially could fail if there are more than 15
    # stickied/deleted comments
    post.comment_limit = limit + 15
    
    num_actual_comms = 0
    for top_level_comment in post.comments:

        if num_actual_comms >= limit:
            break

        if isinstance(top_level_comment, praw.models.MoreComments) or \
           top_level_comment.body == '[deleted]' or \
           top_level_comment.stickied:
            continue

        # Here you can fetch data off the comment.
        # For the sake of example, we're just printing the comment body.
        comments.append([top_level_comment.body, top_level_comment.score])
        num_actual_comms += 1

    return comments


### More general util functions ###

def get_string_time_now() -> str:
    """Returns the current time in string format"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def log(*args):
    """Logs a message to the console with timestamp"""
    # color the timestamp
    timestamp = get_string_time_now()
    timestamp = f'\033[92m[{timestamp}]\033[0m'
    print(f"{timestamp} " + " ".join(map(str, args)))

def log_warn(*args):
    """Logs a warning message to the console with timestamp"""
    timestamp = get_string_time_now()
    timestamp = f'\033[33m[{timestamp}] Warning:\033[0m'
    print(f"{timestamp} " + " ".join(map(str, args)))

def log_error(*args):
    """Logs an error message to the console with timestamp"""
    # color the timestamp red
    timestamp = get_string_time_now()
    timestamp = f'\033[91m[{timestamp}] Error:\033[0m'
    print(f"{timestamp} " + " ".join(map(str, args)))