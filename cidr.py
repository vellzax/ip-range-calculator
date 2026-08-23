import ipaddress
def inspect(cidr): return str(ipaddress.ip_network(cidr))