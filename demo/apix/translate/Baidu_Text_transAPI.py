# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document


import json
import random
from hashlib import md5

# import requests
# 基本配置
from loguru import logger
from requests.adapters import HTTPAdapter
from requests_html import HTMLSession

# ua = UserAgent(use_cache_server=False)
# ua = UserAgent(verify_ssl=False)
session = HTMLSession()
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))
session.keep_alive = False

# Set your own appid/appkey.
appid = '20190508000295298'
appkey = 'SpZnEM6HliTHK1Mlp96I'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'en'
to_lang = 'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


salt = random.randint(32768, 65536)
sign = make_md5(appid + query + str(salt) + appkey)

# Build request
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

# Send request
r = session.post(url, params=payload, headers=headers, proxies=proxies, verify=False)
result = r.json()

# Show response
logger.info(json.dumps(result, indent=4, ensure_ascii=False))
