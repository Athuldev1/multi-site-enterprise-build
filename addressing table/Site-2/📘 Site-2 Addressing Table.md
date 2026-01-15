# Site-2 Addressing and Routing Documentation

## 1. Site-2 Overview

Site-2 is a branch site connected to Site-1 via a routed WAN link.  
The site uses VLAN-based segmentation with dual-stack (IPv4 + IPv6) addressing.

---

## 2. VLAN and Subnet Summary

### VLAN Mapping

| VLAN ID | Name          | IPv4 Subnet            | IPv6 Prefix            |
|-------|---------------|------------------------|------------------------|
| 30    | USERS_SITE2   | 192.168.20.0/26        | 2001:db8:30::/64       |
| 40    | SERVER_SITE2  | 192.168.20.64/26       | 2001:db8:40::/64       |

---

## 3. Site-2 Addressing Table

### Router R2 Interfaces

| Device | Interface  | VLAN | IPv4 Address        | IPv6 Address              | Description |
|------|------------|------|---------------------|---------------------------|-------------|
| R2   | G0/0.30    | 30   | 192.168.20.1/26     | 2001:db8:30::1/64         | Users gateway |
| R2   | G0/0.40    | 40   | 192.168.20.65/26    | 2001:db8:40::1/64         | Servers gateway |
| R2   | G0/1       | WAN  | 10.0.0.2/30         | 2001:db8:100::2/64        | Link to Site-1 |

---

## 4. WAN Link Summary

| Link        | IPv4 Subnet   | IPv6 Subnet           |
|------------|---------------|-----------------------|
| R1 ↔ R2    | 10.0.0.0/30   | 2001:db8:100::/64     |

---

## 5. Static Routing Configuration (R2)

### IPv4 Static Routes

| Destination Network   | Next Hop  | Purpose |
|----------------------|-----------|---------|
| 192.168.10.0/26      | 10.0.0.1  | Site-1 Users |
| 192.168.10.64/26     | 10.0.0.1  | Site-1 Servers |

### IPv6 Static Routes

| Destination Prefix       | Next Hop              | Purpose |
|-------------------------|-----------------------|---------|
| 2001:db8:10::/64        | 2001:db8:100::1       | Site-1 Users |
| 2001:db8:20::/64        | 2001:db8:100::1       | Site-1 Servers |

---

## 6. Routing Decision Table (R2)

This table represents how Router R2 forwards traffic based on destination.

### IPv4 Routing Decisions

| Destination Network     | Route Type | Next Hop  | Outgoing Interface |
|------------------------|------------|-----------|--------------------|
| 192.168.20.0/26        | Connected  | —         | G0/0.30 |
| 192.168.20.64/26       | Connected  | —         | G0/0.40 |
| 192.168.10.0/26        | Static     | 10.0.0.1 | G0/1 |
| 192.168.10.64/26       | Static     | 10.0.0.1 | G0/1 |

### IPv6 Routing Decisions

| Destination Prefix       | Route Type | Next Hop              | Outgoing Interface |
|-------------------------|------------|-----------------------|--------------------|
| 2001:db8:30::/64        | Connected  | —                     | G0/0.30 |
| 2001:db8:40::/64        | Connected  | —                     | G0/0.40 |
| 2001:db8:10::/64        | Static     | 2001:db8:100::1       | G0/1 |
| 2001:db8:20::/64        | Static     | 2001:db8:100::1       | G0/1 |

---

## 7. Verification Commands

```bash
show ip route
show ipv6 route
ping <remote IPv4 address>
ping ipv6 <remote IPv6 address>
