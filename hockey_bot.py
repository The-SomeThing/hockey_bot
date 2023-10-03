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
    if message.author == self.user:
      return
    
    if message.content.startswith("$hockey"):
      await message.channel.send("Hockey is Awesome but you are not.")

  async def on_message_delete(self, message):
    await message.channel.send("What are ya hidin' bud?")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["API_KEY"])






# When line 22 doesn't pass the "self" argument it spits out this message: (Why?)

# await coro(*args, **kwargs)
#          ^^^^^^^^^^^^^^^^^^^^^
# TypeError: MyClient.on_message_delete() takes 1 positional argument but 2 were given