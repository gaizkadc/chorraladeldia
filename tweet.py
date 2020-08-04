# Imports
import chorrada_utils


# Main

# Get credentials, authenticate and check authenticated user
auth_stuff = chorrada_utils.get_twitter_credentials()
api = chorrada_utils.authenticate(auth_stuff)
chorrada_utils.check_credentials(api)

# Tweet content (pool of possible tweet texts)
pool_tweets = [
    "Cuidado, que va.",
    "No te jode...",
    "Para cagar y no echar mierda."
]

# Hashtags to be added after the tweet main text
hashtags = '\n#chorradadeldía'

# Create tweet
tweet = chorrada_utils.create_tweet(pool_tweets, hashtags)

# Get chorrada/image to tweet
chorrada = chorrada_utils.get_image()

# Tweet
api.update_with_media(chorrada, status=tweet)