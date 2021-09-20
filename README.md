# Raccoon
Raccoon - Nexas Mod Manager for servers

This is a server sided mod manager designed to be used within a stack on docker to allow the adding, removing and updating of mods from Nexus Mods

## Thought process


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


## Python Libraries
### Discord Bot API
[discord.py](https://github.com/Rapptz/discord.py)
### Nexus Mod API
[A python wrapper for the Nexus API](https://github.com/GandaG/pynxm)

## Resources
[Discord Cummunity Resources](https://discord.com/developers/docs/topics/community-resources)

[Nexus Mods Resources](https://app.swaggerhub.com/apis-docs/NexusMods/nexus-mods_public_api_params_in_form_data/1.0)

Similar project [mod-manager-server](https://github.com/devon-wolf/mod-manager-server)
