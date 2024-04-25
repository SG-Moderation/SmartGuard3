# SmartGuard 3

<img src="./assets/SmartGuard_TransparentBG.png" align="right"
 alt="SmartGuard logo by s20 and GreenBlob" width="192" height="192">

This is an IRC moderation bot made for in-game chat relays to IRC. It aids moderation by reading messages received real-time in channels and narrowing them down into suspicious messages that may contain potential swears or chat abuse. With this tool, you don't have to read every single message in the chat you're moderating; this bot narrows everything down to a _way_ smaller collection.
> Note: Since this bot is made for in-game chat relays, it treats the first word of any message as the sender.

## Ability

Most cases of swearing, swear filter bypass, and other forms of chat abuse are caught:
- Blending with other words: `hellofvck3you`
- Repetition or distortion: `sSsHhh5%*IITtt!`
- Multiline:
    ```
    <user> f
    <user> u
    <user> you
    ```
- Usage of ignorable characters: `s_h_! t`
- Swear word variants: `phuq`
- Spamming: `ssssstttttooooooooopppppppp`
- All caps: `THIS MESSAGE IS ALMOST in ALL CAPS`
- Sending messages too fast:
    ```
    <user> aaaaaaaaaaaaaaaaa
    <user> aaaaaaaaaaaaaaaaa
    <user> aaaaaaaaaaaaaaaaa
    <user> aaaaaaaaaaaaaaaaa
    ```
## Running the Bot

### Running on Replit

You can run this bot by forking it and running it [on Replit](replit.com/@a-blob/SmartGuard3). With that, you need to define a few necessary "secrets" on Replit through the "secrets" tab. The following "secrets" are required:
| Key | The value to put in |
|--|--|
| `IRC_NICK` | The nick/username of your IRC bot account |
| `IRC_PASS` | The password of your IRC bot account  |
| `IRC_MOD_CHANNEL` | The IRC channel to look for suspicious messages |
| `IRC_WARNINGS_CHANNEL` | The IRC channel to send suspicious messages to |
| `IRC_CHAT_RELAY_WEBHOOK` | The Discord webhook to relay contents of `IRC_MOD_CHANNEL` to |
| `IRC_WARNINGS_RELAY_WEBHOOK` | The Discord webhook to send suspicious messages to |
| `DISCORD_BOT_SECRET` | The token of your Discord bot |

### Running Locally

To run the bot locally, you can clone this repository to your computer, customise the environment variables defined in the `start.bat` or `start.sh` file according to the description of each variable/key provided above, and run the `start.bat` or `start.sh` file to start the bot.

## Using the SmartGuard 3 Action Logging Features

SmartGuard 3 comes along with several logging commands to keep track of warnings, temp-bans, and perma-bans issued to a player. It stores this information in an SQLite database. These commands work both from the IRC channel as well as the Discord channels that SmartGuard has access to. The bot command prefix is `!`. In Discord, you can also run these as [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ).

- To initialise the action logger, first setup the database by using the `create` command.
  ```
  !create
  ```
  Upon successful execution, it will return a message saying that the database was created.
- If you wish to delete the database, use the `delete` command.

Below is an explanation of the various logging commands:
- `!warn <player> <increment>`: Logs warnings with an increment specifying the severity. Please use whole number values. For example:
  ```
  !warn s20 1
  ```
- `!tempban <player>`: Logs temp-bans.
- `!ban <player>`: Logs a perma-ban.
- `!unban <player>`: Unbans a player.
- `!retrieve <player>`: Retrieves the logs for a player.

For the Discord counterpart of the logging functionality, you can use the built-in `help` command to get a quick list of all the available commands and their general usage.