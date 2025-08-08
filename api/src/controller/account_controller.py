from flask import Blueprint, jsonify, request

from ..service.account_service import (
    get_all as get_all_accounts,
    save_all as save_accounts
)

account_bp = Blueprint('account', __name__, url_prefix='/accounts')

@account_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return get_all_accounts()
    elif request.method == 'POST':
        return {"message": "POST method is not implemented yet"}, 501
    return None
