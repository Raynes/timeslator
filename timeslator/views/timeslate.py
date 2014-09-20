import os
import json
from flask import Blueprint, request
from chronyk import Chronyk
from timeslator.utils import error

ENDPOINT = os.environ.get('ENDPOINT', '/timeslate')

bp = Blueprint('timeslate', __name__)


@bp.route(ENDPOINT)
def timeslate():
    input_time = request.args.get('input')
    output_format = request.args.get('format')
    tz = int(request.args.get('tz', '0'))
    if not input_time:
        return error("input parameter is required"), 500
    try:
        input_time = int(input_time)
    except ValueError:
        pass
    try:
        sanitized = Chronyk(input_time)
    except:
        return error("Timeslate does not accept this input format."), 500
    output = {'ctime': sanitized.ctime(timezone=tz),
              'timestring': sanitized.timestring(timezone=tz),
              'timestamp': sanitized.timestamp(timezone=tz),
              'input': input_time}
    if output_format:
        output['formatted'] = sanitized.timestring(output_format, timezone=tz)
    return json.dumps(output)
