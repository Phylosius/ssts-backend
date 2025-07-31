from datetime import datetime
from numpy import ndarray

class FaceId:

    def __init__(self, id: str, created_at: datetime, updated_at: datetime, face_encodings: ndarray):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.face_encodings = face_encodings

    def __str__(self):
        return f'FaceId(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at}, face_encodings={self.face_encodings})'
