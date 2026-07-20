# Quickdial plugin for LiveKit Agents (Python)

Cheap, fast, real-time **TTS** and **STT** for [LiveKit Agents](https://docs.livekit.io/agents/),
powered by [Quickdial](https://quickdial.ai).

- **TTS** — 23+ voices, 16-bit PCM @ 24 kHz, REST + WebSocket streaming.
- **STT** — accurate transcription (whisper.cpp), WebSocket streaming + batch.

## Install

```bash
pip install livekit-plugins-quickdial
```

## Auth

Create an API key at https://web.quickdial.ai, then:

```bash
export QUICKDIAL_API_KEY=qdl_live_your_key
```

## Usage

```python
from livekit.agents import AgentSession
from livekit.plugins import quickdial, silero

session = AgentSession(
    stt=quickdial.STT(language="en"),
    tts=quickdial.TTS(voice="alba"),
    vad=silero.VAD.load(),   # STT emits a final transcript per utterance
    llm=...,
)
```

Standalone:

```python
tts = quickdial.TTS(voice="jane")
async for ev in tts.synthesize("Hello from Quickdial!"):
    ...  # ev.frame is a 24 kHz PCM audio frame
```

## Configuration

| `TTS(...)` | default | notes |
|---|---|---|
| `voice` | `"alba"` | see `GET /v1/voices` for the full list |
| `params` | `None` | Pocket-TTS knobs (`temperature`, `speed`, …) |
| `base_url` | `https://api.quickdial.ai` | API base |
| `api_key` | `$QUICKDIAL_API_KEY` | Bearer key |

| `STT(...)` | default |
|---|---|
| `language` | `"en"` (en/fr/de/es/it/pt) |
| `base_url` | `https://api.quickdial.ai` |

## License

Apache-2.0
