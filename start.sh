#!/bin/sh
export IRC_NICK="<IRC nick/username>"
export IRC_PASS="<IRC password>"
export IRC_MOD_CHANNEL="<The IRC channel to moderate>"
export IRC_WARNINGS_CHANNEL="<The IRC channel to relay suspicious messages to>"
export IRC_CHAT_RELAY_WEBHOOK="<Discord webhook to relay chat to>"
export IRC_WARNINGS_RELAY_WEBHOOK="<Discord webhook to relay suspicious messages to>"
export DISCORD_BOT_SECRET="<The Discord bot token>"

python3 main.py
