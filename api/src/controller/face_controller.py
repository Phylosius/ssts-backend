import uuid

from flask import Blueprint, request

from ..config import VARIABLES
from ..service.face_service import get_faces_info

face_bp = Blueprint('face', __name__, url_prefix='/face')

@face_bp.route('/describe', methods=['POST'])
def describe_face():
    if "image" not in request.files:
        return {"error": "image not found"}, 400

    image = request.files["image"]
    if image.filename == "":
        return {"error": "image filename is empty"}, 400
    image_extension = image.filename.split(".")[-1]

    VARIABLES.TEMP_IMAGE_PATH.mkdir(parents=True, exist_ok=True)
    image_path = (VARIABLES.TEMP_IMAGE_PATH / f"{str(uuid.uuid4())}.{image_extension}").resolve()
    image.save(image_path)

    return get_faces_info(image_path)