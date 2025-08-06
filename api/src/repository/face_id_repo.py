from .pg import transactional
from ..model.face_id import FaceId
from ..mapper.array_mapper import ndarray_to_pgarray


@transactional
def save(cur, face_id: FaceId, account_id: str):
    cur.execute(
        "INSERT INTO face_id (id, account_id, added_at, updated_at, face_encodings) VALUES (%s, %s, %s, %s, %s);",
        (face_id.id, account_id, face_id.created_at, face_id.updated_at, ndarray_to_pgarray(face_id.face_encodings)),
    )
    return True

@transactional
def delete(cur, face_id_id: str):
    cur.execute(
        "DELETE FROM face_id WHERE id = %s;",
        (face_id_id,),
    )
    return True

@transactional
def get_by_id(cur, face_id_id: str):
    cur.execute(
        "SELECT id, added_at, updated_at, face_encodings FROM face_id WHERE id = %s;",
        (face_id_id,),
    )

    data = cur.fetchone()
    if data is None:
        return None
    return FaceId(*list(data))

@transactional
def update(cur, face_id_id: str, face_id: FaceId):
    cur.execute(
        "UPDATE face_id SET added_at = %s, updated_at = %s, face_encodings = %s WHERE id = %s"
        "RETURNING id, added_at, updated_at, face_encodings;",
        (face_id.created_at, face_id.updated_at, ndarray_to_pgarray(face_id.face_encodings), face_id_id),
    )
    data = list(cur.fetchone())
    return FaceId(*data)
