import json
import os
import socket
from functools import wraps
from ji_project_util.log import LogManager
from ji_project_util.monitor import MonitorThreadLocal, MonitorModel
import threading
import multiprocessing
import time
import datetime

"""
做监控使用
"""
MonitorLogger = LogManager.log.logger("monitor")


def nowInt():
    return int(datetime.datetime.now().timestamp() * 1000)


def nowIntSeconds():
    return int(datetime.datetime.now().timestamp())


def getReportTime(timeSecond):
    """
    5秒钟上报一次的标准
    将时间向上取，5,0为界限。23947237秒->23947240秒
    :param timeSecond:
    :return:
    """
    return int(timeSecond / 5) * 5 + 5 if timeSecond % 5 > 0 else timeSecond + 5


def aggregate(tpAppName: str, tpQueue):
    """
    将数据进行信息聚合，写入内存中，如果达到了写入条件，写入到日志文件中
    内存结构 Dict<time,Dict<key,Dict<invoke,times>>>
    字典<上报时间,字典<tpKey,字典<执行时间，时间次数>>>
    :return:
    """
    thisTime = nowIntSeconds()
    lastKey = getReportTime(thisTime)
    reportDict = ReportDict(tpAppName)
    while True:
        # TpModel.OneTpModel()  key: str, reportTime: int, invokeTime: int\
        # x = tpQueue.qsize()
        # print("prepare to queue,empty:" + str(tpQueue.empty()))
        # print(str(tpQueue))

        # print("get one")
        now = nowIntSeconds()
        readyReportTime = getReportTime(now)

        if tpQueue.empty():
            if readyReportTime > lastKey:
                # 开始进行上报
                keys = list(reportDict.keys())
                for key in keys:
                    if key < readyReportTime:
                        # report实际操作，使用log
                        reportDict.reportBesidesPop(key)
                        # reportDict.pop(key)
                lastKey = reportDict.getMinKey(readyReportTime)
            else:
                time.sleep(3)
            continue
        oneTpModel = tpQueue.get()

        if oneTpModel is not None:
            # 开始进行report计算
            reportTime = oneTpModel.reportTime / 1000
            readyReportTime = getReportTime(reportTime)
            reportDict.mergeAggregate(readyReportTime, oneTpModel)

        if readyReportTime > lastKey:
            # 开始进行上报
            keys = list(reportDict.keys())
            for key in keys:
                if key < readyReportTime:
                    # report实际操作，使用log
                    reportDict.reportBesidesPop(key)
            lastKey = reportDict.getMinKey(readyReportTime)
    pass


class ReportDict(object):
    """
    上报字典 类。
    # dict内容：tpk time ip key TpkModel
    # 格式：{time1:{"key1":"-1,0","key2":""},time2:{"key1":"","key2":""}}
    # {time1:{"key1":{"invokeTime":1,"invokeTime":2}},"key2":{}},time2:{"key1":{...},"key2":{...}}}
    reportObj = {}
    """

    def __init__(self, tpAppName: str):
        self.dict = {}
        self.hostName = socket.gethostbyname(socket.gethostname())
        self.tpAppName = tpAppName

    def mergeAggregate(self, readyReportTime: int, oneTpModel: MonitorModel.OneTpModel):
        if readyReportTime not in self.dict:
            putObj = {oneTpModel.key: {oneTpModel.invokeTime: 1}}
            self.dict[readyReportTime] = putObj
        else:
            thisObj = self.dict[readyReportTime]
            if oneTpModel.key not in thisObj:
                thisObj[oneTpModel.key] = {oneTpModel.invokeTime: 1}
                self.dict[readyReportTime] = thisObj
            else:
                valObj = thisObj[oneTpModel.key]
                if oneTpModel.invokeTime not in valObj:
                    valObj[oneTpModel.invokeTime] = 1
                else:
                    valObj[oneTpModel.invokeTime] = valObj[oneTpModel.invokeTime] + 1
                thisObj[oneTpModel.key] = valObj
                self.dict[readyReportTime] = thisObj

        pass

    def keys(self):
        return self.dict.keys()

    def pop(self, key: int):
        self.dict.pop(key)

    def reportBesidesPop(self, key: int):
        """
        将key的内容进行上报,格式
        @{"t":1644750400,"h":"10.170.240.32","a":"jdos_app1","v":629,"l":[{"k":"tp_key1","e":"1,1,2,2"},{"k":"tp_key2","e":"-1,1,0,1"}]}
        :param key:
        :return:
        """
        if key not in self.dict:
            return True
        localDict = self.dict[key]
        tpItems = []
        for tpKey in localDict.keys():
            tpItemObj = localDict[tpKey]
            tpItem = MonitorModel.TpItemModel(tpKey, None)
            val = ""
            for itemKey in tpItemObj.keys():
                val = val + str(itemKey) + ","
                val = val + str(tpItemObj[itemKey]) + ","
            tpItem.e = val[0: len(val) - 1]
            tpItems.append(tpItem)
            pass
        tpModel = MonitorModel.TpModel(key, self.hostName, self.tpAppName, tpItems)
        MonitorLogger.info("@" + json.dumps(tpModel, ensure_ascii=False, cls=MyEncoder))
        self.pop(key)
        return True

    def getMinKey(self, readyReportTime: int):
        if len(self.dict) > 0:
            return min(self.dict.keys())
        return readyReportTime

    pass


