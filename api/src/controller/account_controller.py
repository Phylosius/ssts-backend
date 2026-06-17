from flask import Blueprint, request

from ..service.account_service import (
    get_by_id as get_account_by_id,
    get_all as get_all_accounts,
    save_all as save_accounts, update_accounts, delete_all
)

account_bp = Blueprint('account', __name__, url_prefix='/accounts')

@account_bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    if request.method == 'GET':
        return get_all_accounts()
    elif request.method == 'POST':
        return save_accounts(request.json)
    elif request.method == 'PUT':
        return update_accounts(request.json)
    elif request.method == 'DELETE':
        return delete_all(request.json)
    return None

@account_bp.route('/<account_id>', methods=['GET'])
def details(account_id: str):
    if request.method == 'GET':
        retrieved = get_account_by_id(account_id)
        if retrieved is None:
            return {"error": "account not found"}, 404
        return retrieved
    return None

