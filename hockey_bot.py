import discord, json, requests
from dotenv import dotenv_values

config = dotenv_values(".env")

#def get_meme():
#  response = requests.get("https://meme-api.com/gimme")
#  json_data = json.loads(response.text)
#  return json_data["url"]

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    chirp = message.content

    if message.author == self.user:
      return
    
    if message.content.startswith("$hockey"):
      await message.channel.send("Hockey is Awesome but you are not.")

    elif message.author != self.user:
      await message.channel.send(chirp)

  async def on_raw_message_delete(self, payload):
    current_channel = client.get_channel(payload.channel_id)
    await current_channel.send("What are ya hidin' bud?")



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["API_KEY"])
