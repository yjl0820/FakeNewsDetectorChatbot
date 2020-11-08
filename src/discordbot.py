import discord
import MMmodel as mm

true_ = './FakeNewsChatbot/Volume/data/True.csv'
fake_ = './FakeNewsChatbot/Volume/data/Fake.csv'

X,Y = mm.preprocessing(fake_,true_)
model, tok = mm.modeling(X,Y)

client = discord.Client()

@client.event  
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('/FakeNews'):
        try:
            val = message.content[10:]
            result = mm.input_(model,val,tok)
            await message.channel.send(f"The article or article's title that you gave me is {round(100*result,2)}% chance FAKE!")
        except:
            await message.channel.send("Please Write your Fake News Title with /FakeNews <Article>")

    print(f'{client.user} has connected to Discord!')

client.run('DISCORD BOT API TOKEN')

