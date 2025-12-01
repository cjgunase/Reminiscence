"""Routes for uploading and retrieving memories."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ..schemas import Memory, MemoryBase
from ..state import app_state

router = APIRouter(prefix="/memories", tags=["memories"])


@router.post("/", response_model=Memory, status_code=status.HTTP_201_CREATED)
def create_memory(payload: MemoryBase) -> Memory:
    memory = Memory(**payload.dict())
    app_state.add_memory(memory)
    return memory


@router.get("/", response_model=list[Memory])
def list_memories() -> list[Memory]:
    return list(app_state.memories.values())


@router.get("/{memory_id}", response_model=Memory)
def get_memory(memory_id: str) -> Memory:
    if memory_id not in app_state.memories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memory not found")
    return app_state.memories[memory_id]

