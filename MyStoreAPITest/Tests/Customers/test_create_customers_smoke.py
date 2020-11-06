import pytest
import logging as logger
from MyStoreAPITest.Src.utilities.genericUtilities import generate_random_email_and_password
from MyStoreAPITest.Src.helpers.customers_helper import CustomerHelper
from MyStoreAPITest.Src.dao.customers_dao import CustomersDAO
from MyStoreAPITest.Src.utilities.requestsUtilities import requestsUtilities

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Create New customer with email and password")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    payload = {'email':email, 'password':password}

    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '',f"Create customer api returned value for first name" \
                                            f"but it should be empty."

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create Customer response "id" not same as "ID" in Databae.'\
                                f'Email:{email}'

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    #get existing email from db
    cust_dao = CustomersDAO()
    existing_cust =cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    #Call the api
    req_helper = requestsUtilities()
    payload = {"email":existing_email,"password":"Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists',\
    f"Create customer with existing user error 'code' is not correct ."\
    f"Expected: 'registration-error-email-exists',"\
    f"Actual:{cust_api_info['code']}"