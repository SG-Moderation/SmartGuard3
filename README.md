# SmartGuard3

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


## How it Works

When you run SmartGuard3, it will log into IRC with `IRC_NICK` and `IRC_PASS`, and join both `IRC_MOD_CHANNEL` and `IRC_WARNINGS_CHANNEL`. It will also log into your Discord bot using the `DISCORD_BOT_SECRET` you provided.

It will relay all messages it receives in `IRC_MOD_CHANNEL` to the `IRC_CHAT_RELAY_WEBHOOK`, which should be a Discord webhook. For each message it receives, it will treat the first word of the message as the sender (e.g. `<user> hello`, `<user>` will be treated as the sender). It will determine if the rest of the message is suspicious or not. If it thinks it is suspicious and may contain swears or other forms of chat abuse, it will send the suspicious message into `IRC_WARNINGS_CHANNEL` in the format of `Player <user> said "<message goes here>"`, and send the same message to the `IRC_WARNINGS_RELAY_WEBHOOK`, which should be a Discord webhook.

For each user, the bot keeps a history of the last 20 messages that user sends. The history is used to detect if the user is committing chat abuse through multiple messages.


## Using the SmartGuard3 Action Logging Features

SmartGuard3 comes along with several logging commands to keep track of warnings, temp-bans, and perma-bans issued to a player. It stores this information in an SQLite database. These commands work both from `IRC_WARNINGS_CHANNEL` as well as the Discord channels that the SmartGuard Discord bot has access to. The bot command prefix is `!`. In Discord, you can also run these as [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ).

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


## Licenses

This project is licensed under the [GNU General Public License v3.0](LICENSE). The logo of this project - [`SmartGuard.png`](./assets/SmartGuard.png) -  is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) by @src4026 and @a-blob.
