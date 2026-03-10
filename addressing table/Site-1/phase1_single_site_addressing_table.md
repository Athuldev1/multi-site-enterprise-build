# Site-1 Addressing Documentation

## 1. Assigned IPv6 Prefixes

| VLAN | Purpose           | IPv6 Prefix           | Gateway Address        |
|-----|-------------------|-----------------------|------------------------|
| 10  | User Devices      | 2001:db8:10::/64      | 2001:db8:10::1         |
| 20  | Server Network    | 2001:db8:20::/64      | 2001:db8:20::1         |
| —   | Router Uplink     | 2001:db8:feed::/64    | 2001:db8:feed::1 (future) |

---

## 2. IPv4 Addressing Table – Site-1

| Device    | Interface     | VLAN    | IP Address     | Subnet Mask     | Gateway       | Description          |
|----------|---------------|---------|----------------|-----------------|---------------|----------------------|
| Router R1 | G0/0.10       | VLAN 10 | 192.168.10.1   | 255.255.255.192 | —             | Users VLAN gateway   |
| Router R1 | G0/0.20       | VLAN 20 | 192.168.10.65  | 255.255.255.192 | —             | Servers VLAN gateway |
| Switch S1 | VLAN 1 (mgmt) | —       | 192.168.10.254 | 255.255.255.192 | 192.168.10.1  | Switch management    |
| PC1       | Fa0/1         | VLAN 10 | 192.168.10.10  | 255.255.255.192 | 192.168.10.1  | User workstation     |
| Server1   | Fa0/3         | VLAN 20 | 192.168.10.70  | 255.255.255.192 | 192.168.10.65 | File server          |

---

## 3. Design Notes

- VLANs are segmented by function (Users and Servers).
- Router-on-a-Stick is used for inter-VLAN routing.
- IPv6 prefixes are assigned per VLAN using /64 boundaries.
- Router uplink IPv6 prefix is reserved for future WAN connectivity.
- This document serves as the baseline for Site-1 before introducing dynamic routing and redundancy.
