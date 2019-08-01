import os
import logging

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Logging
LOG_FILE = "/tmp/home_dashboard.log"
LOG_SIZE = 1024*1024
LOG_LEVEL = logging.DEBUG
LOG_FILE_COUNT = 10

# WEATHER
# Monthly API Limit
W_MONTHLY_API_LIMIT = 10000
W_API_CACHE_LIMIT = 2592000/W_MONTHLY_API_LIMIT
W_BASE_URL = 'http://api.apixu.com'
W_VERSION = 'v1'
W_ZIPCODE = '06770'

# UI
DASHBOARD_NAME = 'SmartDash'
VERSION = '0.1'

# DEBUG
IS_MOCK = True
