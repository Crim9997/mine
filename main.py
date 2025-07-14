import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Add your commands here (like the ones from your original script)

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
from flask import Flask
import threading

# Create a dummy Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord Bot is Online", 200

if __name__ == "__main__":
    # Start the dummy server in a background thread
    threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
    ).start()
    
    # Start your Discord bot
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
