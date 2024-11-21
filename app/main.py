from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config import SERVER_ADDRESS, SERVER_ADDRESSES
import asyncio
import httpx

app = FastAPI()

class PaxosServer:
    # TODO: Implement the PaxosServer class
    def __init__(self):
        self.server_address = SERVER_ADDRESS
        self.server_addresses = SERVER_ADDRESSES
        self.instances = {}  # instance_id -> state
        self.learned_values = {}  # instance_id -> value
        self.proposal_number = 0  # Local proposal number
        self.instance_id = 1  # Start from instance 1
        self.lock = asyncio.Lock()
        self.server_id = self.server_address[1]  # Use port number as s

# Initialize the PaxosServer
server = PaxosServer()