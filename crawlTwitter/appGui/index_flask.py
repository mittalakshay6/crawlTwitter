from datetime import time

from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from crawlTwitter import query_tweets

UPLOAD_FOLDER = '../'
ALLOWED_EXT = {'.txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/index')
def upload_file():
    return render_template('index.html')


@app.route('/uploading', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('uploading.html')


@app.route('start')
def startScraping():
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

                print("Sleeping for 2 min")
            time.sleep(120)
    except:
        pass


if __name__ == '__main__':
    app.run(debug=True)
