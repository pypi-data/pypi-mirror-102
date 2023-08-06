# This file is placed in the Public Domain.

from .itr import findall, findmods, findnames
from .obj import Default, Object
from .utl import direct

class Names(Object):

    inits = Object({
        "adm": "gcd.adm",
        "bus": "gcd.bus",
        "clk": "gcd.clk",
        "dbs": "gcd.dbs",
        "edt": "gcd.edt",
        "err": "gcd.err",
        "evt": "gcd.evt",
        "fnd": "gcd.fnd",
        "hdl": "gcd.hdl",
        "irc": "gcd.irc",
        "itr": "gcd.itr",
        "ldr": "gcd.ldr",
        "log": "gcd.log",
        "mbx": "gcd.mbx",
        "nms": "gcd.nms",
        "obj": "gcd.obj",
        "opt": "gcd.opt",
        "prs": "gcd.prs",
        "rss": "gcd.rss",
        "tdo": "gcd.tdo",
        "thr": "gcd.thr",
        "tms": "gcd.tms",
        "trc": "gcd.trc",
        "trm": "gcd.trm",
        "udp": "gcd.udp",
        "url": "gcd.url",
        "usr": "gcd.usr",
        "utl": "gcd.utl",
        "zzz": "gcd.zzz"
    })
    
    names = Default({
        "bus": [
            "gcd.bus.Bus"
        ],
        "cfg": [
            "gcd.obj.Cfg",
            "gcd.rss.Cfg",
            "gcd.udp.Cfg",
            "gcd.irc.Cfg"
        ],
        "client": [
            "gcd.hdl.Client"
        ],
        "command": [
            "gcd.evt.Command"
        ],
        "dcc": [
            "gcd.irc.DCC"
        ],
        "default": [
            "gcd.obj.Default"
        ],
        "email": [
            "gcd.mbx.Email"
        ],
        "enoclass": [
            "gcd.err.ENOCLASS"
        ],
        "enofilename": [
            "gcd.err.ENOFILENAME"
        ],
        "enomore": [
            "gcd.err.ENOMORE"
        ],
        "enotimplemented": [
            "gcd.err.ENOTIMPLEMENTED"
        ],
        "enotxt": [
            "gcd.err.ENOTXT"
        ],
        "enouser": [
            "gcd.err.ENOUSER"
        ],
        "event": [
            "gcd.evt.Event",
            "gcd.irc.Event"
        ],
        "feed": [
            "gcd.rss.Feed"
        ],
        "fetcher": [
            "gcd.rss.Fetcher"
        ],
        "getter": [
            "gcd.prs.Getter"
        ],
        "handler": [
            "gcd.hdl.Handler"
        ],
        "httperror": [
            "urllib.error.HTTPError"
        ],
        "irc": [
            "gcd.irc.IRC"
        ],
        "loader": [
            "gcd.ldr.Loader"
        ],
        "log": [
            "gcd.log.Log"
        ],
        "names": [
            "gcd.nms.Names"
        ],
        "o": [
            "gcd.obj.O"
        ],
        "obj": [
            "gcd.obj.Obj"
        ],
        "object": [
            "gcd.obj.Object"
        ],
        "objectlist": [
            "gcd.obj.ObjectList"
        ],
        "option": [
            "gcd.prs.Option"
        ],
        "output": [
            "gcd.opt.Output"
        ],
        "repeater": [
            "gcd.clk.Repeater"
        ],
        "request": [
            "urllib.request.Request"
        ],
        "rss": [
            "gcd.rss.Rss"
        ],
        "seen": [
            "gcd.rss.Seen"
        ],
        "setter": [
            "gcd.prs.Setter"
        ],
        "skip": [
            "gcd.prs.Skip"
        ],
        "textwrap": [
            "gcd.irc.TextWrap"
        ],
        "thr": [
            "gcd.thr.Thr"
        ],
        "timed": [
            "gcd.prs.Timed"
        ],
        "timer": [
            "gcd.clk.Timer"
        ],
        "todo": [
            "gcd.tdo.Todo"
        ],
        "token": [
            "gcd.prs.Token"
        ],
        "udp": [
            "gcd.udp.UDP"
        ],
        "urlerror": [
            "urllib.error.URLError"
        ],
        "user": [
            "gcd.usr.User"
        ],
        "users": [
            "gcd.usr.Users"
        ]
    })

    modules = Object({
        "cfg": "gcd.irc",
        "cmd": "gcd.cmd",
        "dlt": "gcd.usr",
        "dne": "gcd.tdo",
        "dpl": "gcd.rss",
        "ech": "gcd.adm",
        "flt": "gcd.adm",
        "fnd": "gcd.fnd",
        "ftc": "gcd.rss",
        "krn": "gcd.adm",
        "log": "gcd.log",
        "mbx": "gcd.mbx",
        "met": "gcd.usr",
        "rem": "gcd.rss",
        "rss": "gcd.rss",
        "sve": "gcd.adm",
        "tdo": "gcd.tdo",
        "thr": "gcd.adm",
        "upt": "gcd.adm"
    })

    @staticmethod
    def getnames(nm, dft=None):
        return Names.names.get(nm, dft)


    @staticmethod
    def getmodule(mn):
        return Names.modules.get(mn, None)

    @staticmethod
    def getinit(mn):
        return Names.inits.get(mn, None)

    @staticmethod
    def tbl(tbl):
        Names.names.update(tbl["names"])
        Names.modules.update(tbl["modules"])
        Names.inits.update(tbl["inits"])

    @staticmethod
    def walk(names):
        for mn in findall(names):
            mod = direct(mn)
            if "cmd" not in mn:
                Names.inits[mn.split(".")[-1]] = mn
            Names.modules.update(findmods(mod))
            for k, v in findnames(mod).items():
                if k not in Names.names:
                    Names.names[k] = []
                if v not in Loader.names[k]:
                    Names.names[k].append(v)
