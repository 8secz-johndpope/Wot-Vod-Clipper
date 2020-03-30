import json
import jsonschema

from wot_vod import Tank, Map, BattleLevel, BattleResult, Battle, WotVod

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
