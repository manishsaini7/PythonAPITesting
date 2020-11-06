from MyStoreAPITest.Src.configs.hosts_config import WOO_API_HOSTS
from MyStoreAPITest.Src.utilities.CredentialsUtility import CredentialsUtility
from woocommerce import API
import os

class WooAPIUtility(object):

    def __init__(self):

        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV','test')
        self.base_url = WOO_API_HOSTS[self.env]
        self.wcapi = API(
            url= self.base_url,
            consumer_keys = wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )

    def get(self, wc_endpoint, params=None, expected_status_code =200):
        self.rs

