from dotenv import load_dotenv

# Livekit imports
from livekit import agents
from livekit.plugins import silero, noise_cancellation
from livekit.plugins.turn_detector.english import EnglishModel
from livekit.agents import Agent, AgentSession, RoomInputOptions, RunContext, function_tool

# Local Imports
from data import UserInfo
from agents import AdultAssistant, JuniorAssistant

load_dotenv('.env.local')


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are an intake agent. Learn the user's name and age."""
        )

    @function_tool()
    async def get_user_name(self, context: RunContext[UserInfo], name: str):
        """Use this tool to get the user's name"""
        context.userdata.name = name
        # return self._handoff_if_done()
    
    @function_tool()
    async def get_user_age(self, context: RunContext[UserInfo], age: int):
        """Use this tool to get the user's age"""
        context.userdata.age = age
        return self._handoff_if_done()
    

    def _handoff_if_done(self):
        # if not self.session.userdata.name and not self.session.userdata.age:
        #     return None
        if self.session.userdata.age > 18:
            return AdultAssistant()
        
        if self.session.userdata.age <= 18:
            return JuniorAssistant()



async def entrypoint(ctx: agents.JobContext):
    session = AgentSession[UserInfo](
        stt="cartesia/ink-whisper",
        tts="cartesia/sonic-3:f31cc6a7-c1e8-4764-980c-60a361443dd1",
        llm="openai/gpt-4.1-mini",
        vad=silero.VAD.load(),
        turn_detection=EnglishModel(),
        userdata=UserInfo(name=None, age=None)
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        )
    )
    
    await session.generate_reply(
        instructions=f"Greet the user and offer your assistance"
    )

if __name__ == '__main__':
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))