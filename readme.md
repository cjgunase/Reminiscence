# Reminiscence Therapy App — Design Plan

## Overview
This project is an AI-powered reminiscence therapy application designed to support memory recall, emotional well-being, and engagement for older adults and individuals with memory-related conditions.

Users and families upload personal media (photos, audio, stories), which the AI converts into guided conversations, narrated memory stories, and interactive reminiscence sessions.

---

## Goals
- Improve mood and emotional engagement
- Support memory recall and identity reinforcement
- Assist caregivers in creating meaningful interactions
- Enable AI-assisted, structured reminiscence therapy

---

## User Roles

### Patient / Resident
- Consumes content
- Interacts through voice or simple UI
- No setup responsibility

### Family / Caregiver
- Uploads and edits memories
- Approves AI-generated content
- Reviews summaries

### Clinician (Optional)
- Views session metrics
- Sets therapy mode or difficulty
- Reads engagement data

---

## Core Features

### Memory Input
- Upload photos
- Add text stories
- Record voice notes
- Tag people, places, and dates

### AI Capabilities
- Generate conversation prompts
- Create narrated memory stories
- Provide guided sessions
- Adapt prompts based on emotional signals

### Playback Modes
- Interactive session mode
- Passive audio playback mode

---

## UX Design Principles

### Cognitive Simplicity
- Minimal UI
- Large readable text
- Audio-first option

### Emotional Safety
- Warm tone
- No contradictions
- Emotion-sensitive questioning
- Easy skip and pause

### Accessibility
- Adjustable narration speed
- Visual contrast control
- Voice navigation (future)

---

## System Flow

### Setup (Family)
Upload media → Add metadata → Review AI summaries → Approve

### Therapy Session
Session start → Emotional check-in → Memory presentation → Prompts →
Reflection → Gentle closure

---

## AI Design

### Memory Representation
Each memory is stored as structured data:
- People
- Places
- Dates
- Emotional tags
- Media links
- Confidence score

### Prompt Strategy
- Sensory prompts
- Emotional prompts
- Identity-based prompts
- Reflective prompts
- Closure prompts

### Behavior Rules
- Do not correct memories
- Do not invent facts
- Confirm uncertainty
- Always validate emotion

---

## Technical Architecture

### Frontend
- Next.js
- Media upload & gallery
- Session player
- Accessibility controls

### Backend
- Memory database
- LLM service
- TTS engine
- Session state manager
- Safety filter layer

---

## Safety & Ethics

### Memory Safety
- No hallucinated life events
- Confidence flagging
- Editable content

### Emotional Safety
- Distress detection
- Topic switching
- Emotional closure routines

### Privacy
- Encrypted storage
- Export and deletion tools
- Consent management

---

## Evaluation Plan

### Clinical Metrics
- Engagement
- Mood improvement
- Recall frequency

### UX Metrics
- Session completion
- User feedback

### AI Metrics
- Prompt quality
- Emotional response shifts

---

## Roadmap

### MVP
- Upload flow
- Gallery
- Prompt generator
- Basic TTS

### Phase 2
- Emotion-aware AI
- Session engine
- Voice interface

### Phase 3
- Analytics
- Clinician dashboard
- Family co-authoring

---

## References
- LLM-assisted reminiscence therapy research
- “Elizabeth” chatbot studies
- Dementia care guidelines

---

## Prototype Framework

The repository now includes a lightweight FastAPI prototype that mirrors the
design plan. It focuses on safe prompt generation, memory upload, and session
creation to validate the AI-assisted reminiscence flow.

### Layout

- `backend/app/main.py`: FastAPI entrypoint with routers for memories and sessions.
- `backend/app/routes/`: Memory CRUD and session orchestration endpoints.
- `backend/app/services/`: Prompt generation heuristics and session state tools.
- `backend/app/state.py`: In-memory stores to mimic persistence during prototyping.
- `tests/`: Pytest suite covering prompt generation and session assembly.

### Quickstart

1. Install dependencies: `pip install -r backend/requirements.txt`
2. Run the API: `uvicorn backend.app.main:app --reload --port 8000`
3. Explore interactive docs at `http://localhost:8000/docs`
4. Execute tests: `pytest`

### Example Workflow

```bash
curl -X POST http://localhost:8000/memories/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Family picnic", "people": ["Alex"], "places": ["Central Park"], "emotional_tags": ["nostalgia"]}'

curl -X POST http://localhost:8000/sessions/ \
  -H "Content-Type: application/json" \
  -d '{"memory_ids": ["<memory-id-from-response>"], "mode": "guided"}'
```

Use the `/sessions/preview` endpoint to review AI prompts before starting a
session, reflecting the safety and approval steps from the design plan.
