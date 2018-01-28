# python-discord-wrapper
Small Python3 wrapper to post monitoring or other data to different text channels in Discord

## Dependencies
Python3 with packages "json" and "requests"

## Installation
1. Setup the webhooks in Discord for each text channel you wish to use
2. Create a "config.json" file from the example template, listing all your webhooks with sensible names and descriptions
3. Execute the python script: ./dispost.py channel_1 "my test message"
