"""
ipaddress is a built-in Python module for IP math—no external installs needed.

.ip_network() automatically parses and validates input.

.hosts() returns all usable host IPs (excluding network and broadcast).

"""

import ipaddress

subnet = input("Enter subnet (e.g. 192.168.10.0/26): ")
net = ipaddress.ip_network(subnet, strict=False)

print(f"Network: {net.network_address}")
print(f"Broadcast: {net.broadcast_address}")
print(f"Usable Hosts: {list(net.hosts())[0]} - {list(net.hosts())[-1]}")
