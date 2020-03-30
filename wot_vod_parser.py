import json
import jsonschema

from wot_vod import Tank, Map, BattleLevel, BattleResult, BattleTimestamp, Battle, WotVod

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


def parse(in_json) -> WotVod:
    payload = json.loads(in_json)
    jsonschema.validate(instance=payload, schema=schema)

    return _build_wot_vod(payload)


def _build_wot_vod(payload):
    # Build WotVod
    wot_vod_payload = payload["WotVod"]
    wot_vod = WotVod(wot_vod_payload["date"], wot_vod_payload["id"], wot_vod_payload["title"])

    # Build Battles
    for battle_payload in wot_vod_payload["battles"]:
        battle = _build_battle(battle_payload)
        wot_vod.add(battle)

    return wot_vod


def _build_battle(payload):
    tank = _build_tank(payload["tank"])
    map = _build_map(payload["map"])
    tier = payload["tier"]
    start = _build_timestamp(payload["start"])
    end = _build_timestamp(payload["end"])
    battle_result = _build_battle_result(payload["result"])

    return Battle(tank, map, tier, start, end, battle_result)


def _build_tank(payload):
    return Tank(payload["name"], payload["nation"], payload["type"], payload["tier"])


def _build_map(payload):
    return Map(payload["name"])


def _build_timestamp(payload):
    hour = payload["hour"]
    minute = payload["minute"]
    second = payload["second"]
    return BattleTimestamp(hour, minute, second)


def _build_battle_result(payload):
    battle_level = _build_battle_level(payload["level"])
    return BattleResult(battle_level, payload["damage"], payload["assistance"])


def _build_battle_level(value):
    return BattleLevel(value)
