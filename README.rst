post_sender
========

CLI for downloading and resending yMKT Abandoned Basket/ATG SignUp/Farfetch messages.

Preparing for Development
--------------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone https://github.com/ArseniD/post_sender.git``
3. Fetch development dependencies: ``make install``
4. (Optionally) build and install from source: ``python setup.py bdist_wheel && sudo pip install dist/post_sender-0.1.4-py27-none-any.whl``

Usage
-------

Takes a email address, mail folder, massages date, asking about password and fetch all messages on specified date into 'attachments' folder.


Fetching Example w/ mail address, mail folder, messages date:

::

        $ post_sender -e 'Arseni.Dudko@bur.com' -f 'Noreply/FailureYmkt' -d '30-May-2018' 

Read a given inventory file, parse the JSON/CSV, and add, remove or update systems users info based on file.

Posting Example w/ messages path:

::

        $ post_sender -s one_cart
        $ post_sender -s one_sign
        $ post_sender -s all_cart
        $ post_sender -s all_sign
        $ post_sender -s all_farfetch

Example messages JSON file:

::

        {
          "UserName": "CASTRN_SERV",
          "SourceSystemType": "ATG",
          "SourceSystemId": "Development",
          "ProductCategories": [{
            "Id": "catXXXXX",
            "HierarchyId": "ATG",
            "Name": "catXXXX",
            "Description": "Crossbody Bags",
            "ZZ_URL": "https://us.bur.com/mens-bags/crossbody-bags/",
            "Language": "EN"
          }],
          "Products": [{
            "IdOrigin": "EXTERNAL_01",
            "Id": "123123123",
            "Name": "London Check Crossbody Bag",
            "Description": "<ul><li>Crossbody bag in London check</li><li>Foldover top, internal zip pocket</li><li>Webbed canvas shoulder strap</li><li>Back zip pocket</li></ul>",
            "ImageUrl": "https://assets.bur.com/is/image/Burltd/9d25596b7519639078ba8d7b1d1a9ea80058953d.jpg?$BBY_V2_SL_4X3$",
            "NavigationURL": "https://us.bur.com/london-check-crossbody-bag-p39962151",
            "CategoryId": "catXXXXX",
            "HierarchyId": "ATG",
            "ZZ_BRAND": null,
            "Language": "EN"
          }],
          "Contacts": [{
            "Id": "123123123123",
            "IdOrigin": "ZATG",
            "FirstName": "Dodo",
            "LastName": "Toto",
            "Timestamp": "/Date(1487253102000)/",
            "LanguageDescription": "EN",
            "CountryDescription": "US",
            "EMailAddress": "dodo.toto@bur.com",
            "GenderDescription": null,
            "TitleDescription": "Miss",
            "IsConsumer": false,
            "ZZ_REGISTRATN_TIMESTAMP": "/Date(1450982406000)/",
            "ZZ_LEAD_CREATE_SOURCE": "ATGAB",
            "ZZ_EXTERNAL_SOURCE": "ATGAB"
          }],
          "Interactions": [{
            "ContactId": "123123123123",
            "ContactIdOrigin": "ZATG",
            "CommunicationMedium": "ONLINE_SHOP",
            "InteractionType": "SHOP_CART_ABANDONED",
            "SourceObjectAdditionalId": "o777777777",
            "Timestamp": "/Date(1527681906000)/",
            "Currency": "USD",
            "Amount": "750",
            "StartingPointUrl": "https://us.bur.com/abandoned-cart/xLIOgBgPij0IESQo9In4bw==",
            "ZZ_PRICE_LIST_LOCALE": "en_US_USD",
            "ZZ_DELIVERY_TO_STORE": false,
            "ZZ_PR_TAX_TOTAL": "0",
            "ZZ_PR_SHIPPING_TOTAL": "0",
            "ZZ_SH_FIRST_NAME": "Dodo",
            "ZZ_SH_LAST_NAME": "Toto",
            "ZZ_SH_ADDR_LINE1": "3rd Floor, HFH1, 3/14E",
            "ZZ_SH_ADDR_LINE2": "Horsefe",
            "ZZ_SH_CITY": "London",
            "ZZ_SH_REGION_DESCRIPTION": "London",
            "ZZ_SH_POSTAL_CODE": "SW999x 2000AW",
            "ZZ_SH_COUNTRY_DESCRIPTION": "GB",
            "ZZ_SH_STORE_NAME": null,
            "ZZ_SH_PHONE": "123123123123",
            "ZZ_SHIPPING_METHOD_NAME": "US_UPS_STANDARD_GROUND",
            "ZZ_GIFT_MESSAGE": null,
            "ZZ_INTERACTION_PRODUCT_COUNT": 1,
            "ZZ_SIGN_UP_CODE": "ATGAB",
            "ZZ_PR_SHIPPING_TOTAL_FTD": "$0.00",
            "ZZ_AMOUNT_FTD": "$750.00",
            "ZZ_SHIPPING_AMOUNT_FTD": "$0.00",
            "ZZ_PR_TAX_TOTAL_FTD": "$0.00",
            "Products": [{
              "SourceSystemId": "ATG",
              "ItemType": "EXTERNAL_01",
              "ItemId": "123123123",
              "RecommendationModelTypeID": "ci123123123",
              "Quantity": "1",
              "Name": "London Check Crossbody Bag",
              "Description": "<ul><li>Crossbody bag in London check</li><li>Foldover top, internal zip pocket</li><li>Webbed canvas shoulder strap</li",
              "ImageUrl": "https://assets.bur.com/is/image/Burbltd/9d25596b7519639078ba8d7b1d1a9ea80058953d.jpg?$BBY_V2_SL_4X3$",
              "NavigationURL": "https://us.bur.com/london-check-crossbody-bag-p39962151",
              "ZZ_BRAND": null,
              "ZZ_LANGUAGE": "EN",
              "ZZ_COLOUR": "Navy/black",
              "ZZ_SIZE": null,
              "ZZ_MONOGRAM_TEXT": null,
              "ZZ_LIST_PRICE": "750",
              "Amount": "750",
              "ZZ_LIST_PRICE_FTD": "$750.00",
              "ZZ_AMOUNT_FTD": "$750.00"
            }]
          }]
        }
