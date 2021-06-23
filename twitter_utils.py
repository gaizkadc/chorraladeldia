import tweepy
import os


def tweet_img(logger, img_path, caption):
    logger.info('tweeting image')

    credentials = get_twitter_credentials(logger)
    api = twitter_login(logger, credentials)

    api.update_with_media(img_path, status=caption)

    logger.info('chorrada tweeted')


def get_twitter_credentials(logger):
    logger.info('getting twitter credentials')

    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    credentials = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }

    logger.info('twitter credentials retrieved')

    return credentials


def twitter_login(logger, credentials):
    logger.info('logging in twitter')

    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)

    logger.info('logged in twitter')

    return api


def create_tweet(logger, caption, hashtags):
    logger.info('creating tweet')
    tweet = '"' + caption + '"' ++ hashtags

    logger.info('tweet created: ' + tweet)

    return tweet
