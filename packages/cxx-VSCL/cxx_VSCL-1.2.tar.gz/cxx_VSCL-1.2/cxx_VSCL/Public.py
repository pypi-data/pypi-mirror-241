import time
import cxx_VSCL.core
from cxx_VSCL.core import MyWS


class audio:

    def __init__(self):
        pass

    def audio_load(self, file_name: str):
        """
        加载音频
        :param file_name:
        :return:
        """
        MyWS.do_immediately(
            {'type': 'other', 'commond': 'audio_load', 'file_name': file_name, })
        return self

    def audio_play(self):
        """
        播放音频
        :return:
        """
        MyWS.do_immediately(
            {'type': 'other', 'commond': 'audio_play', })
        return

    def audio_pause(self):
        MyWS.do_immediately(
            {'type': 'other', 'commond': 'audio_pause', })
        return

    def audio_stop(self):
        MyWS.do_immediately(
            {'type': 'other', 'commond': 'audio_stop', })
        return

    def audio_set_volume(self):
        MyWS.do_immediately(
            {'type': 'other', 'commond': 'audio_set_volume', })
        return
