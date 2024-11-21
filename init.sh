#!/bin/bash

# Create the project directory
mkdir -p app


# Create requirements.txt
cat <<EOL > app/requirements.txt
fastapi
uvicorn[standard]
httpx
pydantic
EOL

# Create config.py
cat <<EOL > app/config.py
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
EOL

# Create messages.py
cat <<EOL > app/messages.py
from typing import Optional, Tuple, Any
from pydantic import BaseModel

class Prepare(BaseModel):
    sender: Tuple[str, int]
    instance_id: int
    proposal_number: Tuple[int, int]  # (proposal_number, server_id)

class Promise(BaseModel):
    sender: Tuple[str, int]
    instance_id: int
    proposal_number: Tuple[int, int]
    accepted_number: Optional[Tuple[int, int]] = None
    accepted_value: Optional[Any] = None

class AcceptRequest(BaseModel):
    sender: Tuple[str, int]
    instance_id: int
    proposal_number: Tuple[int, int]
    value: Any

class Accepted(BaseModel):
    sender: Tuple[str, int]
    instance_id: int
    proposal_number: Tuple[int, int]
    value: Any

class Learn(BaseModel):
    sender: Tuple[str, int]
    instance_id: int
    value: Any

class Propose(BaseModel):
    command: str

class ClientRequest(BaseModel):
    command: str

class ClientResponse(BaseModel):
    status: str  # 'OK' or 'ERROR'
    message: str  # Additional information
EOL

# Create main.py
cat <<'EOL' > app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from messages import *
from config import SERVER_ADDRESS, SERVER_ADDRESSES
import asyncio
import httpx

app = FastAPI()

class PaxosServer:
    def __init__(self):
        self.server_address = SERVER_ADDRESS
        self.server_addresses = SERVER_ADDRESSES
        self.instances = {}  # instance_id -> state
        self.learned_values = {}  # instance_id -> value
        self.proposal_number = 0  # Local proposal number
        self.instance_id = 1  # Start from instance 1
        self.lock = asyncio.Lock()
        self.server_id = self.server_address[1]  # Use port number as s
