"""Minimal LiveKit voice agent using Quickdial for STT + TTS.

Run:  QUICKDIAL_API_KEY=... python examples/agent.py dev
"""
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import quickdial, silero


async def entrypoint(ctx: JobContext):
    await ctx.connect()
    session = AgentSession(
        stt=quickdial.STT(language="en"),
        tts=quickdial.TTS(voice="alba"),
        vad=silero.VAD.load(),
        # llm=openai.LLM(model="gpt-4o-mini"),  # add your LLM
    )
    await session.start(agent=Agent(instructions="You are a helpful voice assistant."), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
