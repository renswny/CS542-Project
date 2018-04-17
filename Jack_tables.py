import pymysql
from sqlalchemy import *
from sqlalchemy.orm import *

class CreateTables(object):
    """create tables"""
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:@localhost/Pokedex",
            echo=True)
        self.metadata = MetaData(self.engine)
        self.conn = self.engine.connect()

   “”“In the table pokemon, we don't need HP, attack, speed, have attributes. I just delete these attributes"
   def _pokemon(self):
        pokemon = Table(
            "pokemon", self.metadata,
            Column('pokedex', String(10), primary_key=true),
            Column('name', String(20), nullable=False),
            Column('height', REAL, nullable=False),
            Column('weight', REAL, nullable=False),
            Column('capture_rate', REAL, nullable=False),
            Column('classfication', String(40), nullable=False),
            Column('generation', Integer, nullable=False),
            Column('male_per', REAL, nullable=False),
        )
        return pokemon

    def _HP(self):
        have_hp = Table(
            "have_hp", self.metadata,
            Column('pokedex', String(10), primary_key=True, Foreignkey("pokemon.pokedex"), nullable=False)
            Column('hp', String(10), primary_key=True),
            Column('hp_percentile', Integer, nullable=False),
        )
        return hp
    def run(self):
        pokemon = self._pokemon()
        have_hp = self._HP()
        self.metadata.create_all(self.engine)

if __name__ == '__main__':
    test = CreateTables()
    test.run()
