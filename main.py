import credParser as cred
import dataParser
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):

    def on_data(self, data):
        return dataParser.parse(data)

    def on_error(self, status):
        print status


if __name__ == '__main__':
    credentials = cred.parseFile("credentials.json")
    l = StdOutListener()
    auth = OAuthHandler(credentials['ConKey'], credentials['ConSec'])
    auth.set_access_token(credentials['AccessToken'],
                          credentials['AccessSecret'])
    stream = Stream(auth, l)
    stream.filter(track=['#red', '#blue', '#green', '#exit'])
