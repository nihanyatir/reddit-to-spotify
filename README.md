# reddit-to-spotify
Add songs shared on r/Music to a Spotify playlist.

Version: Python 3.8.4

How it works:
If you're subscribed to r/Music, you must have noticed that redditors share songs as Youtube links so I can't scrape links and directly add them to a playlist. And they use this format: artist - song [genre] (eg. Alabama Shakes - Hold On [Blues Rock/Soul]). So what I did was take only the title of the shared songs and drop the genre part (because I don't need to add that when I search the title on Spotify) and add the results to a playlist I had created for this project.

How to use:

Note that you need to apply for Spotify Developers to get your credentials to use in this project.

-Download the .py file.
-Open Command Prompt or Terminal depending on which OS you're using.
-Go to the directory where you downloaded the file with 'cd' command.
-Run it on your Command Prompt or Terminal with the following command:
python reddit_to_spotify.py
-And voila! You have the last 15 songs shared on r/music subreddit.
