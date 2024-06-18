#!/bin/sh
export IRC_NICK="<The nick/username of your IRC bot account>"
export IRC_PASS="<The password of your IRC bot account>"
export IRC_MOD_CHANNEL="<The IRC channel to look for suspicious messages>"
export IRC_WARNINGS_CHANNEL="<The IRC channel to send suspicious messages to>"
export IRC_CHAT_RELAY_WEBHOOK="<The Discord webhook to relay contents of IRC_MOD_CHANNEL to>"
export IRC_WARNINGS_RELAY_WEBHOOK="<The Discord webhook to send suspicious messages to>"
export ENABLE_DISCORD_BOT="<Set to 'true' if you want to run the Discord bot responsible for Discord action logging commands>"
export DISCORD_BOT_SECRET="<The token of your Discord bot>"

python3 main.py
