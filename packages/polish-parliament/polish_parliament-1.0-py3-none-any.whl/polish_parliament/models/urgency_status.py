from enum import Enum


class UrgencyStatus(str, Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"
    URGENT_WITHDRAWN = "URGENT_WITHDRAWN"

    def __str__(self) -> str:
        return str(self.value)
