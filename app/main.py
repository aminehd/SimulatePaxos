import random
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config import SERVER_ADDRESS, SERVER_ADDRESSES
import asyncio
import os
import httpx

print("app is up and running")
app = FastAPI()

class PaxosServer:
    def __init__(self):
        self.container_name = os.environ.get("CONTAINER_NAME", "Unknown")

        self.server_address = SERVER_ADDRESS
        self.server_addresses = SERVER_ADDRESSES
        self.instances = {}  # instance_id -> state
        self.learned_values = {}  # instance_id -> value
        self.proposal_number = 0  # Local proposal number
        self.instance_id = 1  # Start from instance 1
        self.lock = asyncio.Lock()
        self.server_id = self.server_address[1]  # Use port number as server ID
        self.partitioned = False

    async def simulate_network_partition(self):
        while True:
            await asyncio.sleep(5)  # Random delay between 5 to 15 seconds
            async with self.lock:
                self.partitioned = not self.partitioned  # Toggle partition state
                if self.partitioned:
                    print(f"Server {self.server_id} is now partitioned.")
                else:
                    print(f"Server {self.server_id} is now connected.")
    #  todo implement handle_prepare and handle_accept methods
# Initialize the PaxosServer
server = PaxosServer()
# Start the network partition simulation
@app.on_event("startup")
async def start_network_partition_simulation():
    asyncio.create_task(server.simulate_network_partition())

# Receiver to handle incoming messages
@app.post("/receive")
async def receive_message(payload: dict):
    """
    Receiver for handling incoming messages.
    Simulates a network partition by rejecting messages when partitioned.
    """
    async with server.lock:
        if server.partitioned:
            print(f"Server {server.container_name} is partitioned. Rejecting message.")
            return {"status": "error", "message": f"{server.container_name} is partitioned and cannot process the request."}

        # Process the message normally (this is a placeholder for real logic)
        print(f"Server {server.container_name} received message: {payload}")
        return {"status": "success", "message": f"{server.container_name}  received message successfully.", "payload": payload}
