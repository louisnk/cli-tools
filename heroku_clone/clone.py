import sys
import re
from string import Template

class colors:
	BLUE = '\033[1;34m'
	GREEN = '\033[1;32m'
	YELLOW = '\033[1;33m'
	RED = '\033[1;31m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

print " "
print colors.YELLOW + "Welcome to the Heroku Clone CLI to clone a new Heroku instance from the existing app of your choice, let's walk through the steps..." + colors.ENDC

app = raw_input(colors.ENDC + "\nFirst, what's the Heroku app named?: " + colors.GREEN)
prefix = raw_input(colors.ENDC + "\nSecond, what do you want the new client prefix to be? (never displayed, only used internally): " + colors.GREEN)
name = raw_input(colors.ENDC + "\nNow the client's name, typed exactly as you want it displayed: " + colors.GREEN)
sgId = raw_input(colors.ENDC + "\nTheir SurveyGizmo survey ID: " + colors.GREEN)
logoPath = raw_input(colors.ENDC + "\nThe file name of their logo: " + colors.GREEN)
contentPath = raw_input(colors.ENDC + "\nThe name to their content.json file (leave blank to use client prefix): " + colors.GREEN)
dbUrl = raw_input(colors.ENDC + "\nThe Postgres connection string URL (leave blank to use cloned app's string): " + colors.GREEN)
gaCode = raw_input(colors.ENDC + "\nThe Google Analytics traciknig code to use: (leave blank to disable GA): " + colors.GREEN)
closeDate = raw_input(colors.ENDC + "\nWhen do you want this survey to end? (Please enter date in format YYYY-MM-DDThh:mm): " + colors.GREEN)

check = Template(colors.ENDC + "\nDoes this look right?"
+ "\nPrefix: " + colors.BLUE + "$prefix" + colors.ENDC
+ "\nName: " + colors.BLUE + "$name" + colors.ENDC
+ "\nSurvey id: " + colors.BLUE + "$id"  + colors.ENDC
+ "\nLogo path: " + colors.BLUE + "$logoPath" + colors.ENDC
+ "\nContent path: " + colors.BLUE + "../../content$contentPath" + colors.ENDC
+ "\nDatabase URL: " + colors.BLUE + "$dbUrl" + colors.ENDC
+ "\nGoogle Analytics tracking code: " + colors.BLUE + "$gaCode" + colors.ENDC
+ "\nClose date: " + colors.BLUE + "$closeDate" + colors.ENDC

+ "\n\n[" + colors.GREEN + "yes" + colors.ENDC + "/" + colors.RED + "no" + colors.ENDC + "]: ")

correct = raw_input(check.substitute(prefix=prefix, name=name, id=sgId, logoPath=logoPath, contentPath=contentPath, dbUrl=dbUrl, gaCode=gaCode, closeDate=closeDate))

regex = re.compile('^[yY]')

if regex.match(correct):
	print colors.GREEN + "\nBeginning the process..." + colors.ENDC
	# TODO: actually call the Heroku API and make the fork
else:
	print colors.RED + "\nPlease re-run the script to try again. \nGoodbye." + colors.ENDC
