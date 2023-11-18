from enum import Enum


class VotingKind(str, Enum):
    ELECTRONIC = "ELECTRONIC"
    ON_LIST = "ON_LIST"
    TRADITIONAL = "TRADITIONAL"

    def __str__(self) -> str:
        return str(self.value)
