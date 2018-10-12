Introduction
============

ether-api
~~~~~~~~~~~~~~~~

ether_api is a Flask API to get data from psql database created using ether_sql.

It is maintained by `Analyse Ether <https://www.analyseether.com/>`_, with the goal of making Ethereum data easily available to everyone. This API can be used to fetch Ethereum Blockchain data scraped using ether_sql for performing data analysis.

It is written in Python 3.6+, uses SqlAlchemy <http://docs.sqlalchemy.org/en/latest/>`_ to connect to a postgressql database and uses Flask and simplejson to serve the JSON to the requesting source.

Goals
-----

The main focus is to make Ethereum data easily available to everyone, while serving as a backbone for:

* Open block explorers (coming soon...)
* `Data analysis platforms <https://www.analyseether.com/>`_

Build Status
------------
This is currently in very alpha stage, and not recommended for production use until it has received sufficient testing.

Follow along the `Installation <installation.html>`_ to install the basic setup and checkout the `Guides <./guides/index.html>`_ to understand the process.
