from bullet import SlidePrompt, Bullet, ScrollBar
from panda_puts.graphs import plotly_graph

from panda_puts.persistence import list_saved_strategies
from panda_puts.types.extras import Strategy
from panda_puts.types.option import OptionContract, OptionType, OptionPosition


def main():
    print("Let's go")
    # ------------------- #
    """
    Bull Call
        Buy Call @ Lower Strike
        Sell Call @ Higher Strike
    """
    # plotly_graph(Strategy("Bull Call Spread", "SABR", 11.81, "2-19", [
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 12.0, 0.48),
    #     OptionContract(OptionType.CALL, OptionPosition.SELL, 13.0, 0.19),
    # ]))
    # ------------------- #
    """
    Bear Put
        Sell Put @ Lower Strike
        Buy Put @ Higher Strike
    """
    # plotly_graph(Strategy("Bear Put Spread", "SABR", 11.81, "2-19", [
    #     OptionContract(OptionType.PUT, OptionPosition.SELL, 10.0, 0.08),
    #     OptionContract(OptionType.PUT, OptionPosition.BUY, 11.0, 0.24)
    # ]))
    # ------------------- #
    """
    Long Straddle
        Buy Call and Put at the same Strike (around the current market price)
    """
    # plotly_graph(Strategy("Long Straddle", "GME", 52.40, "2-26", [
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 52.00, 9.05),
    #     OptionContract(OptionType.PUT, OptionPosition.BUY, 52.00, 8.75)
    # ]))
    # ------------------- #
    """
    Long Strangle
        Buy an OTM Call (<market)
        Buy an OTM Put  (>market)
    """
    # plotly_graph(Strategy("Long Strangle", "GME", 52.40, "2-26", [
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 55.00, 7.80),
    #     OptionContract(OptionType.PUT, OptionPosition.BUY, 50.00, 6.75)
    # ]))
    # ------------------- #
    """
    Butterfly Spread
        Buy an ITM call  (<market)
        Buy an OTM call  (>market)
        Sell 2 ATM calls (=market)
    """
    # plotly_graph(Strategy("Butterfly Spread", "NOK", 4.00, "3-12", [
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 3.00, 1.05),
    #     OptionContract(OptionType.CALL, OptionPosition.SELL, 4.00, 0.39),
    #     OptionContract(OptionType.CALL, OptionPosition.SELL, 4.00, 0.39),
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 5.00, 0.10),
    # ]))
    # ------------------- #
    """
    Iron Condor
        Create a "Bull Put" Spread
            Sell OTM Put (<market)
            Buy OTM Put at lower strike
        Buy a Bear Call Spread
            Sell OTM Call (>market)
            Buy OTM Call at higher strike
    """
    # plotly_graph(Strategy("Iron Condor", "SABR", 11.81, "3-19", [
    #     # Bull Put
    #     OptionContract(OptionType.PUT, OptionPosition.SELL, 10.00, 0.40),
    #     OptionContract(OptionType.PUT, OptionPosition.BUY, 8.00, 0.10),
    #     # Bear Call
    #     OptionContract(OptionType.CALL, OptionPosition.SELL, 13.00, 0.78),
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 15.00, 0.36)
    # ]))
    # ------------------- #
    """
    Iron Butterfly
        Sell an ATM Put (=market)
        Buy an OTM Put (<market)
        Sell an ATM Call (=market)
        Buy an OTM Call (>market)
    """
    # plotly_graph(Strategy("Iron Butterfly", "SABR", 11.00, "3-19", [
    #     OptionContract(OptionType.PUT, OptionPosition.SELL, 11.00, 0.65),
    #     OptionContract(OptionType.PUT, OptionPosition.BUY, 9.00, 0.13),
    #     OptionContract(OptionType.CALL, OptionPosition.SELL, 11.00, 1.24),
    #     OptionContract(OptionType.CALL, OptionPosition.BUY, 13.00, 0.48)
    # ]))
    # ------------------- #


if __name__ == "__main__":
    main()
