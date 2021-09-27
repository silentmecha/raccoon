# -- NOTICE FOR TESTING BRANCH -- 

Still requires updates and configuration pending dev environment results from ''replit'' repo. 

# Raccoon
Raccoon - Nexas Mod Manager for servers

This is a server sided mod manager designed to be used within a stack on docker to allow the adding, removing and updating of mods from Nexus Mods

## Thought process
1. Check if tokens are set for both `DISCORD_API_TOKEN` and `NEXUS_API_TOKEN`
2. Load config
3. Download mods into folder (name to be determined) and update config using manifest file.
4. Copy over mods into `BepInEx` folder ( Can be moved to `entry.sh`? )
5. Init Discord bot to listen for commands
6. Thread update check on installed mods from config. ( Update check interval to be determined )
7. If update available then bot must notify

### Notes
`entry.sh` needs to wait for Racoon [init to complete](#discord-health-check) before transfering over the config files from git


### Environment Variables

| Variable Name     | Default Value | Description |
|-------------------|---------------|-------------|
| NEXUS_API_TOKEN   |               |             |
| DISCORD_API_TOKEN |               |             |

### Discord Bot Commands

| Commands                 | Description                  |
|--------------------------|------------------------------|
| /add <mod id/mod url>    | Add a mod to the server      |
| /remove <mod id/mod url> | Remove a mod from the server |
| /list                    | Get a list of installed mods |
| /check                   | Manaul check for updates     |
| /help                    | List the above commands      |

## Temperary dev environment
https://replit.com/@MartinnRoelofse/Racoon-dev

## Python Libraries
### Discord Bot API
[discord.py](https://github.com/Rapptz/discord.py)
### Nexus Mod API
[A python wrapper for the Nexus API](https://github.com/GandaG/pynxm)

## Resources
###### [Discord Cummunity Resources](https://discord.com/developers/docs/topics/community-resources)

###### [Nexus Mods Resources](https://app.swaggerhub.com/apis-docs/NexusMods/nexus-mods_public_api_params_in_form_data/1.0)

###### [Wait for service](https://stackoverflow.com/a/52322884)

###### [Discord Health Check](https://github.com/psidex/DiscordHealthCheck)

###### Similar project [mod-manager-server](https://github.com/devon-wolf/mod-manager-server)
