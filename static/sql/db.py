import sqlite3

class DBClass():
    """
    <usertable>\n
    --+------------------+----------+------------+------------+--
      |  useremail (PK)  |  userpw  |  username  |  usericon  |
    --+------------------+----------+------------+------------+--
    
    <tagtable>\n
    --+--------------+-----------+--
      |  tagid (PK)  |  tagname  |
    --+--------------+-----------+--
    
    <articletable>\n
    --+-----------------+----------------+--------+--------+---------+---------+--
      | articleid (PK)  |  articletitle  |  html  |  date  |  tagid  |  image  |
    --+-----------------+----------------+--------+--------+---------+---------+--
    
    """
    _con = None
    _cur = None
    
    def _start_db():
        DBClass._con = sqlite3.connect("flask.db")
        DBClass._cur = DBClass._con.cursor()
    
    def _fin_db():
        DBClass._cur.close()
    
    #テーブル作成
    def _create():
        DBClass._start_db()
        DBClass._cur.execute("""CREATE TABLE articletable(
                             articleid INTEGER PRIMARY KEY AUTOINCREMENT,
                             articletitle TEXT,
                             html TEXT,
                             date TEXT,
                             tagid INTEGER NOT NULL,
                             image TEXT NOT NULL
                             );""")
        DBClass._con.commit()
        DBClass._fin_db()
    
    def _drop():
        DBClass._start_db()
        DBClass._cur.execute("""
        DROP TABLE articletable;
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def _insert():
        html ='''
        <!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Website</title>
    <link rel="stylesheet" href="static/css/article.css">
</head>

<body>
    <header>
        <a href="/">Home</a>
    </header>
    <div class="frame">
        <div class="articleArea">
            <div class="articleTitle">
                <h3>Pygameのマウス操作</h3>
                <div class="date">2023.12.12</div>
            </div>
            <div class="articleText">
                Pygameのマウスを扱いやすく工夫してみました。<br><br>
                MouseClassを作るというものです。以後Mouseと呼びます。<br>
                このMouseには常に現在のマウスのイベントを読み込み、クリックされたか、もしくはボタンが解放されたか、などを管理するものです。<br><br>
                <img src="../static/img/article/pygame_MouseClass.png"><br><br>
                このMouseをimportして使うと下記のように使える。<br><br>
                if&nbsp;Mouse.is_Left_clicked():<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("左クリックされました")<br><br>
                加えて、&nbsp;&nbsp;Mouse.X,&nbsp;Mouse.Y&nbsp;&nbsp;のようにしてカーソルのXY座標をどのファイルからでも参照できるようになります。<br><br>
                また、このMouseを使うときは、mainのwhile文の中でupdateを下記のように行う必要がある。<br><br>
                <img src="../static/img/article/pygame_MouseClass_main.png"><br><br><br>
                今回はpygameでのマウス操作を簡易的に行う手法をお話ししました。<br>
                他にも興味のある記事がありましたら、ぜひご覧ください。
            </div>
        </div>
        <div class="categryArea">
            <h2 class="categryTitle">Categry</h2>
            <div class="categrys">
                <ul>
                    <li><a href="#">Pygame</a>(1)</li>
                </ul>
            </div>
            
        </div>
    </div>


    <script src="static/js/article.js"></script>
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
</body>

</html>
        '''
        html = html.replace('"', '""')
        DBClass._start_db()
        DBClass._cur.execute(f"""
        INSERT INTO articletable (id,html) VALUES(1,'{html}');
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def _select():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT * FROM articletable;
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result


    #usertable
    def insert_usertable(user_Email, user_pw, user_name, user_icon_path=None):
        DBClass._start_db()
        if user_icon_path == None:
            DBClass._cur.execute(f"""
            INSERT INTO usertable (useremail,userpw,username) VALUES('{user_Email}','{user_pw}','{user_name}');
            """)
        else:
            DBClass._cur.execute(f"""
            INSERT INTO usertable (useremail,userpw,username,usericon) VALUES('{user_Email}','{user_pw}','{user_name}','{user_icon_path}');
            """)
        DBClass._con.commit()
        DBClass._fin_db()

    def select_usertable_all():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT * FROM usertable;
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result

    def serch_user(user_Email, user_pw):
        DBClass._start_db()
        res = DBClass._cur.execute(f"""
        SELECT * FROM usertable WHERE useremail='{user_Email}' and userpw='{user_pw}';
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result
    
    
    #tagtable
    def insert_tagtable(tagname):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        INSERT INTO tagtable (tagname) VALUES('{tagname}');
        """)
        DBClass._con.commit()
        DBClass._fin_db()
        
    def select_tagtable_all():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT * FROM tagtable;
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result
    
    def update_tagtable():
        DBClass._start_db()
        DBClass._cur.execute(f"""
        UPDATE tagtable set tagname = 'Pygame' where tagid = 1;
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    
    
    
    #articletable
    def insert_articletable(articletitle, html, date, tagid, image):
        DBClass._start_db()
        DBClass._cur.execute(f"""
        INSERT INTO articletable (articletitle,html,date,tagid,image) VALUES('{articletitle}','{html}','{date}',{tagid},'{image}');
        """)
        DBClass._con.commit()
        DBClass._fin_db()
    
    def select_articletable_all():
        DBClass._start_db()
        res = DBClass._cur.execute("""
        SELECT * FROM articletable;
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result
    
    def select_articletable_where_id(articleid):
        DBClass._start_db()
        res = DBClass._cur.execute(f"""
        SELECT * FROM articletable where articleid={articleid};
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result
    
    def count_articletable_where_tagid(tagid):
        DBClass._start_db()
        res = DBClass._cur.execute(f"""
        SELECT count(*) FROM articletable where tagid={tagid};
        """)
        result = res.fetchall()
        DBClass._con.commit()
        DBClass._fin_db()
        return result[0][0]
    
    def update_articletable():
        html = """
        Pygameのマウスを扱いやすく工夫してみました。<br><br>
                MouseClassを作るというものです。以後Mouseと呼びます。<br>
                このMouseには常に現在のマウスのイベントを読み込み、クリックされたか、もしくはボタンが解放されたか、などを管理するものです。<br><br>
                <img src="../static/img/article/pygame_MouseClass.png"><br><br>
                このMouseをimportして使うと下記のように使える。<br><br>
                if&nbsp;Mouse.is_Left_clicked():<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("左クリックされました")<br><br>
                加えて、&nbsp;&nbsp;Mouse.X,&nbsp;Mouse.Y&nbsp;&nbsp;のようにしてカーソルのXY座標をどのファイルからでも参照できるようになります。<br><br>
                また、このMouseを使うときは、mainのwhile文の中でupdateを下記のように行う必要がある。<br><br>
                <img src="../static/img/article/pygame_MouseClass_main.png"><br><br><br>
                今回はpygameでのマウス操作を簡易的に行う手法をお話ししました。<br>
                他にも興味のある記事がありましたら、ぜひご覧ください。
        """
        html = html.replace('"', '""')
        DBClass._start_db()
        DBClass._cur.execute(f"""
        UPDATE articletable set html = '{html}' where articleid = 1;
        """)
        DBClass._con.commit()
        DBClass._fin_db()

if __name__ == "__main__":
    
    #DBClass.insert_usertable(user_Email="kosupppppeeeee@gmail.com", user_pw="kosupe", user_name="Kosupe", user_icon_path="static\img\maru_icon.png")
    #DBClass._drop()
    
    html ='''
            <div class="articleText">
                今回はflaskでHTMLを埋め込んでみたのでそのやり方を紹介します。<br><br>
                やり方としてはとてもシンプルで、埋め込みたいHTMLをそのままstr型で保存して、returnで渡すというものです。<br>
                下記のコードのように記述します。<br><br>
                <img src="../static/img/article/flask_umekomi.png"><br><br>
                Markup()の中に書くことによってdivなどのタグをエスケープされないようにしています。<br><br>
                今回はHTMLの埋め込み方法のひとつを紹介しました。<br>
                詳しく知りたい方はこちら
                <a href="https://ja.stackoverflow.com/questions/46630/flask%e3%81%a7%e5%a4%89%e6%95%b0%e3%82%92%e6%96%87%e5%ad%97%e5%88%97%e3%81%a7%e3%81%af%e3%81%aa%e3%81%8fhtml%e3%81%ae%e3%82%bf%e3%82%b0%e3%81%a8%e3%81%97%e3%81%a6%e8%aa%ad%e3%81%bf%e8%be%bc%e3%81%be%e3%81%9b%e3%81%9f%e3%81%84">こちら</a>
                の記事が参考になると思います。    
            </div>
        '''
    html = html.replace('"', '""')
    
    """tasks = DBClass.insert_articletable(
        articletitle="flaskでHTMLを埋め込んでみた",
        html=html,
        date="2023.12.18",
        tagid=2,
        image="https://laplace-daemon.com/wp-content/uploads/2020/02/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88-2019-07-09-21.21.59.png"
    )"""
    
    #DBClass.update_articletable()
    #tasks = DBClass.insert_tagtable("Flask")
    tasks = DBClass.select_articletable_all()
    print(tasks)