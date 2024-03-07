from .models import *
from table import Table
from table.columns import Column

class PersonTable(Table):
    # id = Column(field='id')
    name = Column(field='name')
    email=Column(field='email')
    status = Column(field='status')
    class Meta:
        model = Person