from flask import Blueprint, request

from web_service.model import CnnClassifier


bp = Blueprint("views", __name__)


@bp.route("/ml-service/object-detection", methods=["POST"])
def object_detection():
    request_json = request.get_json()
    if request_json["key"] != "123":
        return "API key incorrecta", 401

    image = request_json["image"]
    classifier = CnnClassifier(image)
    prediction = classifier.predict()
    return prediction
