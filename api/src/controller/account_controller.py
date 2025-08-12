from flask import Blueprint, jsonify, request

from ..service.account_service import (
    get_all as get_all_accounts,
    save_all as save_accounts, update_accounts, delete_all
)

account_bp = Blueprint('account', __name__, url_prefix='/accounts')

@account_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
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
