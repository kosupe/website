from flask import Flask, render_template, request, Markup
from static.sql.db import DBClass

import random


def create_categry_jsons():
    categry_infos = DBClass.select_tagtable_all()
    categry_jsons = []
    
    for categry_info in categry_infos:
        categry_json = {}
        categry_json["title"] = categry_info[1]
        categry_json["count"] = DBClass.count_articletable_where_tagid(categry_info[0])
        categry_jsons.append(categry_json)
    return categry_jsons

def create_article_json():
    article_infos = DBClass.select_articletable_all()
    article_jsons = []
    
    for article_info in article_infos:
        article_json = {}
        article_json["articleid"]    = article_info[0]
        article_json["articletitle"] = article_info[1]
        article_json["date"]         = article_info[3]
        article_json["image"]        = article_info[5]
        article_jsons.append(article_json)
    article_jsons.reverse()
    return article_jsons

app = Flask(__name__, static_folder="./static")

@app.route("/", methods=["GET", "POST"])
def home():
    words ={
        "username" : "GUEST",
        "userimg"  : "https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png"
    }

    #emailとpwのPOST
    if request.method =="POST":
        maile_name = request.form.get("email_name")
        pw_name = request.form.get("pw_name") 

        #EmailとpwのPOSTしたとき
        user_info = DBClass.serch_user(maile_name, pw_name)
        if len(user_info) > 0: #userが見つかったとき
            words["username"] = user_info[0][2]
            words["userimg"]  = user_info[0][3]
    return render_template('index.html', key=words)

@app.route("/igo")
def igo():
    print("igo")
    return render_template('igo.html')

@app.route("/Article")
def Article_home():
    print("Article")
    return render_template('article_home.html', article_jsons = create_article_json(), categry_jsons = create_categry_jsons())

@app.route("/Article/test")
def Article_test():
    print("Article")
    return render_template('article_test.html', categry_jsons = create_categry_jsons())


@app.route("/Article/<articleid>")
def Article(articleid):
    print("Article")
    article_info = DBClass.select_articletable_where_id(articleid)
    article_json = {
        "title": article_info[0][1],
        "html" : Markup(article_info[0][2].replace('""', '"')),
        "date" : article_info[0][3]
    }
    return render_template('article.html', article_json=article_json, categry_jsons = create_categry_jsons())

@app.route("/kspda")
def kspda_home():
    return render_template('kspda_home.html')

@app.route("/kspda/High_schoolDD")
def kspda_DD():
    return render_template('kspda_DD.html')


if __name__=="__main__":
    app.run(port=8000, debug=True)




