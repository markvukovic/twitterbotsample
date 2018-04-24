import tweepy
from time import sleep

#constants
FILENAME="botscript.txt"

#Twitter Info- changes based on user that will be tweeting
auth = tweepy.OAuthHandler("codehere",  "othercodehere")
auth.set_access_token("tokenhere", "othertokenheretoo")
api = tweepy.API(auth)
TWEET="Testing"

def send_a_tweet(TWEET):  #This function sends a single tweet
    try:
        api.update_status(TWEET)
    except tweepy.TweepError as e: #Used for twitter errors. Prints them out.
        print(e.reason)
     
def tweet_a_file(filename): #This tweets out a file, one line at a time
    my_file=open(FILENAME,'r') #read all lines from the file. Saves in all_the_tweets
    all_the_tweets=my_file.readlines()
    my_file.close()
    for tweet in all_the_tweets:
        tweet=tweet.replace("\n","")
        try:
            api.update_status(tweet) #the code that tweets
            print(tweet) #for us to see what we are tweeting
            print("*********************************")#so we can see a break between tweets
            sleep(300) #how long to break between tweets, in seconds
        except tweepy.TweepError as e: #Used for twitter errors. Prints them out.
            print(e.reason)

tweet_a_file(FILENAME)
