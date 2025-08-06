from ..repository.account_repo import (
    get_all as get_all_accounts,
    save as save_account
    )
from ..dto.account_dto import AccountDTO, AccountCreateDTO

def get_all():
    return list(map(lambda a: AccountDTO.from_model(a).to_dict(), get_all_accounts()))

def save_all(accounts: list[AccountCreateDTO]):
    saved_accounts = []
    print(accounts)
    for account in accounts:
        to_save = AccountCreateDTO.from_dict(account).to_model()
        save_account(to_save)
        saved_accounts.append(to_save)

    return list(map(lambda a: AccountDTO.from_model(a).to_dict(), saved_accounts))
