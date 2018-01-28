#!/usr/bin/python3
################################################################################
#                                   DISPOST                                    #
################################################################################
# Author:      Simon Ebnicher, IW3BWH                                          #
# Verison:     1.0                                                           #
# License:     GPLv3                                                           #
# Description: Small wrapper for Discord Webhooks to easily post messages to   #
#              different text channels.                                        #
# Usage:       ./dispost.py "<channelname>" "<message>"                        #
################################################################################

### IMPORTS ####################################################################
import sys
import json
import requests

### GLOBALS ####################################################################
CONFIG_PATH = "config.json"

#### MAIN ######################################################################
def main():
	# read config
	config_json = read_config()
	
	# get command line arguments and print help if number is not matching
	if len(sys.argv) != 3:
		print_help(config_json)
		sys.exit(1)
	channel_name = sys.argv[1]
	message      = sys.argv[2]
	
	# get channel url by channel name
	channel_url = get_channel_url(channel_name, config_json)
	if not channel_url:
		print("")
		print("Error: Channel not found.")
		print_help(config_json)
		sys.exit(1)
	
	# send message
	status_code = send_message(message, channel_url)
	if status_code < 200 or status_code > 299:
		print("Error sending message")
		sys.exit(1)


### HELPERS ####################################################################

def read_config():
	with open(CONFIG_PATH, 'r') as fd:
		config_json = json.load(fd)
	return config_json


def get_channel_url(channel_name, config_json):
	for elem in config_json['webhooks']:
		if elem['name'] == channel_name:
			return elem['url']


def send_message(message, channel_url):
	req = requests.post(channel_url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'content': message})
	return req.status_code


def print_help(config_json):
	print("")
	print("Usage: ./dispost.py \"<channelname>\" \"<message>\"")
	print("")
	print("Available Channels:")
	for elem in config_json['webhooks']:
		print("\t" + elem['name'] + "\t\t" + elem['description'])
	print("")

### END ########################################################################

if __name__ == "__main__":
	main()
	sys.exit(0)
