
class Account:

    def __init__(self, id: str, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'Account(id={self.id}, username={self.username}, email={self.email}, password={self.password}, face_id={self.face_id})'
