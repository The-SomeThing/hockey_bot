import discord, json, requests, random
from dotenv import dotenv_values

config = dotenv_values(".env")

#def get_meme():
#  response = requests.get("https://meme-api.com/gimme")
#  json_data = json.loads(response.text)
#  return json_data["url"]

#The bird that chirps
bird = ["You're 2 ply", #0
        "Chicken feet", #1
        "Your lives are so sad, I get a charity tax break just for hangin' out with ya", #2
        "Maybe if you'd ever been in a real fight, you may not be so keen for another.", #3
        "Oh c'mon kitten, I wont tell anyone"] #4

#Calling all discord functions (and extending them)
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # When text channel receives a message bot will either:
  async def on_message(self, message):
    parrot = message.content
    tcontc = random.randint(0, 9)
    
    # Do nothing for messages it sends itself
    if message.author == self.user:
      return
    
    # Tell you you're worthless
    if message.content.startswith("$hockey"):
      await message.channel.send("Hockey is Awesome but you are not.")

    # Insult the user
    elif tcontc == 6:
      await message.channel.send(random.choice(bird))

    # Parrot the user
    elif message.author != self.user:
      await message.channel.send(parrot)


  async def on_raw_message_delete(self, payload):
    current_channel = client.get_channel(payload.channel_id)
    await current_channel.send("What are ya hidin' bud?")



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["API_KEY"])
