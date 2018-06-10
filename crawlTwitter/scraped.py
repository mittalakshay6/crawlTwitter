from crawlTwitter.database import Database

from crawlTwitter.query import query_tweets

if __name__ == '__main__':

    db = Database()

    file = open("keywords.txt", "r")
    keywords = file.read()

    print("Querying tweets")

    list_of_tweets = query_tweets(keywords)

    print("Tweets queried: ")
    print(len(list_of_tweets))
    print("Insert in Database")

    for tweet in list_of_tweets:
        db.insert_tweet(tweet)

    print("Printing Tweets URL")

    allTweets = db.get_all_tweets()
    for tweet in allTweets:
        print(tweet['url'])

    # print the retrieved tweets to the screen:
    #
    # #Or save the retrieved tweets to file:
    # file = open("output.txt","w")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet.encode('utf-8'))
    # file.close()
