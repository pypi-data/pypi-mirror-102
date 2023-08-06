import discord
from discord.ext import commands
import time
import os
from colorama import init, Fore, Style

init()

def yellow(text):
	return Fore.YELLOW + text + Style.RESET_ALL

def green(text):
	return Fore.GREEN + text + Style.RESET_ALL

def red(text):
	return Fore.RED + text + Style.RESET_ALL
class botUtils:
	class bot:
		def __init__(self, settings: {settings['logging']: "advanced"}):
			self.bot = '';
			try:
				self.logging = settings['logging']
			except:
				self.logging = "advanced"

			try:
				self.prefix = settings['prefix']
			except:
				self.prefix = "!"
				print("Error, you need to define the prefix, it has been set to \"!\"")

		def make(self):
			self.bot = commands.Bot(command_prefix=self.prefix)
			if self.logging == 'advanced':
				print(green(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Bot made with prefix [{self.prefix}]")
			elif self.logging == 'normal':
				print(f"[{time.asctime(time.localtime(time.time()))}]", f"\032 Bot made with prefix [{self.prefix}]")
			else:
				pass
			return self.bot;

		def run(self, token):
			@self.bot.event
			async def on_ready():
				if self.logging == 'advanced':
					print(green(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Bot online.")
				elif self.logging == 'normal':
					print(f"[{time.asctime(time.localtime(time.time()))}]", f"\032 Bot online.")
				else:
					pass
				self.bot.remove_command("help") 
				return

			self.bot.run(token)

		def loadCogs(self, cogs):
			for cog in cogs:
				try:
					print(yellow(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Loading [{cogs[cog]}]")
					self.bot.load_extension(cogs[cog])
					print(green(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Loaded [{cogs[cog]}]")
				except:
					print(red(f"[{time.asctime(time.localtime(time.time()))}]"), f"\032 Failed To Load [{cogs[cog]}]")
		def get(self):
			def getBot(self):
				return self.bot

			def getSettings(self):
				return {'logging': self.logging, "prefix": self.prefix}

			def getAll(self):
				return {'settings': {'logging': self.logging, "prefix": self.prefix}, "bot": self.bot}