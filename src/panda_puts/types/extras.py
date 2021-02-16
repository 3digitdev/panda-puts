from dataclasses import dataclass
from typing import List, Tuple, Optional

from panda_puts.types.option import OptionContract

Coords = Tuple[float, float]


def float_range(start, stop, step):
    start = round(start, 2)
    stop = round(stop, 2)
    while start < stop:
        yield round(start, 2)
        start += step


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


@dataclass
class Breakeven:
    high: Optional[Coords] = None
    low: Optional[Coords] = None


@dataclass
class Points:
    max_profits: List[Coords]
    max_losses: List[Coords]
    graph_min: float
    graph_max: float
    break_even: Breakeven = Breakeven()

    def x_range(self, step: float = 0.01):
        return list(float_range(self.graph_min, self.graph_max, step))

    def check_breakevens_and_round(
        self, price: float, market: float, strat: Strategy
    ) -> float:
        price = round(price, 2)
        if price == 0:
            if market < strat.market_price:
                self.break_even.low = (market, price)
            else:
                self.break_even.high = (market, price)
        return price

    def __str__(self):
        return f"""
Breakeven-: {self.break_even.low}
Breakeven+: {self.break_even.high}
Profits:    {self.max_profits}
Losses:     {self.max_losses}
"""
