# Twitter Bot
import tweepy
import time
import random


class Bot:
    def __init__(self):
        self.ACCESS_TOKEN = "1110882786175606784-wIgaasNOxgaWZIFYYFG9aLikKnYDvi"
        self.ACCESS_TOKEN_SECRET = "IN4JjYHuEXPOqlLSrgTMtDGGoDKZxhfZQwzxWjKAfFlBQ"
        self.CONSUMER_KEY = "49n4OCNqs65Uyo3y09Er4sE7P"
        self.CONSUMER_SECRET = "crN0lPWqO11XJwAjhtj5V0wYKLUvn0rzYUnsHn9SVKECEde6XR"
        self.api = self.authenticate()
        self.file_name = 'lastSeenID.txt'
        self.file_name2 = 'the_call.txt'

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except:
            print("The bot was unable to authenticate. Please check the tokens.")
        else:
            print("The bot has been authenticated")
            return api

    @staticmethod
    def retreivelastseenid(file_name):
        f_read = open(file_name, 'r')
        last_seen_id = int(f_read.read().strip())
        f_read.close()
        return last_seen_id

    @staticmethod
    def storelastseenid(last_seen_id, file_name):
        f_write = open(file_name, 'w')
        f_write.write(str(last_seen_id))
        f_write.close()
        return

    def replytweets(self, file_name):
        while True:
            print('replying to tweets...')
            last_seen_id = self.retreivelastseenid(self.file_name)
            mentions = self.api.mentions_timeline(last_seen_id, tweet_mode='extended')
            for mention in reversed(mentions):
                print (str(mention.id) + ' - ' + mention.full_text)
                last_seen_id = mention.id
                self.storelastseenid(last_seen_id, file_name)
                if 'try' in mention.full_text.lower():
                    self.api.update_status('@' + mention.user.screen_name + ' ' + 'this is a test', mention.id)
            time.sleep(5)

    def readfromfile(self):
        linea = 0;
        while True:
            print("Opening File...")
            my_file = open('the_call.txt', 'r')
            file_lines = my_file.readlines()
            my_line = random.choice(my_file)
            for line in file_lines:
                if len(line) == 280:
                    print(my_line)
                    self.api.update_status(my_line)
                    time.sleep(86400)
                else:
                    print("Could not print line, caracter number exceded.")
            print("Closing File...")
            my_file.close()


if __name__ == '__main__':
    twitter_bot = Bot()
    #twitter_bot.replytweets('lastSeenID.txt')
    twitter_bot.readfromfile()
