from ipaddress import IPv6Network

def ipv6_subnet_info(subnet_input):
    try:
        network = IPv6Network(subnet_input, strict=False)
    except ValueError as e:
        return f"Invalid IPv6 subnet: {e}"

    info = {}

    info["Network"] = str(network.network_address)
    info["Prefix Length"] = network.prefixlen
    info["Subnet"] = str(network.with_prefixlen)

    # Suggested gateway (usually ::1)
    gateway = network.network_address + 1
    info["Suggested Gateway"] = str(gateway)

    # First and last usable hosts without iterating entire host list
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1  # works for IPv6 too

    info["First Host"] = str(first_host)
    info["Last Host"] = str(last_host)

    # Just show a second host example
    info["Second Host"] = str(first_host + 1)

    # Build output
    return "\n".join(f"{k}: {v}" for k, v in info.items())


# Example usage
if __name__ == "__main__":
    subnet = input("Enter an IPv6 subnet (example: 2001:DB8:10::/64): ")
    print("\n--- IPv6 Subnet Information ---")
    print(ipv6_subnet_info(subnet))
