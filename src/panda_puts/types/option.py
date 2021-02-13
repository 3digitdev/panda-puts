from dataclasses import dataclass
from enum import Enum


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
