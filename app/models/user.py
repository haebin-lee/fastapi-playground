from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid

class User(Model):
  id = columns.UUID(primary_key=True, default=uuid.uuid4)
  name = columns.Text(required=True)
  email = columns.Text(required=True)
  