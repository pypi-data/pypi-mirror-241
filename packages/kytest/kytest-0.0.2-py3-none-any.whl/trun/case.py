"""
@Author: kang.yang
@Date: 2023/10/26 09:48
"""
import time
from typing import Union

from trun.core.android.driver import AdrDriver
from trun.core.ios.driver import IosDriver
from trun.core.web.driver import WebDriver
from trun.core.api.request import HttpReq

from trun.utils.config import config
from trun.utils.log import logger


class TestCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """

    driver: Union[AdrDriver, IosDriver, WebDriver] = None

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()

        platform = config.get_common("platform")
        if platform == "android":
            device_id = config.get_app("device_id")
            pkg_name = config.get_app("pkg_name")
            self.driver = AdrDriver(device_id, pkg_name)
        elif platform == "ios":
            device_id = config.get_app("device_id")
            pkg_name = config.get_app("pkg_name")
            self.driver = IosDriver(device_id, pkg_name)
        elif platform == "web":
            browserName = config.get_web("browser_name")
            headless = config.get_web("headless")
            self.driver = WebDriver(browserName=browserName, headless=headless)

        if platform in ["android", "ios"]:
            if config.get_app("auto_start") is True:
                self.driver.start_app()

        self.start()

    def teardown_method(self):
        self.end()

        platform = config.get_common("platform")
        if platform in ["android", "ios"]:
            if config.get_app("auto_start") is True:
                self.driver.stop_app()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)

    def screenshot(self, name: str):
        """截图"""
        self.driver.screenshot(name)

