from typing import Tuple, List, Callable, Dict

import pandas as pd
import plotly.express as px
from panda_puts.types.extras import Strategy, Points
from panda_puts.types.option import OptionPosition, OptionType


def num_format(num):
    return f"<b>${num:.2f}</b>" if num >= 0 else f"<b>(${num * -1:.2f})</b>"


def build_data(strategy: Strategy, points: Points, cmp_fn: Callable[[float], float]) -> Tuple[List[float], List[float]]:
    x, y = points.x_range(), []
    for price in x:
        p = points.check_breakevens_and_round(cmp_fn(price), price, strategy)
        y.append(p * 100)
    return x, y


def bull_call_spread(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    buy_option = [o for o in strategy.options if o.position == OptionPosition.BUY][0]
    sell_option = [o for o in strategy.options if o.position == OptionPosition.SELL][0]
    points = Points(
        max_profits=[(sell_option.strike, round((sell_option.strike + sell_option.premium) - (buy_option.strike + buy_option.premium), 2) * 100)],
        max_losses=[(buy_option.strike, round(sell_option.premium - buy_option.premium, 2) * 100)],
        graph_min=buy_option.strike - (sell_option.strike - buy_option.strike),
        graph_max=sell_option.strike + sell_option.strike - buy_option.strike
    )

    def cmp_fn(price: float) -> float:
        if price <= buy_option.strike:
            return sell_option.premium - buy_option.premium
        elif price > sell_option.strike:
            return (sell_option.strike + sell_option.premium) - (buy_option.strike + buy_option.premium)
        else:
            return (price + sell_option.premium) - (buy_option.strike + buy_option.premium)

    return points, cmp_fn


def bear_put_spread(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    buy_option = [o for o in strategy.options if o.position == OptionPosition.BUY][0]
    sell_option = [o for o in strategy.options if o.position == OptionPosition.SELL][0]
    points = Points(
        max_profits=[(sell_option.strike, ((buy_option.strike + sell_option.premium) - (sell_option.strike + buy_option.premium)) * 100)],
        max_losses=[(buy_option.strike, (sell_option.premium - buy_option.premium) * 100)],
        graph_min=max(sell_option.strike - (buy_option.strike - sell_option.strike), 0),
        graph_max=buy_option.strike + buy_option.strike - sell_option.strike
    )
    
    def cmp_fn(price: float) -> float:
        if price < sell_option.strike:          
            return (buy_option.strike + sell_option.premium) - (sell_option.strike + buy_option.premium)
        elif price >= buy_option.strike:
            return sell_option.premium - buy_option.premium
        else:
            return (sell_option.premium + buy_option.strike) - (price + buy_option.premium)

    return points, cmp_fn


def long_straddle(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    premium_sum = sum([o.premium for o in strategy.options])
    strike = strategy.options[0].strike
    points = Points(
        max_profits=[(0, (strike - 0 - premium_sum) * 100)],
        max_losses=[(strike, premium_sum * -100)],
        graph_min=0.0,
        graph_max=(strategy.market_price * 2.0)
    )

    def cmp_fn(price: float) -> float:
        p = 0 - premium_sum
        if price < strike:
            p += (strike - price)
        elif price > strike:
            p += (price - strike)
        return p

    return points, cmp_fn


def long_strangle(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    premium_sum = sum([o.premium for o in strategy.options])
    call_option = [o for o in strategy.options if o.type == OptionType.CALL][0]
    put_option = [o for o in strategy.options if o.type == OptionType.PUT][0]
    points = Points(
        max_profits=[(0, (put_option.strike - premium_sum) * 100)],
        max_losses=[(strategy.market_price, (0 - premium_sum) * 100)],
        graph_min=0.0,
        graph_max=(strategy.market_price * 2.0)
    )

    def cmp_fn(price: float) -> float:
        if price < put_option.strike:
            return put_option.strike - (price + premium_sum)
        elif price > call_option.strike:
            return price - (call_option.strike + premium_sum)
        else:
            return 0 - premium_sum

    return points, cmp_fn


def butterfly_spread(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    itm_buy = strategy.options[0]
    atm_sell = strategy.options[1]
    otm_buy = strategy.options[-1]
    points = Points(
        max_profits=[(strategy.market_price, (((atm_sell.strike * 2) + (atm_sell.premium * 2)) - (itm_buy.strike + itm_buy.premium + otm_buy.premium + strategy.market_price)) * 100)],
        max_losses=[
            (itm_buy.strike, ((atm_sell.premium * 2) - (itm_buy.premium + otm_buy.premium)) * 100),
            (otm_buy.strike, (((atm_sell.strike * 2) + (atm_sell.premium * 2)) - (itm_buy.strike + itm_buy.premium + otm_buy.strike + otm_buy.premium)) * 100)
        ],
        graph_min=itm_buy.strike - (otm_buy.strike - itm_buy.strike),
        graph_max=otm_buy.strike + (otm_buy.strike - itm_buy.strike)
    )

    def cmp_fn(price: float) -> float:
        if price <= itm_buy.strike:
            return (atm_sell.premium * 2) - (itm_buy.premium + otm_buy.premium)
        elif itm_buy.strike < price <= atm_sell.strike:
            return (price + (atm_sell.premium * 2)) - (itm_buy.strike + itm_buy.premium + otm_buy.premium)
        elif atm_sell.strike < price <= otm_buy.strike:
            return ((atm_sell.strike * 2) + (atm_sell.premium * 2)) - (itm_buy.strike + itm_buy.premium + otm_buy.premium + price)
        else:
            return ((atm_sell.strike * 2) + (atm_sell.premium * 2)) - (itm_buy.strike + itm_buy.premium + otm_buy.strike + otm_buy.premium)

    return points, cmp_fn


def iron_condor(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    buy_premiums = sum([o.premium for o in strategy.options if o.position == OptionPosition.BUY])
    sell_premiums = sum([o.premium for o in strategy.options if o.position == OptionPosition.SELL])
    buy_call_option = [o for o in strategy.options if o.position == OptionPosition.BUY and o.type == OptionType.CALL][0]
    sell_call_option = [o for o in strategy.options if o.position == OptionPosition.SELL and o.type == OptionType.CALL][0]
    buy_put_option = [o for o in strategy.options if o.position == OptionPosition.BUY and o.type == OptionType.PUT][0]
    sell_put_option = [o for o in strategy.options if o.position == OptionPosition.SELL and o.type == OptionType.PUT][0]
    points = Points(
        max_profits=[(strategy.market_price, (sell_premiums - buy_premiums) * 100)],
        max_losses=[
            (buy_put_option.strike, ((buy_put_option.strike + sell_premiums) - (sell_put_option.strike + buy_premiums)) * 100),
            (buy_call_option.strike, ((sell_call_option.strike + sell_premiums) - (buy_call_option.strike + buy_premiums)) * 100)
        ],
        graph_min=(buy_put_option.strike - (strategy.market_price - buy_put_option.strike)),
        graph_max=(buy_call_option.strike + (buy_call_option.strike - strategy.market_price))
    )

    def cmp_fn(price: float) -> float:
        if price < buy_put_option.strike:
            return (buy_put_option.strike + sell_premiums) - (sell_put_option.strike + buy_premiums)
        elif buy_put_option.strike <= price < sell_put_option.strike:
            return (price + sell_premiums) - (sell_put_option.strike + buy_premiums)
        elif sell_put_option.strike <= price <= sell_call_option.strike:
            return sell_premiums - buy_premiums
        elif sell_call_option.strike < price <= buy_call_option.strike:
            return (sell_call_option.strike + sell_premiums) - (price + buy_premiums)
        else:
            return (sell_call_option.strike + sell_premiums) - (buy_call_option.strike + buy_premiums)

    return points, cmp_fn


def iron_butterfly(strategy: Strategy) -> Tuple[Points, Callable[[float], float]]:
    # The Iron Butterfly's calculations are the same as Iron Condor
    return iron_condor(strategy)


STRATEGIES: Dict[str, Callable[[Strategy], Tuple[Points, Callable[[float], float]]]] = {
    "Bull Call Spread": bull_call_spread,
    "Bear Put Spread": bear_put_spread,
    "Long Straddle": long_straddle,
    "Long Strangle": long_strangle,
    "Butterfly Spread": butterfly_spread,
    "Iron Condor": iron_condor,
    "Iron Butterfly": iron_butterfly
}


def plotly_graph(strategy: Strategy):
    if strategy.name not in STRATEGIES:
        names = ", ".join(STRATEGIES.keys())
        raise Exception(f"{strategy.name} is not a valid strategy!\nChoose from [{names}]")
    points, cmp_fn = STRATEGIES[strategy.name](strategy)
    x, y = build_data(strategy, points, cmp_fn)
    df = pd.DataFrame({"Stock Price ($)": x, "Profit/Loss ($)": y, "Bear Call": y})
    fig = px.line(df, x="Stock Price ($)", y="Profit/Loss ($)", title=f"{strategy.name} on {strategy.ticker} at ${strategy.market_price:.2f}")
    for profit in points.max_profits:
        fig.add_annotation(x=round(profit[0], 2), y=round(profit[1], 2), text=num_format(round(profit[1], 2)))
    for loss in points.max_losses:
        fig.add_annotation(x=round(loss[0], 2), y=round(loss[1], 2), text=num_format(round(loss[1], 2)))
    for be in [points.break_even.low, points.break_even.high]:
        if be:
            fig.add_annotation(
                x=round(be[0], 2), y=round(be[1], 2), text=num_format(round(be[0], 2)), hovertext="Breakeven point"
            )
    fig.add_vline(strategy.market_price)
    fig.show()
