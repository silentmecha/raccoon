import sys
import discord
import pynxm

# how to read arguments from commandline into program.
# will need to do some syntax fixing so as to read "arg=key" where key is unknown


if len(sys.argv) == 1:
        print("Usage: %s -f" % sys.argv[0])  
        exit()

for argument in sys.argv:
        if argument == "-NEXUS_API_TOKEN=</ insert token here/>":  # this needs fixing
                apitoken=%NEXUS_API_TOKEN  