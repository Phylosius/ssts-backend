from ..repository.face_id_repo import get_all_by_account_id as get_face_ids_by_account_id

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
