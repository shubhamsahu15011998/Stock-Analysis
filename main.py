from sqlalchemy.orm import sessionmaker

from DB import get_database_connection
from init import app
from models import Base


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)


