import discord, json, requests, random, datetime
from dotenv import dotenv_values

# Discord API token
config = dotenv_values(".env")

# Annoying bot
annoying_mode = False

# The bird that chirps
bird = ["You're 10 ply", #0
        "Chicken feet", #1
        "Your lives are so sad, I get a charity tax break just for hangin' out with ya", #2
        "Maybe if you'd ever been in a real fight, you may not be so keen for another.", #3
        "Oh c'mon kitten, I wont tell anyone"] #4

# Calling all discord functions (and extending them)
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # When text channel receives a message bot will either:
  async def on_message(self, message):
    parrot = message.content
    tcontc = random.randint(0, 9)
    global annoying_mode
    
    # Do nothing for messages it sends itself
    if message.author == self.user:
      return
    
    # Tell you you're worthless
    elif message.content.startswith("!hockey"):
      await message.channel.send("Hockey is Awesome.")

    # Delete messages
    elif message.content.startswith("!clear"):
      deleted = await message.channel.purge(limit= 10)
      await message.channel.send(f'Deleted {len(deleted)} message(s)')

    elif message.content.startswith("!annoyme"):
      annoying_mode = not annoying_mode

    if annoying_mode == True:
      # Insult the user
      if tcontc == 6:
        await message.channel.send(random.choice(bird))
      
      # Parrot the user
      elif message.author != self.user:
        await message.channel.send(parrot)

  async def on_raw_message_delete(self, payload):
    global annoying_mode
    if annoying_mode == True:
      current_channel = client.get_channel(payload.channel_id)
      await current_channel.send("What are ya hidin' bud?")

  # When user joins / leaves voice channel
  # Furious George's Corner General ch_id: 354022119136559116
  # Furious George's Corner Coding-Stuff ch_id: 1153441248330391713
  async def on_voice_state_update(self, member, before, after):
    if member.voice.self_mute is True:
      coding_ch = client.get_channel(1153441248330391713)
      await coding_ch.send("We don't hear you, or we're not listening...")

    if member.voice.self_mute is False:
      coding_ch = client.get_channel(1153441248330391713)
      await coding_ch.send("SPEAK")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(config["API_KEY"])
