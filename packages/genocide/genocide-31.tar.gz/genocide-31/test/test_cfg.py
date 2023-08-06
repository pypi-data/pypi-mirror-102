# This file is placed in the Public Domain.

import unittest

from gcd.edt import edit
from gcd.obj import Cfg, cfg
from gcd.prs import parseargs

cfg = Cfg()

class Test_Cfg(unittest.TestCase):

    def test_parse(self):
        parseargs(cfg, "mods=irc")
        self.assertEqual(cfg.sets.mods, "irc")

    def test_parse2(self):
        parseargs(cfg, "mods=irc,udp")
        self.assertEqual(cfg.sets.mods, "irc,udp")

    def test_edit(self):
        d = {"mods": "rss"}
        edit(cfg, d)
        self.assertEqual(cfg.mods, "rss")
