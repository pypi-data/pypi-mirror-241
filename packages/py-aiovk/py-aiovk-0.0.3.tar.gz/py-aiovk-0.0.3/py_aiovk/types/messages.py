from pydantic import BaseModel


class Message(BaseModel):
    id: int
    date: int
    peer_id: int
