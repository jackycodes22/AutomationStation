import os
from argparse import ArgumentParser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if os.getenv('BUILD_NUMBER'):
    BUILD_NUMBER = os.getenv('BUILD_NUMBER')
else:
    BUILD_NUMBER = 'local'


TEST_ENVIRONMENT = os.getenv('TEST_ENVIRONMENT', None)
API_ENDPOINT = os.getenv('API_ENDPOINT', None)

if TEST_ENVIRONMENT is None:
    parser = ArgumentParser()
    parser.add_argument("--env", action="store", default="prod", help="environment for tests")
    args, unknown_args = parser.parse_known_args()
    TEST_ENVIRONMENT = args.env

if API_ENDPOINT is None:
    parser = ArgumentParser()
    parser.add_argument("--api", action="store", default="oapi", help="api endpoint for tests")
    args, unknown_args = parser.parse_known_args()
    API_ENDPOINT = args.api

SCREENSHOTS = ROOT_DIR + '/results/'

if not os.path.exists(SCREENSHOTS):
    os.makedirs(SCREENSHOTS)

CONNECT_WEB_URL = f'https://connect.{TEST_ENVIRONMENT.lower()}.appetize-dev.com'
INTERACT_WEB_URL = f'https://mobile.{TEST_ENVIRONMENT.lower()}.appetize-dev.com'
OAPI_SCHEDULING_HOST_URL = f'https://api-gw.{TEST_ENVIRONMENT.lower()}.appetize-dev.com/scheduling-api/venues/'
SKIDATA_WEB_PORTAL_URL = "https://appetizesandbox.skidataus.com/FanSiteAdmin/Loyalty/MemberValue/ctl/LoadedValue_CP_List/mid/16547"

if TEST_ENVIRONMENT == 'prod':
    WEBSITE = 'https://rahulshettyacademy.com/AutomationPractice/'
elif TEST_ENVIRONMENT == 'sandbox':
    pass

