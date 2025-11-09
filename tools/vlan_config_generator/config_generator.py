import ipaddress

def generate_config(vlan_id, vlan_name, subnet):
    net = ipaddress.ip_network(subnet, strict=False) #The strict=False argument allows it to correctly handle a subnet that might have a host address specified (e.g., if you mistakenly passed "192.168.10.1/26", it would still correctly identify the network as "192.168.10.0/26").
    
    gateway = list(net.hosts())[0] #The net.hosts() method returns an iterable of all usable host IP addresses in the network.By converting it to a list and taking the first element ([0]), it assigns the first usable IP address in the subnet to the gateway variable. This is a common convention for setting the default gateway (or the router's interface IP) on the network.
    
    config = f"""
    interface GigabitEthernet0/0.{vlan_id}
    encapsulation dot1Q {vlan_id}
    ip address {gateway} {net.netmask}
    description {vlan_name}_VLAN
    """
    return config.strip()

vlans = [
    {"id": 10, "name": "USERS", "subnet": "192.168.10.0/26"},
    {"id": 20, "name": "SERVERS", "subnet": "192.168.10.64/26"},
]

for vlan in vlans:
    print(generate_config(vlan["id"], vlan["name"], vlan["subnet"]))