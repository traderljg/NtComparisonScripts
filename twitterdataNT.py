import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date





query = "(from:$BLK) until:2022-07-11 since:2021-07-11"
tweets = []
limit = 1000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
df = pd.DataFrame(tweets, columns=['Date', 'Tweet Id' , 'Text', 'Username' ])

df['Date'] = pd.to_datetime(df['Date']).dt.date


#df['Date'] = df['Date'].dt.tz_localize(None)

df.to_excel(r'D:\Lucas\N Trust\$BLK.xlsx', index = False)


