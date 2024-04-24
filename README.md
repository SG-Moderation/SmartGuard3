# SmartGuard 3

<img src="./assets/SmartGuard.png" align="right"
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
## WIP
