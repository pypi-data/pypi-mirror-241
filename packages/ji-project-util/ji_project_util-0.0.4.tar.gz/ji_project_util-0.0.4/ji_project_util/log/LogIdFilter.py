import logging.config
from ji_project_util.log import LogIdManager


class MyFilter(logging.Filter):
    def __init__(self, name=None):
        self.name = name

    def filter(self, record):
        if self.name is None:
            allow = True
        else:
            allow = self.name not in record.msg
        if allow:
            # 添加logId
            logId = LogIdManager.getLogId()
            record.logId = logId
            # record.msg = 'logId: ' + logId + record.msg
        return allow
