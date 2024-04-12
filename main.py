import discord
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

token = os.getenv("SECRET_KEY")
genai.configure(api_key=os.getenv("GEMINI_KEY"))

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)

convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["hi"]
    },
    {
        "role": "model",
        "parts": ["Hi there! 👋 How can I help you today?"]
    },
])

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        convo.send_message(message.content)

        channel = message.channel
        await channel.send(convo.last.text)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

