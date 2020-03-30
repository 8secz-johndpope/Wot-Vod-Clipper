from enum import IntEnum
import json


class Tank(object):
    def __init__(self, name, nation, _type, tier):
        self.name = name
        self.nation = nation
        self.type = _type
        self.tier = tier
        pass

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


class Map(object):
    def __init__(self, name):
        self.name = name
        pass

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


class BattleLevel(IntEnum):
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


class BattleResult(object):
    def __init__(self, level: BattleLevel, damage: int, assistance: int, ):
        self.level = level
        self.damage = damage
        self.assistance = assistance
        pass

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
