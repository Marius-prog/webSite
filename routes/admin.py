
from flask import render_template, Blueprint
from models import Contact

bp = Blueprint('admin', __name__)


@bp.route('/messages')
def messages():
    results = Contact.query.all()
    # with open('data/contact.jsonl', 'r') as f:
    #     raw = f.readlines()
    #
    #     msgs = [json.loads(line) for line in raw]
    #     # print(msgs)
    #
    #     render_template('base.html')
    return render_template('messages.html', messages=results)
