=====
Usage
=====

To use SSLCommerz Client in a project::

	from sslcommerz_client import SSLCommerzClient

Initiate Client
===============

To initiate a client:

.. code-block:: python

    from sslcommerz_client import SSLCommerzClient

    client = SSLCommerzClient(
        store_id="YOUR_STORE_ID",
        store_passwd="YOUR_STORE_PASSWORD",
        sandbox=True // default false
    )

Initiate a Session
==================

To Initiate a Session:

.. code-block:: python

    post_data = {
        "total_amount": 100,
        "currency": "BDT",
        "tran_id": "221122",
        "product_category": "fashion",
        "success_url": "https://example.com",
        "fail_url": "https://example.com",
        "cancel_url": "https://example.com",
        "cus_name": "Jon Osterman",
        "cus_email": "jon@osterman.com",
        "shipping_method": "NO",
        "num_of_item": 1,
        "product_name": "Fancy Pants",
        "product_category": "Cloth",
        "product_profile": "physical-goods",
        "cus_add1": "Some Address",
        "cus_city": "Dhaka",
        "cus_country": "Bangladesh",
        "cus_phone": "01558221870",
    }

    resp = client.initiateSession(post_data)

It will return :code:`APIResponse` object with :code:`raw_data` - the actual response, :code:`status_code` for convenience, and an :code:`response` - a :code:`PaymentInitResponse`. One can use :code:`PaymentInitResponse` as is or create a dict or json from it. For more, consult :code:`pydantic` documentation.

Validate IPN
============

To validate an IPN response:

.. code-block:: python

    validation = client.validateIPN(data) // data: response data as a dict.

:code:`validation` will be an :code:`IPNValidationStatus` with validation status as :code:`status` and the response as :code:`IPNResponse`.
