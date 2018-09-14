import psycopg2
from flask import Flask
from settings import DefaultSettings

app = Flask(__name__)
app.config.from_object('settings.DefaultSettings')

class Session():

    def connect_to_psql():
        conn = psycopg2.connect(dbname=app.config['POSTGRES_DB'], user=app.config['POSTGRES_USER'], password=app.config['POSTGRES_PASSWORD'])
        return conn.cursor()
