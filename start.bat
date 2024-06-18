set IRC_SERVER=<The server url of the server you want the bot to join>
set IRC_PORT=<The port of the server>
set IRC_NICK=<The nick/username of your IRC bot account>
set IRC_PASS=<The password of your IRC bot account>
set IRC_MOD_CHANNEL=<The IRC channel to look for suspicious messages>
set IRC_WARNINGS_CHANNEL=<The IRC channel to send suspicious messages to>
set IRC_CHAT_RELAY_WEBHOOK=<The Discord webhook to relay contents of IRC_MOD_CHANNEL to>
set IRC_WARNINGS_RELAY_WEBHOOK=<The Discord webhook to send suspicious messages to>
set ENABLE_DISCORD_BOT=<Set to "true" if you want to run the Discord bot responsible for Discord action logging commands>
set DISCORD_BOT_SECRET=<The token of your Discord bot>

python main.py
