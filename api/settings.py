import os
import sys


class DefaultSettings():
    POSTGRES_USER = os.environ.get("USER")
    # POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'develop'
    # POSTGRES_PASSWORD = 'root'
    POSTGRES_DB = 'ether_sql'
    POSTGRES_HOST = 'localhost'
    POSTGRES_PORT = 5432
