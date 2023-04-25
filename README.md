# Coin-Conjecture

Predict BitCoin prices, how original :)

ML Engineering practice

Target: [USD Bitcoin Price](https://api.coindesk.com/v1/bpi/currentprice.json)

### TO DO

* Data Sources
  * RSS Feeds - [RSS Feeds](https://www.repeatsoftware.com/Help/RSSFeedList.htm) + [feedparser](https://pypi.org/project/feedparser/)
    * [CBN News](https://www1.cbn.com/rss-cbn-articles-cbnnews.xml)
    * [CBN Finances](https://www1.cbn.com/rss-cbn-articles-finances.xml)
    * [WSJ Market](https://feeds.a.dj.com/rss/RSSMarketsMain.xml)
    * [WSJ Business](https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml)
    * [MarketWatch](http://feeds.marketwatch.com/marketwatch/topstories/)
  * [Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#:~:text=The%20Twitter%20API%20v2%20represents,free%20access%20to%20the%20API.)
* Data Colection
  * AWS EventBridge + AWS Lambda functions + some kind of AWS database/s
* Model/s
  * Time series
  * Predict trends
  * Predict volatility, 
  * Create datasets based on distance from the present
  * Vola
* API 
  * AWS API Gateway + AWS Lambda with embedded model/s
  * API Keys
* Automated Deployment
* Automated Infrastructure
* Automated Monitoring
  * Model performance
  * Data collection processes
