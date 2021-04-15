# -*- coding:utf-8 -*-

import requests_html
import time
import urllib3
from requests.adapters import HTTPAdapter
from requests_html import HTMLSession

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = HTMLSession()
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))
session.keep_alive = False
requests_html.user_agent()


def req_api():
    timestamp = time.time()
    url = 'http://screensavers-1252899349.file.myqcloud.com/cdn_bandwith_config.json?v={0}'.format(int(timestamp))
    # proxies = {'http': None, 'https': None}
    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    try:
        r = session.get(url=url, proxies=proxies, verify=False)
        print(r.text)
        cur = r.json()['pb']['cur']
        if cur > 1700:
            print('当前CDN-pb超载:%s' % cur)

    except Exception as e:
        print(e)


req_api()
