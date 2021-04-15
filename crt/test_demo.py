# -*- coding:utf-8 -*-
import urllib3
from loguru import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# test_ording.py
import pytest


# 上海-悠悠


@pytest.mark.run(order=6)
def test_foo():
    print("用例11111111111")
    assert True


@pytest.mark.run(order=1)
def test_bar():
    print("用例22222222222")
    assert True


@pytest.mark.run(order=3)
class TestDd:
    def setup_method(self):
        logger.debug('start')

    def teardown_method(self):
        logger.debug('end')

    # @pytest.mark.run(order=3)
    def test_g(self):
        print("用例333333333333333")
        assert True


if __name__ == '__main__':
    pytest.main(['-s', 'test_demo.py'])
