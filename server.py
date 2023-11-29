from flask import Flask, request
app = Flask(__name__, static_folder='./public')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/login", methods=["POST"])
def login():
    print(request.form.get("email"))
    print(request.form.get("password"))
    return app.send_static_file('index.html')
    
app.run(port=8000, debug=True)
