# -*- coding:utf-8 -*-
import time
from datetime import datetime

import requests_html
import urllib3
from loguru import logger
from requests.adapters import HTTPAdapter
from requests_html import HTMLSession
from watchdog.events import *
from watchdog.observers import Observer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = HTMLSession()
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))
session.keep_alive = False
requests_html.user_agent()


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        # logger.info(datetime.now().strftime('%m-%d %H:%M:%S'), end='')
        if event.is_directory:
            logger.info("文件夹从{0}移动到{1}".format(event.src_path, event.dest_path))
        else:
            logger.info("文件从{0}移动到{1}".format(event.src_path, event.dest_path))

    def on_deleted(self, event):
        # logger.info(datetime.now().strftime('%m-%d %H:%M:%S'), end='')
        if event.is_directory:
            logger.info("删除文件夹:{0}".format(event.src_path))
        else:
            logger.info("删除文件:{0}".format(event.src_path))

    def on_created(self, event):
        # logger.info(datetime.now().strftime('%m-%d %H:%M:%S'), end='')
        if event.is_directory:
            logger.info("新建文件夹:\033[31;1m{0}\033[0m".format(event.src_path))
        else:
            logger.info("新建文件:\033[31;1m{0}\033[0m".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            # logger.info(datetime.now().strftime('%m-%d %H:%M:%S'), end='')
            logger.info("文件夹内容变动:{0}".format(event.src_path))
        # else:
        # logger.info("修改文件:{0}".format(event.src_path))


def req_api():
    time.sleep(20)
    timestamp = time.time()
    url = 'http://screensavers-1252899349.file.myqcloud.com/cdn_bandwith_config.json?v={0}'.format(round(timestamp))
    # proxies = {'http': None, 'https': None}
    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    try:
        r = session.get(url=url, proxies=proxies, verify=False)
        cur = r.json()['pb']['cur']
        if cur > 5600:
            logger.info(r.text)
            logger.info(datetime.now().strftime('%m-%d %H:%M:%S'), end='')
            logger.info('\033[31;1m当前CDN-pb超载:%s\033[0m' % cur)
    except Exception as e:
        logger.info(e)


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, r"C:\Users\Administrator\AppData\Roaming\ScreenSaver", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            req_api()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
