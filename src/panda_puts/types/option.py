from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple


class OptionType(Enum):
    CALL = "Call"
    PUT = "Put"


class OptionPosition(Enum):
    BUY = "Buy"
    SELL = "Sell"


@dataclass
class OptionContract:
    type: OptionType
    position: OptionPosition
    strike: float
    premium: float

    def __str__(self):
        return (
            f"{self.position} {self.type} Option @ ${self.strike} for ${self.premium}"
        )

    @classmethod
    def from_bullets(cls, result: List[Tuple[str, str]]):
        return cls(
            type=OptionType[result[0][1]],
            position=OptionPosition[result[1][1]],
            strike=result[2][1],
            premium=result[3][1],
        )

    @classmethod
    def from_json(cls, data):
        obj = cls(**data)
        obj.type = {v.value: v for v in list(OptionType)}[data["type"]]
        obj.position = {v.value: v for v in list(OptionPosition)}[data["position"]]
        return obj

    def to_json(self):
        return {
            "type": self.type.value,
            "position": self.position.value,
            "strike": self.strike,
            "premium": self.premium,
        }
