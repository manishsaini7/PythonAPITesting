from woocommerce import API
import pprint
wcapi = API(
    url="http://mystore.local/",
    consumer_key="ck_fa65e8d720797856ee09645727b77355bfcbfdf7",
    consumer_secret="cs_ceeae9e28df46d6fc1c53ac64728625ebe2b5d4d",
    version="wc/v3"
)

r = wcapi.get("products")
pprint.pprint(r.json())