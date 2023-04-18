# Coin-Conjecture

Predict BitCoin prices, how original :)

ML Engineering practice

Target: [USD Bitcoin Price](https://api.coindesk.com/v1/bpi/currentprice.json)

### TO DO

* Decide on data sources
  * RSS Feeds - [RSS Feeds](https://www.repeatsoftware.com/Help/RSSFeedList.htm) + [feedparser](https://pypi.org/project/feedparser/)
    * [CBN News](https://www1.cbn.com/rss-cbn-articles-cbnnews.xml)
    * [CBN Finances](https://www1.cbn.com/rss-cbn-articles-finances.xml)
    * [WSJ Market](https://feeds.a.dj.com/rss/RSSMarketsMain.xml)
    * [WSJ Business](https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml)
    * [MarketWatch](http://feeds.marketwatch.com/marketwatch/topstories/)
  * [Rapid API](https://rapidapi.com/hub)
    * [Alpha Vantage](https://rapidapi.com/alphavantage/api/alpha-vantage/)
    * [Bloomberg](https://rapidapi.com/apidojo/api/bloomberg-market-and-financial-news/)
* Develop processes for continuous data collection - AWS EventBridge + AWS Lambda functions + some kind of AWS database/s
* Develop various models using time series data
* Create simple API getting BitCoin price predictions - AWS API Gateway + AWS Lambda with embedded model/s
* Authentication systems
  * API Keys
  * OAuth
* Create process for simple deployments
* Create process for continually monitoring model performance - ask it to predict and measure the results the next day, week, month, etc.


### _Some sloppy ideas 4 u:_
When I was looking at this problem earlier my solution was to train it to recognize chart patterns to find buying opportunities, so maybe something like that would work here too:
* Scan on a consistent interval over different time periods (e.g. every minute scan the datasets for the past 1/10/60 minutes, and every day scan the sets for the past 1/7/30 days)
* Generate a graph image of price over time for each of these periods, and have the AI classify them geometrically instead of using raw data. (Cuts out noise this way, and this is also how many people trade so your model will be "trading" with the market. Matt B would know more about the trading strategy aspect.) Have it look for different chart patterns like turns, bull/bear trends, flat, breakout, etc.
* For each period, pass the sequence of these patterns --maybe as a sequence of (pattern, price change) or (class, dy) tuples?-- as the input argument through another model to get a distibution of up/down/flat/uncertain confidences for the future movement. 
* If you're feeling fancy, you could also introduce things like trade volume, areas of support and resistance, press releases, etc. through another model or through algorithmic analysis to create a "volatility factor" to modify these confidence scores.
* Use the confidence sets to create a probability cone of future price for each period analyzed, then average the time-weighted confidence ranges for each of the periods for each future minute interval to get an overall probability distribution for movement up/down/flat at each future minute, which you could colorize and map directly over the trading chart. It would be like predicting a channel for the price to follow.
* The loss & gradient descent calcs for this would be a nightmare though lmao so I'd only try this if I knew of a library that could handle it automatically. Basically it would have to track whether the price action followed the predicted direction and rate of change, and how closely, for each of the periods analyzed and overall.

You could still feed it raw data but you'd probably have to train like hell haha. Either way I think an up/down/flat/uncertain probability distibution is a more useful target than trying to predict the specific price, especially if you're trying to predict behavior over larger time ranges. The market's so chaotic, there are so many possible factors that the model will never see or be able to know just from the data, and outlier events might accidentally derail your training and set you back. Like imagine you're training on live data, it has it almost figured out, it's predicting so-and-so, then Elon tweets "buy Bitcoin" and gives your AI an existential crisis. If the model predicts "kinda up" and the market goes "way up" instead, it might be able to account for that better. 

Just my $0.02. That's how I planned to approach it before I decided to try the continuous-integration route. I thought it would be simpler to let the model figure out how the market works on its own and just punish it whenever it loses me money lol. I'll tailor that toward Bitcoin too so we can do a head-to-head comparison.
