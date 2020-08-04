# Imports
import tweepy
import credentials
import random
import os
import uuid
import shutil


# Get Twitter Credentials
def get_twitter_credentials():
    consumer_key = credentials.CONSUMER_KEY
    consumer_secret = credentials.CONSUMER_SECRET
    access_token = credentials.ACCESS_TOKEN
    access_token_secret = credentials.ACCESS_TOKEN_SECRET
    auth_stuff = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }
    return auth_stuff


# Authenticate
def authenticate(auth_stuff):
    auth = tweepy.OAuthHandler(auth_stuff['consumer_key'], auth_stuff['consumer_secret'])
    auth.set_access_token(auth_stuff['access_token'], auth_stuff['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


# Check credentials and print authenticated user
def check_credentials(api):
    user = api.me()
    print(user.name)


# Create tweet
def create_tweet(pool_tweets, hashtags):
    tweet = pool_tweets[random.randint(0, len(pool_tweets) - 1)] + hashtags
    return tweet


# Get image
def get_image():
    # Get paths
    path = os.path.abspath(os.getcwd())
    used_path = path + '/chorradas/used/'
    unused_path = path + '/chorradas/unused/'

    # Move image
    images = os.listdir(unused_path)
    old_image, extension = os.path.splitext(unused_path + images[0])
    if extension == 'jpeg':
        extension = 'jpg'

    final_image_name = str(uuid.uuid4())
    final_image_path = used_path + final_image_name + extension.lower()
    old_image_path = unused_path + images[0]
    os.rename(old_image_path, final_image_path)

    # Check image folders
    check_unused_folder(unused_path, used_path)

    return final_image_path


# Check if unused folder is empty
def check_unused_folder(unused_path, used_path):
    unused_images = os.listdir(unused_path)
    used_images = os.listdir(used_path)
    if len(unused_images) == 0:
        for _, image_name in enumerate(used_images):
            shutil.move(used_path + image_name, unused_path)