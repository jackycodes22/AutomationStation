"""
Base Page
"""
from lib.driver.driver_util import DriverUtil


class BasePage(DriverUtil):
    """
    Base Page Class
    """

    def __init__(self, url):
        super().__init__()
        self._url = url
