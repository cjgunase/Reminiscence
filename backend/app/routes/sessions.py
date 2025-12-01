"""Session management routes."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ..schemas import (
    PromptPreviewResponse,
    Session,
    SessionCreateRequest,
    SessionResponse,
)
from ..services.session_engine import complete_session, prepare_session, start_session
from ..state import app_state

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("/preview", response_model=PromptPreviewResponse)
def preview_prompts(payload: SessionCreateRequest) -> PromptPreviewResponse:
    preview_session = prepare_session(payload.memory_ids, payload.mode)
    app_state.sessions.pop(preview_session.id, None)
    app_state.session_memory_map.pop(preview_session.id, None)
    return PromptPreviewResponse(prompts=preview_session.prompts)


@router.post("/", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(payload: SessionCreateRequest) -> SessionResponse:
    session = prepare_session(payload.memory_ids, payload.mode)
    return SessionResponse(**session.dict(), memory_ids=payload.memory_ids, mode=payload.mode)


@router.post("/{session_id}/start", response_model=SessionResponse)
def begin_session(session_id: str) -> SessionResponse:
    if session_id not in app_state.sessions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    session = start_session(session_id)
    memory_ids = app_state.session_memory_map.get(session_id, [])
    return SessionResponse(**session.dict(), memory_ids=memory_ids, mode="guided")


@router.post("/{session_id}/complete", response_model=SessionResponse)
def finish_session(session_id: str) -> SessionResponse:
    if session_id not in app_state.sessions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    session = complete_session(session_id)
    memory_ids = app_state.session_memory_map.get(session_id, [])
    return SessionResponse(**session.dict(), memory_ids=memory_ids, mode="guided")

