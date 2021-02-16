# Panda Puts
_Visualization of common Options Risk Management Strategies_

## Running the Project

- Install dependencies:  `poetry install`
- In `main.py`, either uncomment one of the strategies and edit the values, or make your own using the notes below
- Run the project:  `poetry run viz`

### [Options Strategies](https://www.investopedia.com/trading/options-strategies/)
1. **Bull Call Spread:** The investor buys calls at a specific strike price while also selling the same number of calls at a higher strike price.  Used when the investor is bullish and expects a **moderate** rise in price
2. **Bear Put Spread:** The investor buys put options at a specific strike price and also sells the same number of puts at a lower strike price.  Used when the investor is bearish and expects the asset's price to decline.
3. **Long Straddle:** The investor purchases a call and put option on the same asset with _the same price and expiry_.  Used when the investor knows the asset will move significantly, but not sure which direction it will go.  Maximum loss is the cost of both options contracts combined
4. **Long Strangle:** The investor purchases an OTM call option and an OTM put option on the same asset with the _same expiry_.  Used when the investor believes the price will experience large movement but not sure which direction it will go.
5. **Butterfly Spread:** Combines the **Bull Spread** and **Bear Spread** strategies, using 3 different strike prices.  Example: Purchase 1 ITM call option at a lower strike price, Sell 2 ATM call options and Buy 1 OTM call option.  Used when the investor things the stock will not move much before expiration
6. **Iron Condor:** The investor holds a **Bull Put Spread** and a **Bear Call Spread**.  Used for its percieved high probability of earning a small amount of premium when the stock is experiencing low volatility.
7. **Iron Butterfly:** The investor sells an ATM put and buys an OTM put, while also selling an ATM call and buying an OTM call, all with the _same expiry_.  Used for the income it generates and the higher probability of a small gain with a low volatility stock.