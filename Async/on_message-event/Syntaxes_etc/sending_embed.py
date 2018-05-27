'''this will demostrate on sending an embed message
take that example here:'''
if message.content.startswith("embed"):
    embed = discord.Embed(title="its a title", description="its a description", color=0xFFF000)
    await client.send_message(message.channel, embed=embed)

#lets make the embed more advanced!
if message.content.upper().startswith("HELLO"):
    embed1 = discord.Embed(title="Message Bot", description=f"Hello {message.author.name}, How are you?", color=message.author.color)
    embed1.set_thumbnail(url=message.author.avatar_url)
    embed1.set_footer(text="this was introduced for an example embed!")
    await client.send_message(message.channel, embed=embed1)