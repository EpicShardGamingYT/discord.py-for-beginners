import discord
from discord.ext import commands

import sys, traceback

"""

Cogs example for re-write

Rewrite Documentation:
http://discordpy.readthedocs.io/en/rewrite/api.html
Rewrite Commands Documentation:
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html
"""


# dots represents folders
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.members',
                      'cogs.owner']

bot = commands.Bot(command_prefix="URPREFIX")

# Here we load our cogs listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'{extension} couldnt be loaded')
            traceback.print_exc()




bot.run('TOKEN', bot=True, reconnect=True)
