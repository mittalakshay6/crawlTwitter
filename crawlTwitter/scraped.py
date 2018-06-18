from crawlTwitter.database import Database

from crawlTwitter.query import query_tweets
import time
if __name__ == '__main__':

    # db = Database()
    try:
        file = open("keywords.txt", "r")
        keywords = file.readlines()
        # print(keywords)
        for word in keywords:
            print("Querying for: " + word)
            # print("Querying tweets")
            list_of_tweets = query_tweets(word)
            print("printing")
            for tweet in list_of_tweets:
                print(tweet.text)
                print()
                print()
            print("Sleeping for 2 min")
            time.sleep(120)
    except:
        pass
    #     db.insert_tweet(tweet)
    # print the retrieved tweets to the screen:
    #
    # #Or save the retrieved tweets to file:
    # file = open("output.txt","w")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet.encode('utf-8'))
    # file.close()
