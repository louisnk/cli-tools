import boto3
import os
import re
from subprocess import call

ec2 = boto3.resource(
	'ec2',
	aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
	aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

vpnServer = ec2.Instance(os.environ['VPN_EC2_ID'])

def updateConfigs():
	updateEnvRC()
	updateOVPNconfig()
	print "Configs updated"

def startInstance():
	vpnServer.start()
	vpnServer.wait_until_running()
	print "VPN server started"

def startup():
	startInstance()
	updateConfigs()

def updateOVPNconfig():
	with open(os.environ['VPN_CONFIG_PATH'], 'r+') as vpnConfig:
		configList = filter((lambda s: len(s) > 0 and re.compile('\\n').match(s) is None), vpnConfig.read().split('\n'))
		vpnConfig.seek(0)
		configList.append('remote ' + vpnServer.public_ip_address)

		vpnConfig.write("\n".join(configList))
		vpnConfig.close()

	print "Updated the OpenVPN config remote IP"

def updateEnvRC():
	with open(".envrc", "r+") as envRc:
		envs = filter((lambda s: len(s) > 0 and re.compile('(VPN_REMOTE)|\\n').search(s) is None), envRc.read().split('\n'))
		envRc.seek(0)
		envRc.write("\n".join(["export VPN_REMOTE=" + vpnServer.public_ip_address] + envs))
		envRc.close()

		call(['direnv', 'allow'])

	print "Updated local .envrc $VPN_REMOTE variable with current VPN IP"

# Actually do the things
if vpnServer.state[u'Name'] == 'stopped':
	startup()
else:
	print "VPN server not started because it is currently " + vpnServer.state[u'Name'] + " at " + vpnServer.public_ip_address
	updateConfigs()
