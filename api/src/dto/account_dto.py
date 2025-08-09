
from uuid import uuid4
from api.src.model.account import Account

class AccountDTO:
    def __init__(self, id: str, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    
    def from_dict(data: dict):
        return AccountDTO(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email')
        )

    @classmethod
    def from_model(cls, account: Account):
        return cls(account.id, account.username, account.email)

class AccountCreateDTO:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def to_model(self):
        account_id = str(uuid4())
        return Account(account_id, self.username, self.email, self.password)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )

class AccountUpdateDTO(AccountCreateDTO):
    def __init__(self, id: str, username: str, email: str, password: str):
        super().__init__(username, email, password)
        self.id = id

    def to_model(self):
        return Account(self.id, self.username, self.email, self.password);

    @classmethod
    def from_dict(cls, data: dict):
        return AccountUpdateDTO(data.get('id'), data.get('username'), data.get('email'), data.get('password'))

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
