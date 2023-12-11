from flask import Flask, render_template, request

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
        print(pw_name)
        print(maile_name)

        #usernameのget
        words["username"] = "KOSUPE"
        words["userimg"]  = "static\img\maru_icon.png"

    return render_template('public/index.html', key=words)

@app.route("/igo")
def igo():
    print("igo")
    return render_template('igo/index.html')

@app.route("/<value>")
def test(value):
    print(f"{type(value)}, 値:{value}")
    return f"<h1>渡された値は[{value}]です</h1>"


if __name__=="__main__":
    app.run(port=8000, debug=True)