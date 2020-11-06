import json
import os
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities
from MyStoreAPITest.Src.dao.order_dao import OrderDAO
class ordersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.req_helper = requestsUtilities()

    def create_order(self, add_args=None):

        payload_template = os.path.join(self.cur_file_dir,'..','data','create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more info to payload, then update it
        if add_args:
            assert isinstance(add_args,dict), f"Parameter 'additional_args' must be a dictionary but found {type(add_args)}"
            payload.update(add_args)

        rs_api = self.req_helper.post('orders', payload=payload, expected_status_code=201)

        return rs_api

    @staticmethod
    def verify_order_is_created(order_json, exp_cust_id, exp_products):
        # verify response
        orders_dao = OrderDAO()
        assert order_json, f"Create order response is empty"
        assert order_json['customer_id'] == exp_cust_id, f"Create order with given customer id returned bad" \
                                                         f"Expected customer id = {exp_cust_id} but got '{order_json['customer_id']}'"

        assert len(order_json['line_items']) == len(exp_products), f"Expected only {len(exp_products)} item  in order but " \
                                                   f"found '{len(order_json['line_items'])}'" \
                                                   f"order id : {order_json['id']}."

        # verfy db
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)

        assert line_info, f"Create order, line not found in DB. Order id:{order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1, f"Expected 1 line item but found{len(line_items)}. Order id: {order_id}"

        # get list of products ids in the response
        api_products_ids = [i['product_id'] for i in order_json['line_items']]
        for product in exp_products:
            assert product['product_id'] in api_products_ids, f"Create order does not have at least 1 expected product in DB."\
            f"Product id: {product['product_id']}. Order id: {order_id}"

