"""Session orchestration helpers."""

from __future__ import annotations

from typing import List

from ..schemas import Memory, Prompt, Session, SessionStatus
from ..state import app_state
from .prompt_service import build_prompts


def prepare_session(memory_ids: List[str], mode: str) -> Session:
    memories: List[Memory] = [
        app_state.memories[m_id] for m_id in memory_ids if m_id in app_state.memories
    ]
    prompts: List[Prompt] = [p for m in memories for p in build_prompts(m)]
    session = Session(status=SessionStatus.READY, prompts=prompts)
    app_state.add_session(session, memory_ids)
    return session


def start_session(session_id: str) -> Session:
    session = app_state.sessions[session_id]
    updated = app_state.update_session_status(session_id, SessionStatus.RUNNING)
    return updated or session


def complete_session(session_id: str) -> Session:
    session = app_state.sessions[session_id]
    updated = app_state.update_session_status(session_id, SessionStatus.COMPLETED)
    return updated or session


__all__ = ["prepare_session", "start_session", "complete_session"]
