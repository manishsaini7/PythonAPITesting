import pytest
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities
import logging as logger

@pytest.mark.customers
@pytest.mark.tcid30
def test_test_get_all_customers():
    req_helper = requestsUtilities()
    rs_api = req_helper.get('customers')
    logger.debug(f"Response of list all: {rs_api}")

    assert rs_api, f"Response of list all customers is empty."