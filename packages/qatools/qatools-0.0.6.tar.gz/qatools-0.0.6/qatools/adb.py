#!/usr/bin/python
""  # line:6
import base64  # line:7
import os  # line:8
import platform  # line:9
import socket  # line:10
import stat  # line:11

import psutil  # line:13

STATICPATH = os.path.dirname(os.path.realpath(__file__))  # line:15
DEFAULT_ADB_PATH = {
    "Windows": os.path.join(STATICPATH, "adb", "windows", "adb.exe"),
    "Darwin": os.path.join(STATICPATH, "adb", "mac", "adb"),
    "Linux": os.path.join(STATICPATH, "adb", "linux", "adb"),
    "Linux-x86_64": os.path.join(STATICPATH, "adb", "linux", "adb"),
    "Linux-armv7l": os.path.join(STATICPATH, "adb", "linux_arm", "adb"),
}  # line:22


def make_file_executable(O000OO000OO0OO0O0):  # line:25
    """"""  # line:30
    if os.path.isfile(O000OO000OO0OO0O0):  # line:31
        OOOOO00O00O0O00O0 = os.lstat(O000OO000OO0OO0O0)[stat.ST_MODE]  # line:32
        OO0OOO0OOOOOOOOO0 = (
            True if OOOOO00O00O0O00O0 & stat.S_IXUSR else False
        )  # line:33
        if not OO0OOO0OOOOOOOOO0:  # line:34
            os.chmod(
                O000OO000OO0OO0O0,
                OOOOO00O00O0O00O0 | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH,
            )  # line:35
        return True  # line:36
    return False  # line:37


def builtin_adb_path():  # line:40
    OOOO00O00000O0OOO = platform.system()  # line:41
    O0OO0OO00O00OO0O0 = platform.machine()  # line:42
    OO0O0O00O00OO00OO = DEFAULT_ADB_PATH.get(
        f"{OOOO00O00000O0OOO}-{O0OO0OO00O00OO0O0}"
    )  # line:43
    if not OO0O0O00O00OO00OO:  # line:44
        OO0O0O00O00OO00OO = DEFAULT_ADB_PATH.get(OOOO00O00000O0OOO)  # line:45
    if not OO0O0O00O00OO00OO:  # line:46
        raise RuntimeError(
            f"No adb executable supports this platform({OOOO00O00000O0OOO}-{O0OO0OO00O00OO0O0})."
        )  # line:49
    if OOOO00O00000O0OOO != "Windows":  # line:51
        make_file_executable(OO0O0O00O00OO00OO)  # line:53
    return OO0O0O00O00OO00OO  # line:54


def get_adb_path():  # line:57
    if platform.system() == "Windows":  # line:58
        OOOOOOOOO0OO0O00O = "adb.exe"  # line:59
    else:  # line:60
        OOOOOOOOO0OO0O00O = "adb"  # line:61
    for O00OO00OOOO000O00 in psutil.process_iter(["name", "exe"]):  # line:64
        if O00OO00OOOO000O00.info["name"] == OOOOOOOOO0OO0O00O:  # line:65
            return O00OO00OOOO000O00.info["exe"]  # line:66
    O00O0OOOOOO00O00O = os.environ.get("ANDROID_HOME")  # line:69
    if O00O0OOOOOO00O00O:  # line:70
        O0O0000O000OO000O = os.path.join(
            O00O0OOOOOO00O00O, "platform-tools", OOOOOOOOO0OO0O00O
        )  # line:71
        if os.path.exists(O0O0000O000OO000O):  # line:72
            return O0O0000O000OO000O  # line:73
    O0O0000O000OO000O = builtin_adb_path()  # line:76
    return O0O0000O000OO000O  # line:77


def get_host_ip():  # line:80
    """"""  # line:84
    O0O0O0O0000OO00O0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # line:85
    try:  # line:86
        O0O0O0O0000OO00O0.connect(("8.8.8.8", 80))  # line:87
        OOOO0000OO0000OO0 = O0O0O0O0000OO00O0.getsockname()[0]  # line:88
    finally:  # line:89
        O0O0O0O0000OO00O0.close()  # line:90
    return OOOO0000OO0000OO0  # line:92


def encryption(O000O00OOOO0OO00O):  # line:95
    """"""  # line:100
    O00O0OO0O0OOO0000 = O000O00OOOO0OO00O.encode("utf-8")  # line:101
    OOO00O000OOO0OO00 = base64.b64encode(O00O0OO0O0OOO0000)  # line:102
    return OOO00O000OOO0OO00  # line:103


def decryption(O00O0OOO0OO000O00):  # line:106
    """"""  # line:111
    O0O00OO0OOOOOO00O = base64.b64decode(O00O0OOO0OO000O00).decode("utf-8")  # line:112
    return O0O00OO0OOOOOO00O  # line:113
