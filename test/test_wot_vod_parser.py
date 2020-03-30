import unittest

from wot_vod import Tank, Map, BattleLevel, BattleResult, BattleTimestamp, Battle, WotVod
import wot_vod_parser

in_json = "{\"WotVod\":{\"date\":\"12345678\",\"id\":1,\"title\":\"asdfasdf\",\"battles\":[{\"tank\":{\"name\":\"taaaaaaaaaaank\",\"nation\":\"USSR\",\"type\":\"MT\",\"tier\":10},\"map\":{\"name\":\"maaaaaaaaaaaaaap\"},\"tier\":9,\"start\":{\"hour\":0,\"minute\":12,\"second\":34},\"end\":{\"hour\":5,\"minute\":16,\"second\":17},\"result\":{\"level\":0,\"damage\":1234,\"assistance\":5678}}]}}"


class TestWotVodParser(unittest.TestCase):
    def test_parse(self):
        wot_vod = wot_vod_parser.parse(in_json)
        expected_wot_vod = WotVod(_date="12345678",
                                  _id=1,
                                  title="asdfasdf")
        expected_wot_vod.add(Battle(
            Tank(name="taaaaaaaaaaank",
                 nation="USSR",
                 _type="MT",
                 tier=10),
            Map(name="maaaaaaaaaaaaaap"),
            tier=9,
            start=BattleTimestamp(0, 12, 34),
            end=BattleTimestamp(5, 16, 17),
            result=BattleResult(level=BattleLevel(0),
                                damage=1234,
                                assistance=5678)
        ))

        self.assertEqual(expected_wot_vod, wot_vod)
        pass


if __name__ == '__main__':
    unittest.main()
