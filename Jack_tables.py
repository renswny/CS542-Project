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

    def _ability(self):
        ability = Table(
            "ability", self.metadata,
            Column('aid', String(10), primary_key=True),
            Column('ability', String(20), nullable=False),
        )
        return ability

    def _attack(self):
        attack = Table(
            "attack", self.metadata,
            Column('attack', String(10), primary_key=True),
            Column('attack_percentile', Integer, nullable=False),
        )
        return attack

    def _defense(self):
        defense = Table(
            "defense", self.metadata,
            Column('defense', String(10), primary_key=True),
            Column('defense_percentile', INTEGER, nullable=False),
        )
        return defense

    def _HP(self):
        hp = Table(
            "hp", self.metadata,
            Column('hp', String(10), primary_key=True),
            Column('hp_percentile', Integer, nullable=False),
        )
        return hp

    def _speed(self):
        speed = Table(
            "speed", self.metadata,
            Column('speed', String(10), primary_key=True),
            Column('speed_percentile', Integer, nullable=False),
        )
        return speed

    def _type(self):
        type = Table(
            "type", self.metadata,
            Column('tid', String(10), primary_key=True),
            Column('type', String(20), nullable=False),
        )
        return type

    def _against(self):
        against = Table(
            "against", self.metadata,
            Column('tid_strong_against', String(10), primary_key=True),
            Column('tid_weak_against', String(10), primary_key=True),
        )
        return against

    def _pokemon(self):
        pokemon = Table(
            "pokemon", self.metadata,
            Column('pokedex', String(10), primary_key=true),
            Column('name', String(20), nullable=False),
            Column('height', REAL, nullable=False),
            Column('weight', REAL, nullable=False),
            Column('capture_rate', REAL, nullable=False),
            Column('classfication', String(80), nullable=False),
            Column('generation', Integer, nullable=False),
            Column('male_per', REAL, nullable=False),
            Column('hp', String(10), ForeignKey("hp.hp"), nullable=False),
            Column('attack', String(10), ForeignKey("attack.attack"), nullable=False),
            Column('defense', String(10), ForeignKey("defense.defense"), nullable=False),
            Column('speed', String(10), ForeignKey("speed.speed"), nullable=False),
        )
        return pokemon

    def _evolve(self):
        evolve = Table(
            "evolve", self.metadata,
            Column('pokedex_from', String(10), primary_key=True),
            Column('pokedex_to', String(10), primary_key=True),
        )
        return evolve

    def _betype(self):
        betype = Table(
            "betype", self.metadata,
            Column('pokedex', String(10), primary_key=True),
            Column('tid', String(10), primary_key=True)
        )
        return betype

    def _capable(self):
        capable = Table(
            "capable", self.metadata,
            Column('pokedex', String(10), primary_key=True),
            Column('aid', String(10), primary_key=True)
        )
        return capable

    def run(self):
        ability = self._ability()
        attack = self._attack()
        defense = self._defense()
        hp = self._HP()
        speed = self._speed()
        poketype = self._type()
        against = self._against()
        pokemon = self._pokemon()
        evolve = self._evolve()
        betype = self._betype()
        capable = self._capable()
        self.metadata.create_all(self.engine)

if __name__ == '__main__':
    test = CreateTables()
    test.run()
