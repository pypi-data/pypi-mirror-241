from threading import Thread, get_ident
from ji_project_util.monitor import MonitorModel


class CustomLocal(object):
    """自定义local对象，基于面向对象"""

    def __init__(self):
        # self.storage = {}  # 执行此句代码的时候会先触发__setattr__方法
        # 为了避免报错：RecursionError: maximum recursion depth exceeded while calling a Python object
        # 需要先把storage创建出来，所以调用父类的__setattr__方法
        super(CustomLocal, self).__setattr__("storage", {})

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][key] = value
        else:
            self.storage[ident] = {key: value}  # 执行此句的时候又会触发__setattr__方法，所有就进入了死循环

    def __getattr__(self, item):
        ident = get_ident()
        return self.storage[ident][item]


local = CustomLocal()


def putVal(value: MonitorModel.LocalSaveModel):
    local.val = value


def getVal():
    return local.val
