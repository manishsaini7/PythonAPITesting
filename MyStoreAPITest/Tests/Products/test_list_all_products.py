import pytest
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities
from MyStoreAPITest.Src.dao.products_dao import ProductsDAO
from MyStoreAPITest.Src.helpers.products_helper import productsHelper
import logging as logger


@pytest.mark.tcid24
def test_list_all_products_by_id():
    req_helper = requestsUtilities()
    rs_api = req_helper.get('products')
    logger.debug("getting all products")

    assert rs_api ,f"Response of the Products should not be empty"

@pytest.mark.tcid25
def test_get_product_by_id():

    # get a product (test data) from database
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    product_helper = productsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']
    #make a call

    assert db_name == api_name, f"Get product by id returned wrong product. Id: {rand_product_id}"\
    f"Db name: {db_name}, Api name: {api_name}"
    #verify the response


