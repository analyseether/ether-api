import os
import sys


class DefaultSettings():
    POSTGRES_USER = os.environ.get("USER")
    POSTGRES_PASSWORD = 'develop'
    POSTGRES_DB = 'ether_sql'
    POSTGRES_HOST = 'localhost'
    POSTGRES_PORT = 5432