class MyEncoder(json.JSONEncoder):
    """
    除了基础类型，其他类型使用内部的__dict__进行转化，
    datatime专门转化
    """
    def default(self, obj):
        from _typeshed import NoneType
        if isinstance(obj, dict):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, list):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, tuple):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, str):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, int):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, float):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, bool):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, NoneType):
            return json.JSONEncoder.default(self, obj)
        elif isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return obj.__dict__


class TpProducer(object):
    def __init__(self, tpQueue):
        self.q = tpQueue

    def setQ(self, tpQueue):
        print("setQ:" + str(tpQueue))
        self.q = tpQueue

    def tpBegin(self, key: str):
        """
        标记tp开始的位置, 使用tpBegin要求线程不能变
        从threadLocal中设定好beginTime
        :param key:
        :return:
        """
        if self.q is None:
            return None
        timeBegin = nowInt()
        localSaveModel = MonitorModel.LocalSaveModel(key, timeBegin)
        MonitorThreadLocal.putVal(localSaveModel)
        return localSaveModel

    def tpEnd(self, localSaveModel: MonitorModel.LocalSaveModel):
        """
        标记tp结束了，使用tpEnd要求线程不能变
        :param localSaveModel:
        :return:
        """
        if self.q is None:
            return None
        storageSaveModel = MonitorThreadLocal.getVal()
        if storageSaveModel is None:
            return None
        if storageSaveModel.key != localSaveModel.key:
            return None

        timeEnd = nowInt()
        # 将结果写入到reportObj里面
        invokeTime = timeEnd - storageSaveModel.time
        obj = MonitorModel.OneTpModel(localSaveModel.key, timeEnd, invokeTime)
        # 如果tp计算线程打开，再向里面queue里面推入
        if os.environ.get('OPEN_MONITOR', "True") == "True":
            self.q.put(obj)
            print("queue-s:" + str(self.q))
            # print("queue-size:"+str(self.q.qsize))
        pass

    def tpFailed(self, localSaveModel: MonitorModel.LocalSaveModel):
        """
        标记tp执行失败了，使用tpFailed要求线程不能变
        :param localSaveModel:
        :return:
        """
        if self.q is None:
            return None
        # 将失败的结果写入到reportObj里面
        storageSaveModel = MonitorThreadLocal.getVal()
        if storageSaveModel is None:
            return None
        if storageSaveModel.key != localSaveModel.key:
            return None
        timeEnd = nowInt()
        obj = MonitorModel.OneTpModel(localSaveModel.key, timeEnd, -1)
        # 如果tp计算线程打开，再向里面queue里面推入
        if os.environ.get('OPEN_MONITOR', "True") == "True":
            self.q.put(obj)
            print("queue-size:" + str(self.q.qsize()))
        pass


tpProducer = TpProducer(None)


def tp(key: str):
    """
    tp入口，被调用后进行上报使用
    :param key:
    :return:
    """

    def try_catch(func):
        @wraps(func)
        def _tp(*args, **kwargs):
            localSaveModel = None
            try:
                localSaveModel = tpProducer.tpBegin(key)
                result = func(*args, **kwargs)
                tpProducer.tpEnd(localSaveModel)
                return result
            except Exception as e:
                tpProducer.tpFailed(localSaveModel)
                raise e

        return _tp

    return try_catch


def begin(appName: str):
    """
    开启tp的monitor写入
    开启聚合线程，聚合所有tp-key的耗时
    开启写入线程，5秒的维度来写一次数据到日志文件
    :return:
    """
    # 开启聚合线程 多线程版本后面再写
    log_queue = multiprocessing.Queue()
    tpProducer.setQ(log_queue)
    aggr = threading.Thread(target=aggregate, args=(appName, log_queue,))
    aggr.start()
    # x = threading.Thread(target=testProducer, args=())
    # x.start()
    pass
