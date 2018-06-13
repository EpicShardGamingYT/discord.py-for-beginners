import discord
from discord.ext import commands

import sys, traceback

"""
a basic cogs example in discord.py rewrite
if u notice any issues please create a issue or a pull request
"""


def get_prefix(bot, message):
    """Gets our prefix. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Good idea to not have a really long prefix
    prefixes = ['mybotprefix']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow a special prefix to be used in DMs
        return 'DMPREFIX'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list (line 15).
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme, it dont need 2 be in a folder, can be in same dir.
# Think of it like a dot path import (replace / with .)
# You can load a cog in a cmd by bot.load_extension("folder.name")
initial_extensions = ['cogs.simple',
                      'cogs.status',
                      'cogs.owner']
#gets the bot prefix from the method we have at line 11
bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

# Here we load our extensions(cogs) from the inital_exentions list
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()




bot.run('TOKEN', bot=True, reconnect=True)
