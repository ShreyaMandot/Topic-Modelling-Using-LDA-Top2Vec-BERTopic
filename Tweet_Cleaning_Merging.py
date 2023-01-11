# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:50:17 2022

@author: mshre
"""
import pandas as pd
import re



Clean_df_Version2= pd.read_csv('DatasetVersion2.csv')
Clean_df_Version2["new_text"] =  Clean_df_Version2["text"]
#Perform cleaning on data
#Removing RT, Punctuation etc
Clean_df_Version2['new_text'] =  Clean_df_Version2['text'].str.replace('[#,@,&,-,_,=,+,!,;,.]', ' ')
#Remove emojis from df
filter_char = lambda c: ord(c) < 256
Clean_df_Version2['new_text'] =  Clean_df_Version2["new_text"].apply(lambda s: ''.join(filter(filter_char, s)))
Clean_df_Version2['new_text'] =  Clean_df_Version2["new_text"].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
Clean_df_Version2 = Clean_df_Version2.iloc[:, [0,2,6]]

#Repeat above steps for Dataset Version1 with df name Clean_df_Version1

Clean_df_Version1= pd.read_csv('DatasetVersion1.csv')
Clean_df_Version1["new_text"] =  Clean_df_Version1["text"]
#Perform cleaning on data
#Removing RT, Punctuation etc
Clean_df_Version1['new_text'] =  Clean_df_Version1['text'].str.replace('[#,@,&,-,_,=,+,!,;,.]', ' ')
#Remove emojis from df
filter_char = lambda c: ord(c) < 256
Clean_df_Version1['new_text'] =  Clean_df_Version1["new_text"].apply(lambda s: ''.join(filter(filter_char, s)))
Clean_df_Version1['new_text'] =  Clean_df_Version1["new_text"].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
Clean_df_Version1 = Clean_df_Version1.iloc[:, [0,2,6]]


frames = [Clean_df_Version1, Clean_df_Version2]
result = pd.concat(frames)
result.to_csv('Clean_Tweets.csv')

