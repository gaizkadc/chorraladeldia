import os
import chorrada_utils
import twitter_utils

from dotenv import load_dotenv
load_dotenv()


# get logger
logger = chorrada_utils.get_logger()
logger.info('chorrada-del-dia started')

# create caption
quotes_file_path = os.getenv('QUOTES_FILE_PATH')
caption = chorrada_utils.create_caption(logger, quotes_file_path)

# Hashtags to be added after the tweet main text
hashtags = '\n#chorradadeldía'

# Create tweet
tweet = twitter_utils.create_tweet(logger, caption, hashtags)

# Rename images in unused folder
chorradas_path = os.getenv('IMGS_FOLDER')
unused_path = chorradas_path + '/unused/'
chorrada_utils.rename_images(logger, unused_path)

# Get chorrada/image to tweet
chorrada_path = chorrada_utils.get_image(logger)

# Tweet
if os.getenv('TWITTER_POST') == '1':
    twitter_utils.tweet_img(logger, chorrada_path, caption)

logger.info('done ✅')
