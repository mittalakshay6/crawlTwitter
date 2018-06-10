Synopsis
========

A simple script to scrape for Tweets using the Python package requests
to retrieve the content and Beautifullsoup4 to parse the retrieved
content.

Per Tweet it scrapes the following information: + Username and Full Name
+ Tweet-id + Tweet-url + Tweet text + Tweet html + Tweet timestamp + No. of likes +
No. of replies + No. of retweets

1. Installation and Usage
=========================
    python setup.py install

2.2 The CLI
-----------

You can use the command line application to get your tweets stored to
JSON right away. crawlTwitter takes several arguments:

-  ``-h`` or ``--help`` Print out the help message and exits.

-  ``-l`` or ``--limit`` CrawlTwitter stops scraping when *at least*
   the number of tweets indicated with ``--limit`` is scraped. Since
   tweets are retrieved in batches of 20, this will always be a multiple
   of 20.

   Omit the limit to retrieve all tweets. You can at any time abort the
   scraping by pressing Ctrl+C, the scraped tweets will be stored safely
   in your JSON file.

-  ``--lang`` Retrieves tweets written in a specific language. Currently
   30+ languages are supported. For a full list of the languages print
   out the help message.

-  ``-bd`` or ``--begindate`` Set the date from which CrawlTwitter
   should start scraping for your query. Format is YYYY-MM-DD. The
   default value is set to 2006-03-21.

-  ``-ed`` or ``--enddate`` Set the enddate which CrawlTwitter should
   use to stop scraping for your query. Format is YYYY-MM-DD. The
   default value is set to today.

-  ``-p`` or ``--poolsize`` Set the number of parallel processes
   CrawlTwitter should initiate while scraping for your query. Default
   value is set to 20. Depending on the computational power you have,
   you can increase this number. It is advised to keep this number below
   the number of days you are scraping. For example, if you are
   scraping from 2017-01-10 to 2017-01-20, you can set this number to a
   maximum of 10. If you are scraping from 2016-01-01 to 2016-12-31, you
   can increase this number to a maximum of 150, if you have the
   computational resources.

-  ``-o`` or ``--output`` Gives the name of the output file. If no
   output filename is given, the default filename 'tweets.json' or 'tweets.csv' 
   will be used.

-  ``-c`` or ``--csv`` Write the result to a CSV file instead of a JSON file.
   
-  ``-d`` or ``--dump``: With this argument, the scraped tweets will be
   printed to the screen instead of an outputfile. If you are using this
   argument, the ``--output`` argument doe not need to be used.

2.2.1 Examples of simple queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of how CrawlTwitter can be used:

``CrawlTwitter Trump --limit 100 --output=tweets.json``

``CrawlTwitter Trump -l 100 -o tweets.json``

``CrawlTwitter Trump -l 100 -bd 2017-01-01 -ed 2017-06-01 -o tweets.json``

2.2.2 Examples of advanced queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use any advanced query Twitter supports. An advanced query
should be placed within quotes, so that CrawlTwitter can recognize it
as one single query.

Here are some examples:

-  search for the occurence of 'Bitcoin' or 'BTC':
   ``CrawlTwitter "Bitcoin OR BTC " -o bitcoin_tweets.json -l 1000``
-  search for the occurence of 'Bitcoin' and 'BTC':
   ``CrawlTwitter "Bitcoin AND BTC " -o bitcoin_tweets.json -l 1000``
-  search for tweets from a specific user:
   ``CrawlTwitter "Blockchain from:VitalikButerin" -o blockchain_tweets.json -l 1000``
-  search for tweets to a specific user:
   ``CrawlTwitter "Blockchain to:VitalikButerin" -o blockchain_tweets.json -l 1000``
-  search for tweets written from a location:
   ``CrawlTwitter "Blockchain near:Seattle within:15mi" -o blockchain_tweets.json -l 1000``

2.3 From within Python
----------------------

You can easily use CrawlTwitter from within python:

::

    from CrawlTwitter import query_tweets
    
    if __name__ == '__main__':
        list_of_tweets = query_tweets("Trump OR Clinton", 10)

        #print the retrieved tweets to the screen:
        for tweet in query_tweets("Trump OR Clinton", 10):
            print(tweet)
        
        #Or save the retrieved tweets to file:
        file = open(“output.txt”,”w”) 
        for tweet in query_tweets("Trump OR Clinton", 10):
            file.write(tweet.encode('utf-8')) 
        file.close()

3. Output
=========

All of the retrieved Tweets are stored in the indicated output file. The
contents of the output file will look like:

::

    [{"fullname": "Rupert Meehl", "id": "892397793071050752", "likes": "1", "replies": "0", "retweets": "0", "text": "Latest: Trump now at lowest Approval and highest Disapproval ratings yet. Oh, we're winning bigly here ...\n\nhttps://projects.fivethirtyeight.com/trump-approval-ratings/?ex_cid=rrpromo\u00a0\u2026", "timestamp": "2017-08-01T14:53:08", "user": "Rupert_Meehl"}, {"fullname": "Barry Shapiro", "id": "892397794375327744", "likes": "0", "replies": "0", "retweets": "0", "text": "A former GOP Rep quoted this line, which pretty much sums up Donald Trump. https://twitter.com/davidfrum/status/863017301595107329\u00a0\u2026", "timestamp": "2017-08-01T14:53:08", "user": "barryshap"}, (...)
    ]

3.1 Opening the output file
---------------------------

In order to correctly handle all possible characters in the tweets
(think of Japanese or Arabic characters), the output is saved as utf-8
encoded bytes. That is why you could see text like
"\u30b1 \u30f3 \u3055 \u307e \u30fe ..." in the output file.

What you should do is open the file with the proper encoding:

.. figure:: https://user-images.githubusercontent.com/4409108/30702318-f05bc196-9eec-11e7-8234-a07aabec294f.PNG

   Example of output with Japanese characters

TO DO
=====

-  CrawlTwitter can not retrieve retweets.
-  Add caching potentially? Would be nice to be able to resume scraping
   if something goes wrong and have half of the data of a request cached
   or so.








github crawl not allowed

https://www.quora.com/What-is-the-effective-way-to-crawl-all-projects-on-GitHub

