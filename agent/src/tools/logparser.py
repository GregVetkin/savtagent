import subprocess
import json






def journalctl_logs(since=None, until=None, priority=None, lines=None, unit=None):
    command = ["sudo", "journalctl", "--no-pager", "--output=json"]
    
    if since:
        command.extend(["--since", since])
    if until:
        command.extend(["--until", until])
    if priority:
        command.extend(["-p", priority])
    if lines:
        command.extend(["-n", lines])
    if unit:
        command.extend(["-u", unit])
    
    try:
        result  = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logs    = [json.loads(line) for line in result.stdout.splitlines()]
        return logs
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}