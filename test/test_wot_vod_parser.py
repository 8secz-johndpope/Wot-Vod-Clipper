import wot_vod_parser

import unittest

in_json = "{\"WotVod\":{\"date\":\"12345678\",\"id\":1,\"title\":\"asdfasdf\",\"battles\":[{\"tank\":{\"name\":\"taaaaaaaaaaank\",\"nation\":\"USSR\",\"type\":\"MT\",\"tier\":10},\"map\":{\"name\":\"maaaaaaaaaaaaaap\"},\"tier\":9,\"start\":{\"hour\":0,\"minute\":12,\"second\":34},\"end\":{\"hour\":5,\"minute\":16,\"second\":17},\"result\":{\"level\":0,\"damage\":1234,\"assistance\":5678}}]}}"


class TestWotVodParser(unittest.TestCase):
    def test(self):
        wot_vod = wot_vod_parser.parse(in_json)
        print(wot_vod)


if __name__ == '__main__':
    unittest.main()
