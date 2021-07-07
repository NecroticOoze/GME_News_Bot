# GameStop Press Release Bot

This is a simple script that will perform get the most recent GameStop press release articles and programmatically to the Reddit subreddit r/Superstonk.

To deploy:

1. Create virtual environment, install dependencies via `pip install -r requirements.txt`

2. Create a Reddit app to use the API via https://reddit.com/prefs/apps

3. Create a new `config.py` file in the bot directory, copy the code from the `config_sample.py` and fill in the information.

4. Use crontab to run the `application.py` script every hour, every day. It should programmatically know when there is a new article and automatically post it to the subreddit r/Superstonk.
