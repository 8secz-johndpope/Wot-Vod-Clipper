# Libraries
import ntpath

# Local Libs
from wot_vod import Tank, Map, BattleLevel, BattleResult, Battle, WotVod
from vod_clipper import VodClipper


class WotVovClipper(object):
    def __init__(self):
        self.clipper = VodClipper()
        pass

    def clip(self, in_file, out_dir, wot_vod: WotVod):
        extension = self.compute_file_extension(in_file)
        for battle in wot_vod.battles:
            out_filename = self.build_filename(battle, out_dir, extension)
            duration = battle.end - battle.start
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
