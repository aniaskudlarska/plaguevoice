import tweepy
import random
import time
import difflib

key = '1Hfjc32WzKIEDcTjXsF6vVvJ1'
secretkey = 'hYjOybN9pv3o3a7LRQo1qTxzF8zaIK4noxQRgE9qtMHsLedqDs'

accesstoken = '1313171961246253059-AhmeYwB1Uw2M5CvcZM9Z9GqDGPxG8z'
accesstokensecret = 'Ok8XKkX27oB6YPnEAecqM10oueu5maNV50c92mWnzK7sl'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(key, secretkey)
auth.set_access_token(accesstoken,accesstokensecret)

#Create API as object
api = tweepy.API(auth)



#Create list of plague lines as strings
file = open("F:\Documents\GitHub\plaguevoice\plaguevoice.txt", "r")
qlist = []
for line in file:
    qlist.append(line)
tweet = api.user_timeline(count = 1)[0]
toprint = random.choice(qlist)
while toprint.strip() == tweet.text:
    print('hit')
    if toprint.strip() == tweet.text:
        toprint = random.choice(qlist)
        print(toprint)

api.update_status(toprint)

    #print(tweet.text)
#get_last_tweet()
