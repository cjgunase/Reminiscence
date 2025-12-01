"""Prompt generation heuristics aligned with reminiscence therapy principles."""

from __future__ import annotations

from typing import Iterable, List

from ..schemas import EmotionTag, Memory, Prompt


def _format_list(items: Iterable[str], prefix: str) -> str:
    values = list(items)
    return f" {prefix} " + ", ".join(values) if values else ""


def build_prompts(memory: Memory) -> List[Prompt]:
    sensory_prompt = (
        "What sounds or smells do you remember from this moment?"
        f"{_format_list(memory.places, 'at')}"
    )
    emotional_prompt = (
        "How did this make you feel, and who were you with?"
        f"{_format_list(memory.people, 'with')}"
    )
    identity_prompt = (
        "What does this memory say about who you were or wanted to be?"
    )

    prompts = [
        Prompt(memory_id=memory.id, type="sensory", text=sensory_prompt),
        Prompt(memory_id=memory.id, type="emotional", text=emotional_prompt),
        Prompt(memory_id=memory.id, type="identity", text=identity_prompt),
    ]

    if EmotionTag.NOSTALGIA in memory.emotional_tags:
        prompts.append(
            Prompt(
                memory_id=memory.id,
                type="nostalgia",
                text="Does revisiting this bring back other related moments?",
            )
        )

    return prompts


__all__ = ["build_prompts"]
