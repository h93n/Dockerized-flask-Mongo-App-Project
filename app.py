import base64
#import add
#import tmdbb
import data_ip
from tmdbb import MoviePosterDownloader

import requests
from data_ip import MovieDatabase
from flask import Flask, render_template, request
from pymongo import MongoClient





app = Flask(__name__)
#
# DOMAIN = 'mongodb'
# PORT = 27017
# client = MongoClient(
#         host = [ str(DOMAIN) + ":" + str(PORT) ],
#         serverSelectionTimeoutMS = 3000, # 3 second timeout
#         username = "admin",
#         password = "root",
#     )
#
# db = client["movies"]
# collection = db["movies"]

@app.route('/')
def index():
    return render_template('searchH.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        DOMAIN = 'mongodb'
        PORT = 27017
        USERNAME = 'admin'
        PASSWORD = 'root'
        DB_NAME = 'movies'
        COLLECTION_NAME = 'movies'

        movie_db = MovieDatabase(DOMAIN, PORT, USERNAME, PASSWORD, DB_NAME, COLLECTION_NAME)
        result = movie_db.search_in_mongo(query)
        if result:
            image_url=movie_db.search_to_get_posterURL(query)
            return render_template('result1.html', image_url=image_url)

        else:
           api_key = '0e627a7b49ba25e9ba89bc8d60514db4'
           downloader = MoviePosterDownloader(api_key)
           res1=downloader.add_to_mongo(query, movie_db)

           if(res1==1):
                image_url = movie_db.search_to_get_posterURL(query)
                return render_template('result1.html', image_url=image_url)

           else:
            return render_template('not_found.html')

    return render_template('searchH.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)