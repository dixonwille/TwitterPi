# TwitterPi

## Presentation

[TwitterPi Presentation](http://go-talks.appspot.com/github.com/dixonwille/TwitterPi/Presentation/IoT.slide)

## Software Prerequisites
- Python2.7
- tweepy

To install tweepy use `pip install tweepy`
## Credentials
The client looks for a file called `credentials.json`. It should look like this:
```
{
  "ConKey":"<consumerKey>",
  "ConSec":"<consumerSecret>",
  "AccessToken": "<accessToken>",
  "AccessSecret": "<accessTokenSecret>"
}
```
The `.gitignore` file is setup to not commit this files for versioning. It is highly recommended you keep these keys a secret as anyone with access to them can use your app as if they were you.

### Creating Credentials
To get they keys that you need to access Twitter's API:
 1. Visit `apps.twitter.com`
 2. Login to your twitter account (if not already logged in)
 3. Click the `Create New App` button
 4. Name your app (must me unique ex. &lt;username&gt;&#95;TwitterPi)
 5. Give your app a description
 6. Give your app a homepage
  - Use your github repo
  - If you don't have one you can use mine `https://github.com/dixonwille/TwitterPi`
 7. Sign your life away by agreeing to the Developer Agreement
 8. Click `Create your Twitter Application`
 9. Go to the `Permissions` tab and update Access to `Read Only` and click `Update Settings`
 10. Go to the `Keys and Access Tokens` tab and click `Create my access token`
 11. Copy these keys and put them into your `credentials.json` file respectively


## Running client
To run the client it is as simple as `python main.py`
