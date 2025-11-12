from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str | None
    age: int | None