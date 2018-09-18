# ether-api
Flask based API's to get data from psql database created using ether_sql

## Buidl status
Still very much in development

## Installation guide
Clone the library

```
git clone https://github.com/analyseether/ether-api.git
cd ether-api
```

Create a virtual environment and activate it:

```
virtualenv -p python3.6 venv
. venv/bin/activate
```


Install the required dependencies

```
pip install -r requirements.txt
```

## Setting up the database

Install postgresql as database:

```
sudo apt-get install postgresql
```

Create a new psql user, this prompts for a user password, use the same password in the `settings.py` file

```
sudo -u postgres createuser -s -P -e $USER
createdb ether_sql
```

You can either load the database using the [ether_sql](https://github.com/analyseether/ether_sql) library or load the database present in the test folder:

```
psql ether_sql < tests/ether_sql_test.sql
```


## Running the api's

Run the flask server

```
export FLASK_APP=api/api.py
flask run
```


Finally, test the API's

```
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

`̀``
