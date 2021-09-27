import os
import discord
import pynxm

# how to read arguments from commandline into program.
# will need to do some syntax fixing so as to read "arg=key" where key is unknown

nexus_token=os.getenv('NEXUS_API_TOKEN')
discord_toekn=os.getenv('DISCORD_API_TOKEN')
#max_backup_count=os.getenv('RACC_BACK_COUNT_MAX')
#beckup_interval=os.getenv('RACC_BACK_INTERVAL')