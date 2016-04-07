port=""

echo "Setting iptables to forward UDP port"
read -p "What port do you want to forward? " port
# Open a port for OpenVPN
iptables -A INPUT -i eth0 -m state --state NEW -p udp --dport $port -j ACCEPT

# Allow TUN inteface connections to OpenVPN
iptables -A INPUT -i tun+ -j ACCEPT

# Allow TUN interface connections to be forwarded to other interfaces
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT


# NAT the VPN client traffic to the internet
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE

