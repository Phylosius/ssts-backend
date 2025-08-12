import face_recognition
from numpy import array

from ..dto.face_info_dto import FaceInfoDto
from ..dto.ltbr_rectangle import LTBRRectangle
from ..dto.face_encodings_dto import EncodingsMatchInfoDTO

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

def compare_faces(known_faces: list, face_to_check, tolerance: float = 0.7):
    known_faces = array([array(face) for face in known_faces])
    face_to_check = array(face_to_check)
    face_distances = face_recognition.face_distance(known_faces, face_to_check)
    face_matches = face_recognition.compare_faces(known_faces, face_to_check, tolerance=tolerance)

    matches = []
    for i, face in enumerate(known_faces):
        matches.append(
            EncodingsMatchInfoDTO(
                list(face),
                bool(face_matches[i]),
                face_distances[i]
            ).to_dict()
        )

    return {
        "toCheckEncoding": list(face_to_check),
        "matches": matches
    }