from ..model.account import Account
from ..dto.account_dto import AccountDTO

def account_to_dict(account: Account):
    return AccountDTO.from_model(account).to_dict()

def accounts_to_dicts(accounts):
    return list(map(lambda a: account_to_dict(a), accounts))
