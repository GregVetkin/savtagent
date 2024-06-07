import json
from flask              import Response, Blueprint, request
from modules.system     import SystemLogCollector, reboot, shutdown


blueprint_system = Blueprint('system', __name__)


BAD_PRIORITY    = {'error': 'Bad priority. Accepted: 0, 1, 2, 3, 4, 5, 6, 7, debug, info, notice, warning, err, crit, alert, emerg'}
PRIORITIES      = [None, "0", "1", "2", "3", "4", "5", "6", "7", "debug", "info", "notice", "warning", "err", "crit", "alert", "emerg"]


@blueprint_system.route('/system/logs', methods=['GET'])
def journalctl_logs():
    since       = request.args.get('since')
    until       = request.args.get('until')
    priority    = request.args.get('priority')
    lines       = request.args.get('lines')
    unit        = request.args.get('unit')
    
    if priority not in PRIORITIES:
        return Response(response        = json.dumps(BAD_PRIORITY, indent=4), 
                        content_type    = "application/json",
                        status          = 404)

    return Response(response        = json.dumps(SystemLogCollector(since, until, priority, lines, unit).collect(), indent=4), 
                    content_type    = "application/json",
                    status          = 200)



@blueprint_system.route('/system/shutdown', methods=['GET'])
def shutdown_pc():
    try:
        shutdown()
    except Exception as e:
        return Response(response        = str(e), 
                        status          = 500)
    else:
        return Response(response        = "OK", 
                        status          = 200)


@blueprint_system.route('/system/reboot', methods=['GET'])
def reboot_pc():
    try:
        reboot()
    except Exception as e:
        return Response(response        = str(e), 
                        status          = 500)
    else:
        return Response(response        = "OK", 
                        status          = 200) 
    
