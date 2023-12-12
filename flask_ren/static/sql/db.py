import sqlite3

class DBClass():
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
        DBClass._cur.execute("""CREATE TABLE usertable(
                             useremail TEXT PRIMARY KEY,
                             userpw TEXT NOT NULL,
                             username TEXT NOT NULL,
                             usericon TEXT DEFAULT 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'
                             );""")
        DBClass._con.commit()
        DBClass._fin_db()
    
    def _drop():
        DBClass._start_db()
        DBClass._cur.execute("""
        DROP TABLE usertable;
        """)
        DBClass._con.commit()
        DBClass._fin_db()

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


if __name__ == "__main__":
    
    #DBClass.insert_usertable(user_Email="kosupppppeeeee@gmail.com", user_pw="kosupe", user_name="Kosupe", user_icon_path="static\img\maru_icon.png")
    tasks = DBClass.serch_user(user_Email="kosupppppeeeee@gmail.com", user_pw="kosupe")
    print(tasks)