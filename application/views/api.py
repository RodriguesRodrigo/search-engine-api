from flask import Blueprint, jsonify


api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/healthcheck", methods=("GET",))
def health_check():
    return jsonify({"message": "ok"})
