from crawlTwitter import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("Wells AND Fargo", 10)

    # #print the retrieved tweets to the screen:
    for tweet in query_tweets("Wells AND Fargo", 10):
        print(tweet)
    #
    # #Or save the retrieved tweets to file:
    # file = open("output.txt","w")
    # for tweet in query_tweets("Trump OR Clinton", 10):
    #     file.write(tweet.encode('utf-8'))
    # file.close()