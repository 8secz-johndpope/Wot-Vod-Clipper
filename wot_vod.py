from enum import Enum


class Tank(object):
    def __init__(self, name, nation, _type, tier):
        self.name = name
        self.nation = nation
        self.type = _type
        self.tier = tier
        pass


class Map(object):
    def __init__(self, name):
        self.name = name
        pass


class BattleLevel(Enum):
    ACE = 0
    First = 1
    Second = 2
    Third = 3


class BattleTimestamp(object):
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second
        pass

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second


class BattleResult(object):
    def __init__(self, level: BattleLevel, damage: int, assistance: int, ):
        self.level = level
        self.damage = damage
        self.assistance = assistance
        pass


class Battle(object):
    def __init__(self, tank: Tank, _map: Map, tier: int,
                 start: BattleTimestamp, end: BattleTimestamp,
                 result: BattleResult):
        self.tank = tank
        self.map = _map
        self.tier = tier
        self.start = start
        self.end = end
        self.result = result
        pass


class WotVod(object):
    def __init__(self, _date, _id, title):
        self.date = _date
        self.id = _id
        self.title = title
        self.battles = []
        pass

    def add(self, battle: Battle):
        self.battles.append(battle)
        pass
