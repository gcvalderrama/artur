from flask import Blueprint, request, make_response
from app.repository.database import db_init
from app.components.BikeComponent import BikeComponent

api = Blueprint('bike_api', __name__)

url_prefix = "/bikes"

component = BikeComponent()


@api.route(url_prefix, methods=["GET"])
def list_items():
    bikes = component.list()
    return make_response({"data": bikes}, 200)


@api.route(url_prefix, methods=["POST"])
def create():
    data = request.get_json()
    component.create(data)
    return make_response({}, 200)


@api.route(url_prefix + "/<key>", methods=["PUT"])
def update(key):
    data = request.get_json()
    result = component.update(key, data)
    return make_response(result, 200)




