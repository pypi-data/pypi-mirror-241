from typing import List


class LocalSaveModel(object):
    def __init__(self, key: str, time: int):
        self.key = key
        self.time = time


class OneTpModel(object):
    def __init__(self, key: str, reportTime: int, invokeTime: int):
        self.key = key
        self.reportTime = reportTime
        self.invokeTime = invokeTime


class TpItemModel(object):
    def __init__(self, k: str, e: str):
        self.k = k
        self.e = e


class TpModel(object):
    def __init__(self, t: int, h: str, a: str, l: List[TpItemModel]):
        self.t = t
        self.h = h
        self.a = a
        self.v = 629
        self.l = l


class TpkModel(object):
    """
    time_ip_key 为唯一key进行数据聚合，聚合粒度为5秒钟，以秒数5，0进行拆分找平
    """
    def __init__(self, tpk:str, t:int, h:str, k:str, e:str):
        self.tpk = tpk
        self.t = t
        self.h = h
        self.k = k
        self.e = e