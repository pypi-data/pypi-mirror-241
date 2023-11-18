from enum import Enum


class ComitteeType(str, Enum):
    EXTRAORDINARY = "EXTRAORDINARY"
    INVESTIGATIVE = "INVESTIGATIVE"
    STANDING = "STANDING"

    def __str__(self) -> str:
        return str(self.value)
