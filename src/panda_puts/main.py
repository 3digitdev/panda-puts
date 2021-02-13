from panda_puts.graphs import show_graph
from panda_puts.types.option import OptionContract, OptionType, OptionPosition
from panda_puts.types.extras import Strategy, Points, Breakeven
from panda_puts.persistence import save_strategy, load_strategy

"""
Line Graph (single line)
---
Y-axis:  Profit (0 in the middle)
X-axis:  Share Price (start at 00
    this can be bounded by some small value outside of each breakeven point
---
Filenames:  {ticker}_{strategy}_{date-str}.[csv|json]
CSV Format:
                Profit,Share_price
                ...,...
                ...,...
"""


def main():
    show_graph()


if __name__ == "__main__":
    main()
