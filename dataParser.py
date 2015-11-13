import json
# Can comment this out if not printing to screen
import sys
import codecs


def parse(data):
    # Can comment this out if not printing to screen
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout,
                                                       errors='replace')
    tweet = json.loads(data)
    print(tweet["user"]["screen_name"] + " " + tweet["text"])
    # Return true keeps reading from stream,
    # Return false ends reading from stream,
    # This is a nice way of saying only allow me to exit program
    if tweet["user"]["screen_name"] == "dixonwille" and tweet["text"]\
            .find('#exit') > -1:
        return False
    else:
        return True
