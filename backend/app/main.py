"""FastAPI entrypoint exposing therapy-focused endpoints."""

from __future__ import annotations

from fastapi import FastAPI

from .routes import memories, sessions

app = FastAPI(
    title="Reminiscence Therapy API",
    description="Prototype API for memory uploads, prompt generation, and session flow",
)

app.include_router(memories.router)
app.include_router(sessions.router)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]
