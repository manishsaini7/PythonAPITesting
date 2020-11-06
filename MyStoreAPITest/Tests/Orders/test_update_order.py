from MyStoreAPITest.Src.helpers.ordersHelper import ordersHelper
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities
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
