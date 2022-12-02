import peewee as pw
from peewee import Model

db = pw.MySQLDatabase('politic',host='localhost', user='root', port=3306, password='1111')

class BaseModel(Model):
    class Meta:
        database = db

class Block(BaseModel):
    army = pw.IntegerField()
    name = pw.CharField(max_length=255)
    dateFinal = pw.DateField()
    numberParticipants = pw.IntegerField()
    id = pw.IntegerField(primary_key=True)

class BlockDocument(BaseModel):
    dateCreated = pw.DateField()
    nameDocument = pw.CharField(max_length=255)
    startingNum = pw.IntegerField()
    id = pw.ForeignKeyField(Block, backref="id")

class Country(BaseModel):
    history = pw.CharField(max_length=255)
    name = pw.CharField(max_length=255)
    GDP = pw.IntegerField()
    id = pw.CharField(primary_key=True)

class Industry(BaseModel):
    level = pw.IntegerField()
    id = pw.IntegerField(primary_key=True)

class Climate(BaseModel):
    climateZone = pw.IntegerField()
    id = pw.IntegerField(primary_key=True)

class Region(BaseModel):
    square = pw.IntegerField()
    name = pw.CharField(max_length=255)
    id_country = pw.ForeignKeyField(Country, backref="id_country")
    id_climate = pw.ForeignKeyField(Climate, backref="id_cl")
    id_prom = pw.ForeignKeyField(Industry, backref="id_ind")

class Conflict(BaseModel):
    name = pw.CharField(max_length=255)
    numParticipants = pw.IntegerField()
    id = pw.IntegerField(primary_key=True)

class countryConflictLinker(BaseModel):
    id = pw.ForeignKeyField(Country, backref="id")
    id2 = pw.ForeignKeyField(Conflict, backref="id")

class blockCountryLinker(BaseModel):
    id = pw.ForeignKeyField(Block, backref="id")
    id2 = pw.ForeignKeyField(Country, backref="id")

#db.init()
db.connect()
db.create_tables(
    [Block, Country, Region, BlockDocument, Industry, Climate, Conflict, countryConflictLinker,
    blockCountryLinker])