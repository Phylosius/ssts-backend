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
