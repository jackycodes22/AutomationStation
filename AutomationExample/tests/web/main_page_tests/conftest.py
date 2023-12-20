"""Universal fixtures"""
import pytest as pytest

import config
from lib.driver.driver import Driver


@pytest.fixture(scope='function')
def launch(request):
    """Login to venue """
    web_driver = Driver()
    driver = web_driver.get_webdriver_instance()

    def quit_driver():
        try:
            if request.node.rep_call.failed or request.node.rep_setup.failed:
                test_name = request.node.nodeid.replace("/", ".")
                file_name = "{}/{}.png".format(config.SCREENSHOTS, test_name)
                driver.save_screenshot(file_name)
        except AttributeError:
            test_name = request.node.nodeid
            print("{} missing rep_call or rep_setup. Unable to create screenshot".format(test_name))

        driver.quit()

    request.addfinalizer(quit_driver)

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
