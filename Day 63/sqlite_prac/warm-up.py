from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Hi</h1>"


if __name__ == "__main__":
    app.run(debug=True)