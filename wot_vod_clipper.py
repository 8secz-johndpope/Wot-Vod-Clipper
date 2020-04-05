#!/usr/bin/python

# Libraries
from enum import IntEnum
import json
import jsonschema
import ntpath
import sys

# Locals
from vod_clipper import VodClipper


# Classes for WotVod Objects
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


# Class for WotVodParser
schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "WotVod",
    "description": "A schema for Wot VoD",

    "definitions": {
        "nonEmptyString": {
            "type": "string",
            "minLength": 1
        },

        "nonNegativeInteger": {
            "type": "integer",
            "minimum": 0
        },

        "maxFiftyNineNonNegativeInteger": {
            "type": "integer",
            "minimum": 0,
            "maximum": 59
        },

        "nation": {
            "type": "string",
            "enum": ["USSR", "Germany", "USA", "France", "UK", "Czechoslovakia", "Japan", "China", "Sweden", "Italy"]
        },

        "tank_type": {
            "type": "string",
            "enum": ["LT", "MT", "HT", "TD", "SPG"]

        },

        "tier": {
            "type": "integer",
            "minimum": 1,
            "maximum": 10
        },

        "BattleLevel": {
            "type": "integer",
            "minimum": 0,
            "maximum": 3
        },

        "Tank": {
            "type": "object",
            "properties": {
                "name": {
                    "$ref": "#/definitions/nonEmptyString"
                },
                "nation": {
                    "$ref": "#/definitions/nation"
                },
                "type": {
                    "$ref": "#/definitions/tank_type"
                },
                "tier": {
                    "$ref": "#/definitions/tier"
                }
            },
            "required": ["name"]
        },

        "Map": {
            "type": "object",
            "properties": {
                "name": {
                    "$ref": "#/definitions/nonEmptyString"
                }
            },
            "required": ["name"]
        },

        "BattleTimestamp": {
            "type": "object",
            "properties": {
                "hour": {
                    "$ref": "#/definitions/nonNegativeInteger"
                },
                "minute": {
                    "$ref": "#/definitions/maxFiftyNineNonNegativeInteger"
                },
                "second": {
                    "$ref": "#/definitions/maxFiftyNineNonNegativeInteger"
                }
            },
            "required": ["hour", "minute", "second"]
        },

        "BattleResult": {
            "type": "object",
            "properties": {
                "level": {
                    "$ref": "#/definitions/BattleLevel"
                },
                "damage": {
                    "$ref": "#/definitions/nonNegativeInteger"
                },
                "assistance": {
                    "$ref": "#/definitions/nonNegativeInteger"
                }
            },
            "required": ["level", "damage", "assistance"]
        },

        "Battle": {
            "type": "object",
            "properties": {
                "tank": {
                    "$ref": "#/definitions/Tank"
                },
                "map": {
                    "$ref": "#/definitions/Map"
                },
                "tier": {
                    "$ref": "#/definitions/tier"
                },
                "start": {
                    "$ref": "#/definitions/BattleTimestamp"
                },
                "end": {
                    "$ref": "#/definitions/BattleTimestamp"
                },
                "result": {
                    "$ref": "#/definitions/BattleResult"
                }
            },
            "required": ["tank", "map", "start", "end", "result"]
        },

        "WotVod": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "pattern": "[0-9]{8}"
                },
                "id": {
                    "$ref": "#/definitions/nonNegativeInteger"
                },
                "title": {
                    "$ref": "#/definitions/nonEmptyString"
                },
                "battles": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Battle"
                    }
                }
            },
            "required": ["date", "id", "title", "battles"]

        }
    },

    "type": "object",
    "properties": {
        "WotVod": {
            "$ref": "#/definitions/WotVod"
        }
    },
    "required": ["WotVod"]
}


class WotVodParser(object):
    def parse(self, in_json) -> WotVod:
        payload = json.loads(in_json)
        jsonschema.validate(instance=payload, schema=schema)

        return self._build_wot_vod(payload)

    def _build_wot_vod(self, payload):
        # Build WotVod
        wot_vod_payload = payload["WotVod"]
        wot_vod = WotVod(wot_vod_payload["date"], wot_vod_payload["id"], wot_vod_payload["title"])

        # Build Battles
        for battle_payload in wot_vod_payload["battles"]:
            battle = self._build_battle(battle_payload)
            wot_vod.add(battle)

        return wot_vod

    def _build_battle(self, payload):
        tank = self._build_tank(payload["tank"])
        _map = self._build_map(payload["map"])
        tier = payload["tier"]
        start = self._build_timestamp(payload["start"])
        end = self._build_timestamp(payload["end"])
        battle_result = self._build_battle_result(payload["result"])

        return Battle(tank, _map, tier, start, end, battle_result)

    @staticmethod
    def _build_tank(payload):
        return Tank(payload["name"], payload["nation"], payload["type"], payload["tier"])

    @staticmethod
    def _build_map(payload):
        return Map(payload["name"])

    @staticmethod
    def _build_timestamp(payload):
        hour = payload["hour"]
        minute = payload["minute"]
        second = payload["second"]
        return BattleTimestamp(hour, minute, second)

    def _build_battle_result(self, payload):
        battle_level = self._build_battle_level(payload["level"])
        return BattleResult(battle_level, payload["damage"], payload["assistance"])

    @staticmethod
    def _build_battle_level(value):
        return BattleLevel(value)


class WotVodClipper(object):
    def __init__(self):
        self.clipper = VodClipper()
        self.parser = WotVodParser()
        pass

    def clip(self, in_file, out_dir, wot_vod: WotVod = None, config=None):
        if not wot_vod and not config:
            sys.exit("[ERROR]{} Please provide either WotVod object or configuration in JSON."
                     .format(self.__class__.__name__))

        if not wot_vod:
            # Parse config JSON if wot_vod object is None
            wot_vod = self.parser.parse(config)

        self._clip(in_file=in_file, out_dir=out_dir, wot_vod=wot_vod)
        pass

    def _clip(self, in_file, out_dir, wot_vod: WotVod):
        extension = self.compute_file_extension(in_file)
        for battle in wot_vod.battles:
            out_filename = self.build_filename(wot_vod, battle, out_dir, extension)
            duration = battle.end - battle.start
            print("[INFO] Clipping battle {}-{} to {}".format(battle.start, battle.end, out_filename))
            self.clipper.clip(in_file, out_filename, battle.start, duration)
        pass

    @staticmethod
    def build_filename(vod: WotVod, battle: Battle, out_dir, extension):
        filename = '{}-{}|DMG {}|Spot {}|{}|{}|{}|{}| '.format(
            vod.date, vod.id,
            battle.result.damage,
            battle.result.assistance,
            battle.map.name,
            battle.tier,
            battle.tank.name,
            battle.tank.type
        )
        return ntpath.join(out_dir, filename, extension)

    @staticmethod
    def compute_file_extension(in_file):
        input_name, input_ext = ntpath.splitext(ntpath.basename(in_file))
        return input_ext
