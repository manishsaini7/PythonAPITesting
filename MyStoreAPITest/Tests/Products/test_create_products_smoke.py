import pytest
from MyStoreAPITest.Src.utilities.genericUtilities import generate_random_string
from MyStoreAPITest.Src.helpers.products_helper import productsHelper
from MyStoreAPITest.Src.dao.products_dao import ProductsDAO

@pytest.mark.products
@pytest.mark.tcid26
def test_create_1_simple_product():

    #generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    prod_rs = productsHelper().call_create_products(payload)

    #verify the respopnse is not empty
    assert prod_rs,f"Create product api response is empty. Payload: {payload}"
    assert prod_rs['name'] == payload['name'], f"Create product api call response has"\
    f"unexpected name. Expected:{payload['name']}, Actual: {prod_rs['name']}"

    #verify the product exist in db
    product_id = prod_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product , title in db doest not match"\
    f"title in api. DB:{db_product[0]['post_title']}, API:{payload['name']}"


