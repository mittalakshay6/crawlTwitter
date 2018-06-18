import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client["testing_db"]
        self.collection = self.db["testing"]

    def get_db(self):
        return self.db

    def get_col(self):
        return self.collection

    def insert_tweet(self, tweet):
        doc = {"timestamp": tweet.timestamp, "text": tweet.text, "url": tweet.url}
        doc_id = self.collection.insert_one(doc)
        return doc_id

    # No parameter in find gives same result as SELECT * in MySQL

    def get_one_tweet(self):
        return self.collection.find_one()

    # It will give the latest 100 tweets
    def get_all_tweets(self):
        return self.collection.find()
