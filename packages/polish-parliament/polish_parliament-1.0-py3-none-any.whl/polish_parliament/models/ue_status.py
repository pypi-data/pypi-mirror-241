from enum import Enum


class UEStatus(str, Enum):
    ADAPTATION = "ADAPTATION"
    ENFORCEMENT = "ENFORCEMENT"
    NO = "NO"

    def __str__(self) -> str:
        return str(self.value)
