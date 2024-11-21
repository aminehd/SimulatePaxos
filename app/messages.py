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
