from dotenv import load_dotenv

from livekit.agents import Agent

# Local Imports
from data import UserInfo
from prompts import ADULT_PROMPT, UNDER18_PROMPT

load_dotenv('.env.local')

class AdultAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=ADULT_PROMPT
        )

    async def on_enter(self) -> None:
        user_info: UserInfo = self.session.userdata
        await self.session.generate_reply(instructions=f"Greet the {user_info.name} personally and offer your assistance.")

class JuniorAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=UNDER18_PROMPT
        )

    async def on_enter(self) -> None:
        user_info: UserInfo = self.session.userdata
        await self.session.generate_reply(instructions=f"Greet the {user_info.name} personally and offer your assistance.")
