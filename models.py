from peewee import *
db = PostgresqlDatabase(
    'casino',  # Required by Peewee.
    user='myuser',  # Will be passed directly to psycopg2.
    password='mypass',  # Ditto.
    host='localhost')  # Ditto.



class Base(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = ('id', )


class User(Base):
    name = CharField(
        null=True
    )
    phone_number = CharField(
        max_length=20,
        null=True
    )
    email = CharField(
        null=True,
        max_length=255
    )
    message = CharField(
        null=True
    )

    class Meta:
        db_table = 'users'

