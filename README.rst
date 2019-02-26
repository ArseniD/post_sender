post_sender
========

CLI for downloading and resending yMKT Abandoned Basket/ATG SignUp/Farfetch messages.

Preparing for Development
--------------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone https://github.com/ArseniD/post_sender.git``
3. Fetch development dependencies: ``make install``
4. (Optionally) build and install from source: ``python setup.py bdist_wheel && pip install --user dist/post_sender-0.1.4-py27-none-any.whl``

Usage
-------

Takes a email address, mail folder, massages date, asking about password and fetch all messages on specified date into 'attachments' folder.

**Fetching Example**:

::

        $ post_sender -e 'Arseni.Dudko@bur.com' -f 'Noreply/FailureYmkt' -d '30-May-2018' 


Read a given inventory file, parse the JSON/CSV, and add, remove or update systems users info based on file.

**Posting Example**:

::

        $ post_sender -s one_cart
        $ post_sender -s one_sign
        $ post_sender -s all_cart
        $ post_sender -s all_sign
        $ post_sender -s all_farfetch

Uninstall
---------

``pip uninstall post_sender``
