import subprocess
import json
from models             import BaseCollector
from typing             import List



class SystemLogCollector(BaseCollector):
    def __init__(self, since=None, until=None, priority=None, lines=None, unit=None, json=True):
        self._since     = since
        self._until     = until
        self._priority  = priority
        self._lines     = lines
        self._unit      = unit
        self._json      = json


    def _journalctl_logs(self):
        command = ["sudo", "journalctl", "--no-pager"]
        
        if self._json:
            command.extend(["--output=json"])
        if self._since:
            command.extend(["--since", self._since])
        if self._until:
            command.extend(["--until", self._until])
        if self._priority:
            command.extend(["-p", self._priority])
        if self._lines:
            command.extend(["-n", self._lines])
        if self._unit:
            command.extend(["-u", self._unit])
        
        try:
            result  = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            if self._json:
                logs    = [json.loads(line) for line in result.stdout.splitlines()]
                return logs
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(str(e))
        
    def collect(self):
        return self._journalctl_logs()