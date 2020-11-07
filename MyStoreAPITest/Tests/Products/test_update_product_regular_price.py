import pytest
import random
from MyStoreAPITest.Src.helpers.products_helper import productsHelper
from MyStoreAPITest.Src.dao.products_dao import ProductsDAO

@pytest.mark.tcid61
def test_update_regular_price():
    product_helper = productsHelper()
    # get random product
    rs_products = product_helper.call_list_products()
    products_id = [i['id'] for i in rs_products ]
    _product_id = random.choice(products_id)

    # make api call
    regular_price = "29.99"
    payload = {"regular_price": regular_price}
    rs_api = product_helper.call_update_regular_price(_product_id,payload)

    # verify response
    assert rs_api, f"Response api is empty"
    assert rs_api['price'] == regular_price, f"Price is not updated."\
    f"Expected regular price is {regular_price} but response price is 'rs_api['price']'."

    # verify in DB
    product_dao = ProductsDAO()
    product_db = product_dao.get_product_regular_price_by_id(_product_id)

    assert product_db[0]['meta_value'] == regular_price, f"Regular price in database is not updated"\
    f"Expected Regular price is {regular_price}. But retreived is 'product_db[0]['meta_value']'"
