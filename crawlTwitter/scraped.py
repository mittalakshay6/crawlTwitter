from crawlTwitter.database import Database

from crawlTwitter.query import query_tweets

if __name__ == '__main__':

    # db = Database()

    file = open("keywords.txt", "r")
    keywords = file.read()
    # print(keywords)

    print("Querying tweets")
    list_of_tweets = query_tweets("State bank of india")
    print("printing")
    for tweet in list_of_tweets:
        print("done")
        print(tweet.text)
        print()
    #     db.insert_tweet(tweet)
    # print the retrieved tweets to the screen:
    #
    # #Or save the retrieved tweets to file:
    # file = open("output.txt","w")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet.encode('utf-8'))
    # file.close()
