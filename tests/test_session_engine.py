from backend.app.schemas import EmotionTag, Memory
from backend.app.services.prompt_service import build_prompts
from backend.app.services.session_engine import prepare_session
from backend.app.state import app_state


def test_prompt_generation_includes_emotion_tag():
    memory = Memory(
        title="Family picnic",
        description="A sunny afternoon at the park",
        people=["Alex", "Jamie"],
        places=["Central Park"],
        emotional_tags=[EmotionTag.NOSTALGIA],
    )
    app_state.add_memory(memory)

    prompts = build_prompts(memory)

    assert any(p.type == "nostalgia" for p in prompts)
    assert any("Central Park" in p.text for p in prompts)


def test_prepare_session_collects_prompts():
    memory = Memory(title="Graduation day", description="College ceremony")
    app_state.add_memory(memory)

    session = prepare_session([memory.id], mode="guided")

    assert session.prompts, "Session should include generated prompts"
    assert session.status.value == "ready"
