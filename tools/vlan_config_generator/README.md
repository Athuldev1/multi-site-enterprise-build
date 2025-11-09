### VLAN Configuration Generator

**File:** Tools/vlan_config_generator.py  
**Purpose:** Auto-generate router sub-interface configs from VLAN definitions.

#### Example Input
vlans = [
    {"id": 10, "name": "USERS", "subnet": "192.168.10.0/26"},
    {"id": 20, "name": "SERVERS", "subnet": "192.168.10.64/26"},
]

#### Example Output
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.192
 description USERS_VLAN
