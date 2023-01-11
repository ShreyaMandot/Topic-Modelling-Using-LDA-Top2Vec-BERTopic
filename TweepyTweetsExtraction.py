# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:12:40 2022

@author: mshre
"""

# import tweepy
import tweepy as tw
import pandas as pd
import re
from textblob import TextBlob


# your Twitter API key and API secret
my_api_key = "IMFgX5BVErwYOoyleSH029T3l"
my_api_secret = "5Dushwi73BZv0h8ibF1EWtrOf0kx7zkwJ7AjWoex6evAvIQIT0"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#search_query = "mirtazapine -filter:retweets"

# get tweets from the API
search_query = ["escitalopram -filter:retweets","mirtazapine -filter:retweets","Celexa -filter:retweets",
                "citalopram -filter:retweets","Lexapro -filter:retweets","escitalopram -filter:retweets", 
                "Pexeva -filter:retweets", "paroxetine -filter:retweets","fluoxetine -filter:retweets",
                "Prozac+Prozac+Weekly -filter:retweets", "Trintellix -filter:retweets",
                "vortioxetine -filter:retweets","Viibryd -filter:retweets", "vilazodone -filter:retweets",
                "Zoloft -filter:retweets", "sertraline -filter:retweets", "Cymbalta -filter:retweets",
                "duloxetine -filter:retweets", "Effexor-filter:retweets", "Effexor+XR -filter:retweets",
                "venlafaxine -filter:retweets", "Fetzima -filter:retweets", "levomilnacipran -filter:retweets",
                "Pristiq Khedezla -filter:retweets", "desvenlafaxine -filter:retweets",
                "Asendin -filter:retweets","amoxapine -filter:retweets", "Elavil -filter:retweets",
                "amitriptyline -filter:retweets","Ludiomil -filter:retweets" "maprotiline -filter:retweets",
                "Norpramin -filter:retweets", "desipramine -filter:retweets", "Pamelor -filter:retweets",
                "nortriptyline -filter:retweets", "Sinequan -filter:retweets", "doxepin -filter:retweets",
                "Surmontil -filter:retweets" , "trimipramine -filter:retweets", "Tofranil -filter:retweets",
                "imipramine -filter:retweets", "Vivactil -filter:retweets", "protriptyline -filter:retweets",
                "Desyrel -filter:retweets", "trazodone -filter:retweets","Serzone -filter:retweets",
                "nefazodone -filter:retweets", "Remeron -filter:retweets", "Wellbutrin -filter:retweets",
                "Wellbutrin+SR -filter:retweets", "Paxil -filter:retweets",
                "Wellbutrin+XL -filter:retweets", "bupropion -filter:retweets", "Emsam -filter:retweets", 
                "selegiline -filter:retweets", "Marplan -filter:retweets", "isocarboxazid -filter:retweets",
                "Nardil -filter:retweets", "phenelzine -filter:retweets", "Parnate -filter:retweets",
                "tranylcypromine -filter:retweets", "Spravato -filter:retweets", "esketamine -filter:retweets",
                "Zulresso -filter:retweets", "brexanolone -filter:retweets"]
                          
                    
tweets_copy = []
for i in range(len(search_query)):
    tweets = tw.Cursor(api.search_tweets,
              q=search_query[i],
              lang="en",tweet_mode='extended'
              ).items(500) 
    for tweet in tweets:
        tweets_copy.append(tweet)
        print("Total Tweets fetched:", len(tweets_copy))


all_tweets_json = []
for tweet in tweets_copy:
      all_tweets_json.append({'user_name': tweet.user.name,
                              'text': tweet.full_text,
                              'user_location': tweet.user.location,
                              'user_verified': tweet.user.verified,
                              'date': tweet.created_at
                              })

df3= pd.DataFrame(all_tweets_json)
df3.to_csv('DatasetVersion1.csv')
#Created DatasetVesrion2 in the same way for another week

#################################################################################


