# chorraladeldia
Twitter bot that tweets a random meme/chorrada/image from your private collection.

## What you need
* Twitter credentials of your app, that will be set in `credentials.py`. You can copy `credentials.py.sample`, remove the `.sample` part and put your credentials there.
* A folder named `chorradas` that will contain two folders: `unused` with the memes/chorradas/images yet to be tweeted and `used` with the already tweeted memes/chorradas/images.
```
chorradadeldia
 - chorradas
    - unused
    - used
```

## Environment variables
The bot takes environment variables that will be loaded from the `.env` file, which should look like:
```
APP_NAME=chorrada-del-dia
LOGS_FOLDER_PATH=logs

IMGS_FOLDER=chorradas
QUOTES_FILE_PATH=quotes.txt

TWITTER_POST=1

TWITTER_CONSUMER_KEY=<consumer key>
TWITTER_CONSUMER_SECRET=<consumer secret key>
TWITTER_ACCESS_TOKEN=<access token>
TWITTER_ACCESS_TOKEN_SECRET=<access token secret>
```

## Tweet your meme/chorrada/image
Create a `virtualenv` and activate it:
```
virtualenv venv
```
```
source venv/bin/activate
```

Install all necessary packages:
```
pip install -r requirements.txt
```

Run the bot:
```
python chorrada-del-dia.py
```

Deactivate your `virtualenv` when you are done:
```
deactivate
```