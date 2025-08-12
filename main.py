from flask import Flask
from flask_sqlalchemy import SQLAlchemy #ORM

app = Flask(__name__)

#Create Databasse

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)


#Create routers

@app.route("/")
def home():
    return "hello"

#http:/www.thenerdbook.io/




if __name__ == "__main__":
    app.run(debug=True)