from flask import Flask
app=Flask(__name__)


@app.route("/")
def home():
    return "hii vimal"

@app.route("/login")
def log():
    return "welcome founder"    

if __name__=="__main__":
    app.run(debug=True)