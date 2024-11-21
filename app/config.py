import os

def parse_addresses(env_var):
    addresses = []
    addr_str = os.environ.get(env_var)
    if addr_str:
        for addr in addr_str.split(','):
            host, port = addr.strip().split(':')
            addresses.append((host, int(port)))
    return addresses

# This server's address
SERVER_ADDRESS = (os.environ.get('HOST', '0.0.0.0'), int(os.environ.get('PORT', '8000')))

# List of all server addresses
SERVER_ADDRESSES = parse_addresses('SERVER_ADDRESSES')
