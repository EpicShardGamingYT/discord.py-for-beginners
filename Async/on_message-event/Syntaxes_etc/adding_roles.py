'''this one will demonstrate on adding roles which has been asked rarely but i fell like it will be not rarely soon,
anyways so how do you make it to add roles?
lets make examples there'''

#now lets make a command that the bot will add the admin role into me(you)!
if messsage.content.startswith("!admin"):
    if message.author.id == "<your_id>":
        role = discord.utils.get(message.server.roles, name="Admin") #head into docs for further info about discord.utils.get
        '''we are using if message.author in order to tell our bot that if only you are sending these and discord.utils.get will
        be used for the bot to catch/get the role'''
        #now lets make the sytax to add role:
        await client.add_roles(message.author, role)
        m = await client.send_message(message.channel, f"{message.author.mention}, Done!")
        await bot.delete_message(m)
       
#you gotta make sure that the bot has permission or you will get a FORBIDDEN error
        
        
