"""In-memory application state for prototyping.

This module keeps the prototype lightweight while mimicking persistence and
session coordination. For production, replace these stores with database and
message queue integrations.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .schemas import Memory, Session, SessionStatus


@dataclass
class AppState:
    """Container for prototyping stores and orchestration helpers."""

    memories: Dict[str, Memory] = field(default_factory=dict)
    sessions: Dict[str, Session] = field(default_factory=dict)
    session_memory_map: Dict[str, List[str]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def add_memory(self, memory: Memory) -> None:
        self.memories[memory.id] = memory

    def link_memory_to_session(self, session_id: str, memory_id: str) -> None:
        self.session_memory_map[session_id].append(memory_id)

    def get_session_memories(self, session_id: str) -> List[Memory]:
        ids = self.session_memory_map.get(session_id, [])
        return [self.memories[m_id] for m_id in ids if m_id in self.memories]

    def add_session(self, session: Session, memory_ids: List[str]) -> None:
        self.sessions[session.id] = session
        for m_id in memory_ids:
            if m_id in self.memories:
                self.link_memory_to_session(session.id, m_id)

    def update_session_status(self, session_id: str, status: SessionStatus) -> Optional[Session]:
        session = self.sessions.get(session_id)
        if session:
            self.sessions[session_id] = session.copy(update={"status": status})
            return self.sessions[session_id]
        return None


app_state = AppState()
"""Singleton-like state instance for the prototype."""
