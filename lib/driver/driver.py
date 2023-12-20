"""Base Driver Class for WebDriver"""
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class Driver:
    """Driver Class for Web Tests"""
    @staticmethod
    def get_webdriver_instance():
        """
        Create the driver instance
        :return:
        """

        options = webdriver.ChromeOptions()
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("use-fake-ui-for-media-stream")
        options.add_argument("window-size=375,812")
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        service = ChromeService(ChromeDriverManager().install(), caps=caps)
        driver = webdriver.Chrome(service=service, options=options)

        return driver
