from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities

class productsHelper(object):
    def __init__(self):
        self.request_helper = requestsUtilities()

    def get_product_by_id(self, product_id):
        return self.request_helper.get(f"products/{product_id}")

    def call_create_products(self, payload):
        return self.request_helper.post('products', payload= payload , expected_status_code=201)

    def call_list_products(self, payload = None) :
        return self.request_helper.get('products', payload=payload)

    def call_update_regular_price(self, product_id, payload):
        return self.request_helper.put(f"products/{product_id}",payload=payload)