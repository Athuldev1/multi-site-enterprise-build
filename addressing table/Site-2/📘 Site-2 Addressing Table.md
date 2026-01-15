📘 Site-2 Addressing Table

Site-2 VLANs

VLAN 30 → Users
VLAN 40 → Servers


IPv4

VLAN 30 → 192.168.20.0/26
VLAN 40 → 192.168.20.64/26


IPv6

VLAN 30 → 2001:db8:30::/64
VLAN 40 → 2001:db8:40::/64


🔹 Addressing Table – Site-2

Device	Interface	VLAN	IPv4 Address	 IPv6 Address	              Purpose
R2	G0/0.30	        30	192.168.20.1/26	 2001:db8:30::1/64	     Users gateway
R2	G0/0.40	        40	192.168.20.65/26 2001:db8:40::1/64    Servers gateway
R2	G0/1	        WAN	10.0.0.2/30	 2001:db8:100::2/64	     Link to Site-1



🔹 WAN Link Summary

Link	IPv4 Subnet	IPv6 Subnet
R1 ↔ R2	10.0.0.0/30	2001:db8:100::/64


2️⃣ Site-2 Routing Table (Configured Routes)


📍 Static Routes on R2

Destination Network	Protocol	Next Hop	      Reason
192.168.10.0/26	   Static	      10.0.0.1	    Reach Site-1 Users
192.168.10.64/26	Static	      10.0.0.1	    Reach Site-1 Servers
2001:db8:10::/64	Static	    2001:db8:100::1	    Reach Site-1 Users (IPv6)
2001:db8:20::/64	Static	     2001:db8:100::1	    Reach Site-1 Servers (IPv6)

Routing Decision Table
<img width="844" height="476" alt="image" src="https://github.com/user-attachments/assets/d72ef9eb-5d10-4bf5-a201-a7adb43f6f43" />

