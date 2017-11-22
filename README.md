# ACX-HitBTC-Analysis
A simple bot which searches for all possible arbitrage opportunities between ACX.io and HitBTC.com


This is a script designed to show some inital steps an arbitrage trader might take when searching for profitable opportunities.

Programming software overhead for new exchanges, especially websocket interfaces and orderbook parsing modules, is extremely time-consuming. Because of this it is important to focus our efforts on opportunities which demonstrate profitability.

The first steps worth taking are a simple arbitrage analysis of the ticker data from REST, calculated off the best bids and asks, rather than simulating trades against the orderbooks to derive the true profit.

REST ticker data tends to heavily overstate profit opportunities, and also show opportunity where none exists. However, the one upside is that it will never miss a profitable opportunity. If there is the potential to make a profitable arbitrage trade anywhere in the orderbooks then the simulated ticker trade will yield a positive return (after fees).

Because of this, REST ticker analysis is an ideal first step. We can quickly acertain if no profit exists and move on without wasting further time.


This demonstration script shows that (As of 23/11/2017) there does not exist any profitable opportunities for a trader who wishes to arbitrage between ACX.io and HitBTC.com

To demonstrate this, the script continuously simulates ticker trades against all of the 6 possible arbitrage trips which can be made using both exchanges. The script will print the trip taken and percentage profit made for each of the possible trips.

To check all the trips once simply run the script and then call the function check_trips():
>> check_trips()


This script also features an automatic mode, where it will continuously check for profitable arbitrage trades. If a trade is found the script will add it to a CSV file in the working directory. This allows the trader to let the script run for several days if necessary, to gain a full understanding of the potential profit which may be present.
