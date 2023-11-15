#!/usr/bin/python
""  # line:6
import argparse  # line:7
import os  # line:8
import sys  # line:9

from qatools import __description__  # line:11
from qatools import __version__  # line:12
from qatools.adb import decryption  # line:13
from qatools.adb import get_adb_path  # line:14
from qatools.adb import get_host_ip  # line:15

adb = get_adb_path()  # line:17


def main():  # line:20
    O0OOOO0OO000O0OOO = argparse.ArgumentParser(description=__description__)  # line:21
    O0OOOO0OO000O0OOO.add_argument(
        "-v", "--version", dest="version", action="store_true", help="show version"
    )  # line:25
    O000O00000OOO0O00 = O0OOOO0OO000O0OOO.add_subparsers(
        help="sub-command help"
    )  # line:26
    O000O00000OOO0O00.add_parser("clear", help="clear app cache data).")  # line:27
    O000O00000OOO0O00.add_parser(
        "adb", help="complete adb debugging capability."
    )  # line:28
    O000O00000OOO0O00.add_parser(
        "remote", help="open Android device remote debugging port(5555)."
    )  # line:31
    O000O00000OOO0O00.add_parser(
        "proxy", help=f"enable device global proxy({get_host_ip()}:8888)."
    )  # line:34
    O000O00000OOO0O00.add_parser(
        "unproxy", help=f"disable device global proxy."
    )  # line:35
    if len(sys.argv) == 1:  # line:37
        O0OOOO0OO000O0OOO.print_help()  # line:39
        sys.exit(0)  # line:40
    elif len(sys.argv) == 2:  # line:41
        if sys.argv[1] in ["-v", "--version"]:  # line:43
            print(f"{__version__}")  # line:45
        elif sys.argv[1] == "remote":  # line:47
            ret = os.system(f"{adb} tcpip 5555")  # line:49
            if ret == 0:
                print("已经开启端口5555远程调试，请检查是否开启成功。")  # line:50
        elif sys.argv[1] == "proxy":  # line:51
            os.system(
                f'{adb} {decryption(b"c2hlbGwgc2V0dGluZ3MgcHV0IGdsb2JhbCBodHRwX3Byb3h5")} {get_host_ip()}:8888'
            )  # line:55
            print(f"已经开启代理，请检查是否开启成功。{get_host_ip()}:8888")  # line:56
        elif sys.argv[1] == "unproxy":  # line:58
            os.system(
                f'{adb} {decryption(b"c2hlbGwgc2V0dGluZ3MgcHV0IGdsb2JhbCBodHRwX3Byb3h5IDow")}'
            )  # line:62
            print("已经关闭代理，请检查是否关闭成功。")  # line:63
        elif sys.argv[1] == "adb":  # line:65
            os.system(f"{adb}")  # line:67
        elif sys.argv[1] in ["-h", "--help"]:  # line:69
            O0OOOO0OO000O0OOO.print_help()  # line:71
        else:  # line:72
            O0OOOO0OO000O0OOO.print_help()  # line:73
        sys.exit(0)  # line:74
    elif sys.argv[1] == "adb":  # line:76
        del sys.argv[0:2]  # line:77
        O0000OOOO00O0000O = " ".join(
            [str(OOO0O0OO0OOO0O00O) for OOO0O0OO0OOO0O00O in sys.argv]
        )  # line:78
        os.system(f"{adb} {O0000OOOO00O0000O}")  # line:79
        sys.exit(0)  # line:80
    elif len(sys.argv) == 3:  # line:82
        if sys.argv[1] == "clear":  # line:83
            os.system(f"{adb} shell pm clear {sys.argv[2]}")  # line:84
        sys.exit(0)  # line:85
    O0000OOOO00O0000O = O0OOOO0OO000O0OOO.parse_args()  # line:87
    if O0000OOOO00O0000O.version:  # line:89
        print(f"{__version__}")  # line:90
        sys.exit(0)  # line:91
