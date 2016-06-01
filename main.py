#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : main.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1464507738
# Last Modified :
# Release By : Doom.zhou
###############################################################################

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.logger import Logger

import os


class wubi(BoxLayout):

    def font_name(self, *args):
        if os.path.exists('wqy-microhei.ttc'):
            return 'wqy-microhei.ttc'
        else:
            return '/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc'

    def gen_dict(self):
        a = {}
        for i in open('wubi.t', 'r'):
            a.update({i.split()[0]: i.split()[1]})
        return a

    def query(self, *args):
        MyTextInput = self.ids['MyTextInput'] 
        ResultDisplayLabel = self.ids['ResultDisplayLabel']
        Mbdict = self.gen_dict()
        result = StringProperty()
        if len(args[0]) > 2:
            Logger.info('info: less than three word')
            MyTextInput.text = args[0][:2]
            result = '支持少于3个字'
        elif len(args[0]) == 0:
            result = 'Unknown'
        elif len(args[0]) == 1:
            try:
                key = args[0][:1].encode('utf-8')
                result = Mbdict[key]
            except: # 2/3 compatible code
                key = args[0][:1]
                result = Mbdict[key]
                Logger.info(result)
        else:
            try:
                key1 = args[0][:1].encode('utf-8')
                key2 = args[0][1:2].encode('utf-8')
                result = Mbdict[key]
            except: # 2/3 compatible code
                key1 = args[0][:1]
                key2 = args[0][1:2]
                result = Mbdict[key1][:2] + Mbdict[key2][:2]
                Logger.info(result)
        ResultDisplayLabel.text = result


class wubiapp(App):

    def build(self):
        return wubi()


if __name__ == '__main__':
    wubiapp().run()
