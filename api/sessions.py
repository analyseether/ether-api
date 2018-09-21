from sqlalchemy import MetaData, create_engine
from flask import Flask
from sqlalchemy.orm import sessionmaker

if __package__ is None or __package__ == '':
  from settings import DefaultSettings
else:
  from .settings import DefaultSettings

app = Flask(__name__)
app.config.from_object(DefaultSettings)

user= str(app.config['POSTGRES_USER'])
password= str(app.config['POSTGRES_PASSWORD'])
host=str(app.config['POSTGRES_HOST'])
port=str(app.config['POSTGRES_PORT'])
db=str(app.config['POSTGRES_DB'])

url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format(user, password, host, port, db)

class Session():
    def __init__(self):
        self.engine = create_engine(url, client_encoding='utf8', isolation_level="AUTOCOMMIT")

    def connect_to_psql(self):
        Ses = sessionmaker(bind=self.engine)
        return Ses()

    def get_table_object(self, name):
        META_DATA = MetaData(bind=self.engine, reflect=True)

        return META_DATA.tables[name]
