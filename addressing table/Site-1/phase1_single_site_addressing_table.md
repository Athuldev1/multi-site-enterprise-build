| Device    | Interface     | VLAN    | IP Address     | Subnet Mask     | Gateway       | Description          |
| --------- | ------------- | ------- | -------------- | --------------- | ------------- | -------------------- |
| Router R1 | G0/0.10       | VLAN 10 | 192.168.10.1   | 255.255.255.192 | –             | Users VLAN gateway   |
| Router R1 | G0/0.20       | VLAN 20 | 192.168.10.65  | 255.255.255.192 | –             | Servers VLAN gateway |
| Switch S1 | VLAN 1 (mgmt) | –       | 192.168.10.254 | 255.255.255.192 | 192.168.10.1  | Management           |
| PC1       | Fa0/1         | VLAN 10 | 192.168.10.10  | 255.255.255.192 | 192.168.10.1  | User workstation     |
| Server1   | Fa0/3         | VLAN 20 | 192.168.10.70  | 255.255.255.192 | 192.168.10.65 | File server          |
