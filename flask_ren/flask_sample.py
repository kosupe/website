from flask import Flask, render_template

app = Flask(__name__, static_folder="./static")

@app.route("/")
def home():
    return render_template('public/index.html')

@app.route("/igo")
def igo():
    print("igo")
    return render_template('igo/index.html')


if __name__=="__main__":
    app.run(port=8000, debug=True)