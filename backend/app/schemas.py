"""Pydantic schemas aligned with the design plan."""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


def generate_id() -> str:
    return uuid.uuid4().hex


class EmotionTag(str, Enum):
    JOY = "joy"
    CALM = "calm"
    NOSTALGIA = "nostalgia"
    SADNESS = "sadness"
    EXCITEMENT = "excitement"


class MemoryBase(BaseModel):
    title: str = Field(..., description="Short name for the memory")
    description: Optional[str] = Field(None, description="Narrative or caption")
    people: List[str] = Field(default_factory=list)
    places: List[str] = Field(default_factory=list)
    dates: List[str] = Field(default_factory=list)
    emotional_tags: List[EmotionTag] = Field(default_factory=list)
    media_urls: List[HttpUrl] = Field(default_factory=list)


class Memory(MemoryBase):
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    confidence: float = Field(
        0.7,
        ge=0,
        le=1,
        description="Confidence in AI-generated narrative enrichment",
    )


class Prompt(BaseModel):
    id: str = Field(default_factory=generate_id)
    memory_id: str
    type: str
    text: str


class SessionStatus(str, Enum):
    DRAFT = "draft"
    READY = "ready"
    RUNNING = "running"
    COMPLETED = "completed"


class Session(BaseModel):
    id: str = Field(default_factory=generate_id)
    status: SessionStatus = SessionStatus.DRAFT
    prompts: List[Prompt] = Field(default_factory=list)


class SessionCreateRequest(BaseModel):
    memory_ids: List[str]
    mode: str = Field(
        "guided",
        description="Session mode such as guided, passive playback, or analytics",
    )


class SessionResponse(Session):
    memory_ids: List[str] = Field(default_factory=list)
    mode: str


class PromptPreviewResponse(BaseModel):
    prompts: List[Prompt]

