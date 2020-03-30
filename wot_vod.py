from enum import Enum


class Tank(object):
    def __init__(self, name, nation, _type, level):
        self.name = name
        self.nation = nation
        self.type = _type
        self.level = level
        pass


class Map(object):
    def __init__(self, name):
        self.name = name


class BattleLevel(Enum):
    ACE = 0
    First = 1
    Second = 2
    Third = 3


class BattleResult(object):
    def __init__(self, level: BattleLevel, damage: int, assistance: int, ):
        self.level = level
        self.damage = damage
        self.assistance = assistance


class Battle(object):
    def __init__(self, tank: Tank, _map: Map, tier, start_s, end_s):
        self.tank = tank
        self.map = _map
        self.tier = tier
        self.start = start_s
        self.end = end_s
        pass


class WotVod(object):
    def __init__(self, _date, _id, title):
        self.date = _date
        self.id = id
        self.title = title
        self.battles = []
        pass

    def add(self, battle: Battle):
        self.battles.append(battle)
        pass
