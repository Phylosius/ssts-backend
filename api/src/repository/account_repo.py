from .pg import transactional
from ..model.account import Account

@transactional
def save(cur, account: Account):
    cur.execute(
        "INSERT INTO account (id, username, email, password) VALUES (%s, %s, %s, %s);",
        (account.id, account.username, account.email, account.password),
    )
    return True

@transactional
def delete(cur, account_id: str):
    cur.execute(
        "DELETE FROM account WHERE id = %s;",
        (account_id,),
    )
    return True

@transactional
def get_by_id(cur, account_id: str):
    cur.execute(
        "SELECT id, username, email, password FROM account WHERE id = %s;",
        (account_id,),
    )
    data = cur.fetchone()
    if data is None:
        return None
    data = list(data)
    return Account(*data)

@transactional
def update(cur, account_id: str, account: Account):
    cur.execute(
        "UPDATE account SET username = %s, email = %s, password = %s WHERE id = %s"
        "RETURNING id, username, email, password;",
        (account.username, account.email, account.password, account_id),
    )
    data = list(cur.fetchone())
    return Account(*data)
