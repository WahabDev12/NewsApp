from flask import Flask,render_template,url_for,redirect,request
import os
from flask_sqlalchemy import SQLAlchemy
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        key_word = request.form.get("word")
        newsapi = NewsApiClient(api_key = "90f837dd9edf4f97839e4753b6cd6c94")
        top_headlines  = newsapi.get_everything(q=str(key_word))    
        articles = top_headlines["articles"]
        desc = []
        news = []
        img = []
        url = []
        for i in range(len(articles)):
            myarticles  = articles[i]
            news.append(myarticles["title"]) 
            desc.append(myarticles["description"])
            img.append(myarticles["urlToImage"]) 
            url.append(myarticles["url"])

        my_list = zip(news,desc,img,url)
        return render_template("index.html", context = my_list, key_word= "Search results for " + key_word)
    else:
        return render_template("index.html", title="Error")


if __name__ == "__main__":
    app.run(debug = True)