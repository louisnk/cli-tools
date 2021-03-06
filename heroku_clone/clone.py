import os
import re
from string import Template
from subprocess import call

yesRegex = re.compile('^[yY]')

def flatten(k):
	return flatten(k[0]) + (flatten(k[1:]) if len(k) > 1 else []) if type(k) is list else [k]

reps = 0

class colors:
	BLUE = '\033[1;34m'
	GREEN = '\033[1;32m'
	YELLOW = '\033[1;33m'
	RED = '\033[1;31m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

# All the methods to gather and store env variables for your forked app
class settingsCollector:
	def __init__(self):
		self.selectList = {}
		self.toChange = []
		self.toSet = {}

	def collectSettings(self):
		print "\nNow set the value of each env variable you want to set: "
		for i in self.toChange:
			self.toSet[self.selectList[int(i)]] = raw_input("\n" + self.selectList[int(i)] + ": ")

		return self

	def confirmSettings(self):
		print "\nDo these look right? \n"
		for key in self.toSet:

			print key + ": " + colors.GREEN + self.toSet[key] + colors.ENDC

		correct = raw_input("\n[y/n]: ")
		if yesRegex.match(correct) is not None:
			return self
		else:
			reps += 1
			if reps < 3: # because three strikes and you're out
				return self.collectSettings().confirmSettings()
			else:
				print "\nSorry, it seems we're not playing the same game, please try again."
				exit()

	def listEnvVars(self):
		customIgnores = (os.environ['HEROKU_CLONE_SACRED'] + '|') if 'HEROKU_CLONE_SACRED' in os.environ is not False else ''
		print ""
		for i,key in enumerate(heroku.existingEnvVars):
			if re.compile(customIgnores + '(DATABASE_URL)').search(key) is None:
				print "[" + str(i) + "] " + key
				self.selectList[i] = key
			else:
				if re.compile('DATABASE_URL').search(key) is None:
					self.toSet[key] = heroku.existingEnvVars[key]

		return self

	def selectEnvVars(self):
		print ""
		varsList = raw_input("\nWhat config variables do you want to change? Type the #s from the list above seperated by commas: ")

		if isinstance(varsList, str):
			self.toChange = self.splitVarsList(varsList)

		if len(self.toChange) < 1:
			if yesRegex.match(raw_input("\nIt looks like nothing was entered, want to try again? [y/n]:")) is not None:
				self.selectEnvVars()
			elif yesRegex.match(raw_input("\nAre you sure you want to exactly duplicate all env vars? ")) is not None:
				return self
			else:
				print "\nThanks for playing."
				exit()
		else:
			return self

	def splitVarsList(self, varsList):
		return list(map((lambda s: s.strip()), str.split(varsList, ',')))

# All the calls and prompts to interact with Heroku
class herokuHandler:
	def __init__(self):
		self.existingEnvVars = {}
		self.existingName = ""
		self.existingPipeline = ""
		self.newEnvVars = {}
		self.newName = ""

	def addRemote(self):
		print "\nCopy the following git URL into the next prompt: "
		call(['heroku', 'info', '-a', self.newName])
		gitUrl = raw_input("\nThe new git url, please: ")

		call(['git', 'remote', 'add', self.newName, gitUrl])

		return self

	def buildKeystring(self, settings):
		keyString = ""
		for key in settings:
			keyString += key +"="+ settings[key] + ","

		return str.split(keyString, ',')[:-1]

	def checkNewEnvVars(self):
		print colors.GREEN + "\nIf these all look right, you're done!" + colors.ENDC
		call(['heroku', 'config', '--app', self.newName])
		return self

	def fork(self):
		print colors.GREEN + "\nForking " + self.existingName + " to " + self.newName + colors.ENDC
		call(['heroku', 'fork', '--from', self.existingName, '--to', self.newName])
		return self

	def getEnvVars(self):
		def splitEnvVals(i):
			# Strip extra whitespace, replace full quotes, split on colons, then strip each individual piece again
			vals = map((lambda s: s.strip()), i.strip().replace('"', '').split(": "))
			self.existingEnvVars[vals[0]] = vals[1] # Build our existingEnvVars hashmap
			return

		print colors.GREEN + "\nCopy everything except the title from here:\n============================\n" + colors.ENDC
		call(['heroku', 'config', '--app', self.existingName])
		print colors.RED + "\n============================\nto here." + colors.ENDC

		varList = []
		sentinel = '__end'

		print "\nPaste it here, hit enter, type " + colors.BOLD + "__end" + colors.ENDC + ", and hit enter again when finished: "

		for line in iter(raw_input, sentinel):
			varList.append(splitEnvVals(line))

		return self

	def getExistingAppName(self):
		self.existingName = raw_input("\nWhat's the name of the existing Heroku app? ")
		return self

	def getExistingPipeline(self):
		self.existingPipeline = raw_input("\nWhat's the name of the existing deployment pipeline? [leave blank if it's not part of a pipeline]")
		return self

	def getNewAppName(self):
		self.newName = raw_input("\nWhat's the name of the new Heroku app? ")
		return self

	def sendToPipeline(self):
		if len(self.existingPipeline) > 0:
			call(['heroku', 'plugins:install', 'heroku-pipelines'])
			call(['heroku', 'pipelines:add', '--app', self.newName, self.existingPipeline])
		return self

	def setEnvVars(self, settings):
		self.newEnvVars = settings
		keyStrings = self.buildKeystring(settings)

		call(flatten(['heroku', 'config:set', keyStrings, '--app', self.newName]))

		return self

# Initialize our classes for env var collection
collector = settingsCollector()
heroku = herokuHandler()


print "\nWelcome to the Heroku Clone CLI - Let's walk through the process to clone a new Heroku instance from the existing app of your choice."

# Now run through all the methods and do all the things
heroku.getExistingAppName().getExistingPipeline().getEnvVars().getNewAppName().fork().sendToPipeline().addRemote().setEnvVars(
		collector.listEnvVars()
			.selectEnvVars()
			.collectSettings()
			.confirmSettings()
			.toSet # this ultimately returns the dictionary of key/values to set/update
	).checkNewEnvVars()


print colors.GREEN + "\nAll done" + colors.ENDC
exit()
