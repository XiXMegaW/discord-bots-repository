import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user}is ready to be used!")

@client.event
async def on_message(message): #the "message" in the on_message(message) is the variable used under

    prefix = "?" #change this to anything to change the prefix of your "commands" (You don't actually need this, but it's just easier to change the code)

    if message.content.lower() == f"{prefix}test": #Don't forget to do message.content , or else it won't show the message 2.Don't forget the lower() with (), or else it will break (.lower lowers the text)
        await message.send(f"Your message here") #the f in (f"") is used to insert variables in the message

    if message.content.lower() == f"{prefix}delete":
        await message.delete() #Deletes the original message
        await message.send("Message deleted!")
    
    if message.author.get_role(1047316750154342492): #Just copy the ID of a role. (Go in the settings/advanced and then Developer)
        print("You have the \"hello\" role.")

    if message.channel.name == "Your Channel":
        print(f"You are using the {message.channel.name} channel.")

client.run("Put your bot token here. (Don't share it!)")
