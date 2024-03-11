#!/bin/sh
export NICKNAME="<IRC nick/username>"
export PASSWORD="<IRC password>"
export CHANNEL1="<The IRC channel to moderate>"
export CHANNEL2="<The IRC channel to relay suspicious messages to>"
export CHANNEL3="<The IRC channel to run commands>"
export RELAY_WEBHOOK="<Discord webhook to relay chat to>"
export LOG_WEBHOOK="<Discord webhook to relay suspicious messages to>"
export DISCORD_BOT_SECRET="<The Discord bot token>"

python3 main.py
