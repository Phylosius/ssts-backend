import face_recognition

from ..dto.face_info_dto import FaceInfoDto
from ..dto.ltbr_rectangle import LTBRRectangle

def get_faces_info(image_path: str):
    faces_info = []

    image = face_recognition.load_image_file(image_path)
    faces_locations = face_recognition.face_locations(image)
    faces_encodings = face_recognition.face_encodings(image, faces_locations)

    if len(faces_locations) > 0:
        for i in range(len(faces_locations)):
            faces_info.append(
                FaceInfoDto(
                    "",
                    list(faces_encodings[i]),
                    LTBRRectangle(
                        faces_locations[i][3], faces_locations[i][0], faces_locations[i][2], faces_locations[i][1])
                ).to_dict()
            )

    return faces_info