#!/usr/bin/python

# Libraries
from enum import IntEnum, Enum
import itertools
import json


class BaseEntity(object):
    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class ExtendedEnum(Enum):
    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))


class MasteryBadge(ExtendedEnum):
    ACE = 'Ace Tanker'
    First = 'First Class'
    Second = 'Second Class'
    Third = 'Third Class'


class Tier(ExtendedEnum):
    Ten = 10
    Nine = 9
    Eight = 8
    Seven = 7
    Six = 6
    Five = 5
    Four = 4
    Three = 3
    Two = 2
    One = 1


class Tank(BaseEntity):
    def __init__(self, name, nation, _type, tier: Tier):
        self.name = name
        self.nation = nation
        self.type = _type
        self.tier = tier
        pass


class Map(BaseEntity):
    def __init__(self, name):
        self.name = name
        pass


class BattleTimestamp(BaseEntity):
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second
        pass

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second


class BattleResult(BaseEntity):
    def __init__(self, mastery_badge: MasteryBadge, damage: int, assistance: int, ):
        self.mastery_badge = mastery_badge
        self.damage = damage
        self.assistance = assistance
        pass


class Battle(BaseEntity):
    def __init__(self, tank: Tank, _map: Map, tier: Tier,
                 start: BattleTimestamp, end: BattleTimestamp,
                 result: BattleResult):
        self.tank = tank
        self.map = _map
        self.tier = tier
        self.start = start
        self.end = end
        self.result = result
        pass


class Date(BaseEntity):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        pass


class WotVod(BaseEntity):
    def __init__(self, _date: Date, _id, title):
        self.date = _date
        self.id = _id
        self.title = title
        self.battles = []
        pass

    def add(self, battle: Battle):
        self.battles.append(battle)
        pass
