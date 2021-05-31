# flairmodbot

## What is this bot?

FlairModBot is a bot which helps you moderate. All you have to do is change the post flair and the bot will leave a comment and remove the post.

## Why use this bot?

Well, this is great for mobile moderation. Along with that, it reduces time spent modding, as you dont have to leave a removal reason and manually select a reason. It also helps not clutter up your profile. 

## How do I use this bot?

As of now, you can clone this repo or just copy and paste the code somewhere, it's pretty small.

## How do I run it?

Well, this bot can run on any server. However, you need to input some details into the [main.py](https://github.com/voicedm/flairmodbot/blob/main/main.py) file, after creating a new application at old.reddit.com/prefs/apps. Input the details into main.py, along with your subreddit name.

Followed by this, go to your subreddit tools and create a post flair with Mod Only permissions. After creating it, copy the ID of the flair and replace the flair ID currently given with your ID. After that, you can change the comment you want the bot to leave as well. 

After inputting all this, just run the script, and your bot should be alive! 

## To Do

- Make one bot which can be configured in a Reddit wiki page instead using YAML.

- Store all data in a SQL database.
