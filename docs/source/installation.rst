Installation Guide
==================

Linux dependencies
------------------

Install postgresql as database::

  $ sudo apt-get install postgresql

Install python3 headers::

  $ sudo apt-get install python3-pip
  $ sudo apt-get install python3.6-dev

Install redis server::

  $ sudo apt-get install redis-server

Install Rabbit-MQ server::

  $ sudo apt-get install rabbitmq-server


Python dependencies
-------------------

Clone the **ether-api** library::

  $ git clone https://github.com/analyseether/ether-api.git
  $ cd ether-api

Create and activate a virtual environment::

  $ virtualenv envname
  $ source envname\bin\activate

Install python libraries::

  $ pip install -r requirements.txt


Database setup
--------------

Create a new psql user, this prompts for a user password, use the same password in the variable :code:`POSTGRES_PASSWORD` of the **settings.py** file::

  $ sudo -u postgres createuser -s -P -e $USER


Create the ether_sql database in psql::

    $ createdb ether_sql

You can either load the database using the ether_sql library or load the database present in the test folder::
	psql ether_sql < tests/ether_sql_test.sql


Running the API
---------------

Run the flask server::

	export FLASK_APP=api/api.py
	flask run

Finally, test the API's::

	$ curl -i http://127.0.0.1:5000/v1.0/current_blockNumber/
	HTTP/1.0 200 OK
	Content-Type: text/html; charset=utf-8
	Content-Length: 39
	Server: Werkzeug/0.14.1 Python/3.6.6
	Date: Tue, 18 Sep 2018 11:46:58 GMT

	[
	  {
	    "block_number": 5000100
	  }
	]