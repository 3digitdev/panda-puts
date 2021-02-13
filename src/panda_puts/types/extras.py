from dataclasses import dataclass
from typing import List

from panda_puts.types.option import OptionContract


@dataclass
class Breakeven:
    high: float
    low: float


@dataclass
class Points:
    break_even: Breakeven
    max_profit: float


@dataclass
class Strategy:
    name: str
    ticker: str
    market_price: float
    expiry: str
    options: List[OptionContract]

    @classmethod
    def from_json(cls, data):
        obj = cls(**data)
        obj.options = [OptionContract.from_json(opt) for opt in data["options"]]

    def to_json(self):
        return {
            "name": self.name,
            "ticker": self.ticker,
            "market_price": self.market_price,
            "expiry": self.expiry,
            "options": [opt.to_json() for opt in self.options],
        }
