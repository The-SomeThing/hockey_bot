import discord, json, requests
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_meme():
  response = requests.get("https://meme-api.com/gimme")
  json_data = json.loads(response.text)
  return json_data["url"]

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith("$hockey"):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
#client.run('MTE1NzQxOTM1MTEyNTc5NDk2Ng.Gs0pjE.dbQmasXDjkXzCOEb1F-84q3nZJKByJi7WmrsgQ') # Replace with your own token.
client.run(config["API_KEY"])
