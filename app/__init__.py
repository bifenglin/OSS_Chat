import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_socketio import SocketIO
from app.index import MyIndexView
from .engine import LlamaQueryEngine

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
socketio = SocketIO(app)
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView)
llama_query_engine = LlamaQueryEngine()
llama_query_engine.load_doc_from_csv(csv_path="app/data/readme_data.csv", is_persist=True, persist_dir="app/data/persist", max_docs=2000)

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
