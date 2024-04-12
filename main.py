import discord
import os

from dotenv import load_dotenv
load_dotenv()

token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        await channel.send('Say hello!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

# # app id: 1228304487639158895
# # public key: 17bd2421abbd19876ba758ec7fbc557fbb7fa67c3da6eb099129494e59c85513
