from ..repository.account_repo import (
    get_all as get_all_accounts,
    get_by_id as get_account_by_id,
    save as save_account,
    update as update_account,
    delete as delete_account,
    )
from ..dto.account_dto import AccountDTO, AccountCreateDTO, AccountUpdateDTO
from ..mapper.account_mapper import accounts_to_dicts


def get_all():
    return list(map(lambda a: AccountDTO.from_model(a).to_dict(), get_all_accounts()))

def save_all(accounts: [AccountCreateDTO]):
    saved_accounts = []
    print(accounts)
    for account in accounts:
        to_save = AccountCreateDTO.from_dict(account).to_model()
        save_account(to_save)
        saved_accounts.append(to_save)

    return list(map(lambda a: AccountDTO.from_model(a).to_dict(), saved_accounts))

def update_accounts(accounts):
    updated_accounts = []
    for account in accounts:
        to_update = AccountUpdateDTO.from_dict(account).to_model()
        update_account(to_update.id, to_update)
        updated_accounts.append(to_update)
    return accounts_to_dicts(updated_accounts)

def delete_all (accounts_ids):
    deleted_accounts = []
    for id in accounts_ids:
       deleted_accounts.append(get_account_by_id(id))
       delete_account(id)

    return accounts_to_dicts(deleted_accounts)