# Twitter Bot
import tweepy
import time
from Credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
mentions = api.mentions_timeline()

FILE_NAME = 'lastSeenID.txt'


def retreivelastseenid(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def storelastseenid(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def replytweets():
    print('replying to tweets...')
    last_seen_id = retreivelastseenid(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print (str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        storelastseenid(last_seen_id, FILE_NAME)
        if 'try' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name + ' ' + 'this is a test', mention.id)


while True:
    replytweets()
    time.sleep(5)
