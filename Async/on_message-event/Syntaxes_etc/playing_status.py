#this code will demonstrate on adding up a playing status for the bot

#now lets add a simple playing status when the bot is ready!
@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="It's a bot"))

#now let's try something different, this one we are going to put a streaming status
'''if you already have the:
@client.event
async def on_ready():, DO NOT ADD IT AGAIN!!
alright here let's make it!'''
@@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name="With Players!", url="https://twitch.tv/T", type=1)) #the url is needen so it can show the actual streaming status, if not putten, it will show a playing on PC and when you click on profile, it will show streaming, so in conclusion, adding url makes it show a streaming status!

#now lets do an advanced one where we are going to count members the bot is "Listening"
@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name=f"{len(client.get_all_members())} Players!", type=2))
 



	