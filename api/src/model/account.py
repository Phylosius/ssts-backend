from .face_id import FaceId
from ..repository.pg import transactional

@transactional
def get_face_ids_by_account_id(cur, account_id: str):
    cur.execute(
        "SELECT id, added_at, updated_at, face_encodings FROM face_id WHERE account_id = %s;",
        (account_id,),
    )

    data = cur.fetchall()
    return [FaceId(*list(row)) for row in data]

class Account:

    def __init__(self, id: str, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def get_face_ids(self):
        return get_face_ids_by_account_id(self.id)

    def __str__(self):
        return f'Account(id={self.id}, username={self.username}, email={self.email}, password={self.password})'
