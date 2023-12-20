"""WebDriver Helper Methods"""
from lib.driver.driver import Driver

TIMEOUT = 30
IS_DISPLAYED_MAX_TIMEOUT = 25


class DriverUtil(Driver):
    """Driver Util class for webdriver helper methods"""

    def __init__(self):
        self._driver = Driver.get_webdriver_instance()

    def go_to(self, url):
        """Gets page"""
        self._driver.get(url)
