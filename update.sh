function setremote {
	local RED="\033[0;31m"
	local GREEN="\033[0;32m"

	read -p "Enter new OpenVPN IP: " ip
	if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
		eval 'sed -i.bak /^remote/d "$VPN_CONFIG_PATH"'
		echo "remote" $ip >> "$VPN_CONFIG_PATH"
		printf "\n${GREEN} IP updated, exiting."
		exit 1
	else
		printf "${RED}invalid ip"
		exit 1
	fi

}

setremote
