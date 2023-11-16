from contextvars import ContextVar
import uuid
import hashlib

ctx_log_id = ContextVar('LOG_ID', default="None")


def setLogId(logId=None):
    """
    给线程设置log_id
    """
    if logId is None:
        logId = hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[0:32]
    ctx_log_id.set(logId)
    pass


def getLogId():
    return ctx_log_id.get()
