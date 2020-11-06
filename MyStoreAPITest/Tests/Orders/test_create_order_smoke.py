import pytest
from MyStoreAPITest.Src.dao.products_dao import ProductsDAO
from MyStoreAPITest.Src.helpers.ordersHelper import ordersHelper
from MyStoreAPITest.Src.helpers.customers_helper import CustomerHelper

@pytest.fixture(scope='module')
def my_order_smoke_setup():
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_product_from_db(1)

    product_id = rand_product[0]['ID']
    order_helper = ordersHelper()
    info = {'product_id': product_id,
            'order_helper': order_helper}
    return info

@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_order_smoke_setup):

    customer_id = 0
    product_id = my_order_smoke_setup['product_id']
    order_helper = my_order_smoke_setup['order_helper']
    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(add_args=info)

    expected_products = [{'product_id' : product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)

@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_order_smoke_setup):
    # get a product from db
    order_helper = my_order_smoke_setup['order_helper']
    customer_helper = CustomerHelper()
    product_id = my_order_smoke_setup['product_id']
    # make the call

    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
    "customer_id": customer_id
    }
    order_json = order_helper.create_order(add_args=info)

    # verify response

    expected_products = [{'product_id' : product_id}]
    order_helper.verify_order_is_created(order_json,customer_id, expected_products)