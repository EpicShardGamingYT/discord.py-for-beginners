#this is the beggining of making the on_message commands
@client.event
async def on_message(message):
    #this will demonstrate three ways of making it!
    if message.content == "ping":
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith("cookie"):
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith("COMMAND"):
        await client.send_message(message.channel, "what?")