
from flask import make_response, Blueprint

bp = Blueprint('health', __name__)


@bp.route('/health')
def messages():
    return make_response('Ok')

@bp.route('/status')
def status():
    return make_response('green')

