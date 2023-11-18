from enum import Enum


class ReferralType(str, Enum):
    ADDITIONAL = "ADDITIONAL"
    ADDITIONAL_OPINION = "ADDITIONAL_OPINION"
    NORMAL = "NORMAL"
    OPINION = "OPINION"
    WITHDRAWAL = "WITHDRAWAL"

    def __str__(self) -> str:
        return str(self.value)
