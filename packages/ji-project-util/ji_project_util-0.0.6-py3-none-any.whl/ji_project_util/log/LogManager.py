import os
import io
from string import Template

import yaml
import logging.config
import multiprocessing
import threading

que = multiprocessing.Queue()


def logger_thread(q):
    while True:
        record = q.get()
        if record is None:
            break
        logger = logging.getLogger(record.name)
        logger.handle(record)


class Logger(object):
    def __init__(self):
        initData = {
            "buzlog": "/Users/jixiangkun/D/pyconfig/buz.log",
            "tplog": "/Users/jixiangkun/D/pyconfig/tp.log"
        }
        MY_DIR = os.path.dirname(os.path.abspath(__file__))
        BASE_DIR = MY_DIR.split("ji_project_util")[0]
        if os.path.exists(BASE_DIR + "config.yaml"):
            with io.open(os.path.abspath(BASE_DIR + "config.yaml"), encoding='utf-8') as configFile:
                initData = yaml.safe_load(configFile)
        configFilePath = os.environ.get("CONFIG_FILE_PATH")
        if configFilePath is not None and os.path.exists(configFilePath):
            with io.open(configFilePath, encoding='utf-8') as configFile:
                initData = yaml.safe_load(configFile)

        with io.open(os.path.abspath(BASE_DIR + "ji_project_util/log/logging.yaml"), encoding='utf-8') as f:
            re = Template(f.read()).substitute(initData)
            config = yaml.safe_load(re)
            logging.config.dictConfig(config)

        qh = logging.handlers.QueueHandler(que)
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        root.addHandler(qh)

        # que = multiprocessing.Queue()
        lp = threading.Thread(target=logger_thread, args=(que,))
        lp.start()
        # lp.join()

    def logger(self, name: str):
        logger = logging.getLogger(name)
        return logger


log = Logger()
