# CLI-tools

##
* __heroku_clone/clone.py__ - a walkthrough to flexibly forking/cloning heroku apps, just run ``python clone.py``
	* a local `$HEROKU_CLONE_SACRED` env variable might contain something like this: `(AWS)|(_KEY)|(_SECRET)|(NODE_ENV)` to limit which env variables are changeable on a clone
* __./ip-tables.sh__ - a simple shell script to set iptables to forward VPN traffic on a port of your choice
* __./update.sh__ - a shell script to change the remote IP in an OpenVPN config, requires a relevant ``VPN_CONFIG_PATH`` env variable
