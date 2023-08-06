import os
import pprint
from sslcommerz_client import SSLCommerzClient
from sslcommerz_client.dataclasses import ResponseStatusEnum

STORE_ID = os.environ.get("STORE_ID")
STORE_PASSWD = os.environ.get("STORE_PASSWD")


def test_main():
    client = SSLCommerzClient(
        store_id=STORE_ID, store_passwd=STORE_PASSWD, sandbox=True
    )
    pdata = {
        "total_amount": 100,
        "currency": "BDT",
        "tran_id": "221122",
        "product_category": "fashion",
        "success_url": "https://co.design",
        "fail_url": "https://co.design",
        "cancel_url": "https://co.design",
        "cus_name": "Utsob Roy",
        "cus_email": "roy@co.design",
        "shipping_method": "NO",
        "num_of_item": 1,
        "product_name": "Fancy Pants",
        "product_category": "Cloth",
        "product_profile": "physical-goods",
        "cus_add1": "bla",
        "cus_city": "Khulna",
        "cus_country": "Bangladesh",
        "cus_phone": "01558221870",
    }
    resp = client.initiateSession(pdata)
    assert resp.status_code == 200
    response = resp.response
    assert response.status == ResponseStatusEnum.SUCCESS
