# -*- coding:utf-8 -*-
import os
import random
import re
import time

import allure
import pytest
import urllib3
import yagmail
from loguru import logger

from bdocr import domain

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def setup_method(self):
    logger.info('start')


def teardown_method(self):
    os.system('adb -s 022GPLDU39019379 shell input keyevent 26')
    logger.info('end')


def sent_mail(file, subject, message):
    receiver = "pytest@139.com"
    yag = yagmail.SMTP("b4hand@qq.com", 'okpykwvdqeczhage', 'smtp.qq.com')
    yag.send(
        to=receiver,
        subject=subject,
        contents=message,
        attachments=file,
    )
    logger.info('file = %s,subject=%s,message=%s' % (file, subject, message))


def devices():
    logger.info('00000000')
    result = os.popen('adb devices')
    context = result.read()
    if '022GPLDU39019379' in context:
        return True


devices = devices()
myskip = pytest.mark.skipif(devices != True, reason='skip赋值给变量，可多处调用')


@allure.feature('模块1,设备检测')
@pytest.mark.run(order=1)
def test_devices():
    logger.info('模块1,设备检测')
    if not devices:
        subject = 'no devices/emulators found'
        sent_mail(None, subject, None)
    assert devices == True


@allure.feature('模块3,重启')
@myskip
@pytest.mark.run(order=3)
def test_reboot():
    logger.info('模块3,重启')
    # week = datetime.datetime.today().weekday() + 1
    now_localtime = time.strftime("%H:%M:%S", time.localtime())  # 当前时间
    if now_localtime < "10:00:00":
        logger.info('reboot')
        os.system('adb reboot')
    else:
        logger.info('reboot only morning')


@allure.feature("模块2,执行任务")
@pytest.mark.run(order=2)
@myskip
class TestDd:
    @pytest.fixture()
    def file(self):
        logger.info('模块2,file')
        sleeptime = random.randint(0, 6) * 40
        logger.info('sleep %s' % sleeptime)
        time.sleep(sleeptime)
        file = r'F:\screenshot\screenshot.png'
        try:
            os.remove(file)
        except OSError as e:
            logger.info(e)
        os.system('adb -s 022GPLDU39019379 shell input keyevent 26')  # power
        time.sleep(2)
        os.system('adb -s 022GPLDU39019379 shell input keyevent 3')  # home
        time.sleep(1)
        os.system('adb -s 022GPLDU39019379 shell input keyevent 3')  # home
        time.sleep(2)
        logger.debug('DD-start')
        os.system('adb -s 022GPLDU39019379 shell monkey -p com.alibaba.android.rimet 1')  # start
        sleeptime = random.randint(25, 40)
        time.sleep(sleeptime)
        logger.debug('screenshot')
        os.system('adb -s 022GPLDU39019379 shell /system/bin/screencap -p /sdcard/screenshot.png')
        time.sleep(5)
        os.system('adb pull /sdcard/screenshot.png F:/screenshot')
        time.sleep(5)
        os.system('adb -s 022GPLDU39019379 shell am force-stop com.alibaba.android.rimet')
        os.system('adb -s 022GPLDU39019379 shell input keyevent 26')
        return file

    @pytest.fixture()
    def message(self, file):
        messages = domain(file)
        message = messages.replace('考勤打卡:', '').replace('钉钉', '').replace('设置工作状态Q搜索', '').replace('M工作通知:上海展盟网', '')
        return message

    @pytest.fixture()
    def subject(self, message):
        pattern = re.compile(r'\d{2}:\d{2}极速打卡')
        it = pattern.findall(message)

        pattern_on = re.compile(r'\d{2}:\d{2}.班打卡')
        it_on = pattern_on.findall(message)

        if it:
            subject = it[0]
        elif it_on:
            subject = it_on[0]
        elif '登录' in message:
            subject = 'error:未登录'
        else:
            subject = 'error:未知异常'
        return subject

    @allure.story('截图识别发邮件')
    @pytest.mark.flaky(reruns=2, reruns_delay=31)
    def test_todo(self, file, subject, message):
        sent_mail(file, subject, message)
        logger.info('subject=%s,message=%s' % (subject, message))
        assert '异常' not in subject


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./report --clean')
