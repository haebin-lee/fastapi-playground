from cassandra.cluster import Cluster 
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from app.core.config import settings;
from app.models.user import User

def init_db():
  print('Initializing database...')
  cluster = Cluster(settings.SYLLADB_HOSTS)
  session = cluster.connect()
  session.execute(f"""
    CREATE KEYSPACE IF NOT EXISTS {settings.SYLLADB_KEYSPACE} 
    WITH REPLICATION = {{'class': 'SimpleStrategy', 'replication_factor': 1}}
  """)

  connection.setup(settings.SYLLADB_HOSTS, settings.SYLLADB_KEYSPACE, protocol_version=3)
  sync_table(User)
  print('Database initialized.')