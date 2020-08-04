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
* I would also recommend setting up your own tweet texts in `pool_tweets` in the file `tweet.py`

## Tweet your meme/chorrada/image
Create a `virtualenv`:
```
virtualenv venv
```

Install all necessary packages:
```
pip install -r requirements.txt
```

Run the bot:
```
python tweet.py
```