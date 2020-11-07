from MyStoreAPITest.Src.helpers.ordersHelper import ordersHelper
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities
from MyStoreAPITest.Src.utilities.genericUtilities import generate_random_string
import pytest

@pytest.mark.regression
@pytest.mark.parametrize("new_status",[pytest.param('cancelled', marks=pytest.mark.tcid55),
                                       pytest.param('completed', marks=pytest.mark.tcid56),
                                       pytest.param('on-hold', marks=pytest.mark.tcid57),
                                       ])

def test_update_order_status(new_status):
    req_helper = requestsUtilities()
    # create a new order
    order_json = ordersHelper().create_order()
    cur_status = order_json['status']

    assert cur_status != new_status, f"Current status of order is already {new_status}."\
                                     f"Unable to run test"

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    rs_update = req_helper.put(f'orders/{order_id}',payload=payload)

    # get order inforamtion
    new_order_info = req_helper.get(f'orders/{order_id}')

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status},"\
    f"but order is still '{new_order_info['status']}'"

@pytest.mark.order
@pytest.mark.regression
@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    new_status = 'abcdefgha'

    req_helper = requestsUtilities()
    # create a new order
    order_json = ordersHelper().create_order()

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    rs_update = req_helper.put(f'orders/{order_id}',payload=payload,expected_status_code=400)

    assert rs_update['code'] == 'rest_invalid_param',f"Update order status to random string did not have"\
    f"correct code in response. Expected: 'rest_invalid_param' Actual:{rs_update['code']}"

    assert rs_update['message'] == 'Invalid parameter(s): status', f"Update order status to random string did not have "\
                                                        f"correct message in response. Expected: 'Invalid parameter(s): status' Actual:{rs_update['message']}"

@pytest.mark.tcid59
def test_update_order_customer_note():
    req_helper = requestsUtilities()
    # create a new order
    order_json = ordersHelper().create_order()
    order_id = order_json['id']

    # update the customer note
    rand_string = generate_random_string(40)
    payload = {"customer_note": rand_string}
    rs_update = req_helper.put(f'orders/{order_id}',payload=payload)

    # get order inforamtion
    new_order_info = req_helper.get(f'orders/{order_id}')

    assert new_order_info['customer_note'] == rand_string, f"Update order's 'customer_note' field failed."\
    f"Expoected: {rand_string}, Actual : {new_order_info['customer_note']}"
