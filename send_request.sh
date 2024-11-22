#!/bin/bash

# Usage: ./send_request.sh <port>

# Check if port is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <port>"
  exit 1
fi

PORT=$1

# Send the POST request
curl -X POST http://localhost:$PORT/receive \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello Paxos!"}'
