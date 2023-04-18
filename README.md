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
