from flask import Flask
from app.controllers.BikeController import api as bike_api
from app.core.BikeEntity import BikeEntity

from app.repository.database import db_session
from app.repository.database import db_init

app = Flask(__name__)

app.register_blueprint(bike_api)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.teardown_appcontext
def shut_down_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    '''
    session = db_session
    
    result = BikeEntity.query.all()
    print(result)
    '''
    app.run(debug=True)