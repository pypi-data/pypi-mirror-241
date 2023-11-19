import json #line:1
from basic import FileUtilsEx #line:3
class JsonUtilsEx :#line:6
    ""#line:7
    def __init__ (O00OO00OOO0OO0O00 ):#line:9
        ""#line:10
    @staticmethod #line:12
    def toPythonObjFromFile (O0000O0O0OOO0000O ):#line:13
        ""#line:18
        with open (O0000O0O0OOO0000O ,encoding ="utf-8")as OO0O0O0OO0O0OO0O0 :#line:19
            O0O0O00OOOOO000OO =json .load (OO0O0O0OO0O0OO0O0 )#line:20
        return O0O0O00OOOOO000OO #line:21
    @staticmethod #line:23
    def toStrByFile (O0O0OO0OO0O00000O ,OOOO000OO0OOO00OO ):#line:24
        ""#line:30
        O0000000O00OO00OO =json .dumps (OOOO000OO0OOO00OO ,ensure_ascii =False )#line:31
        FileUtilsEx .writeFile (O0O0OO0OO0O00000O ,O0000000O00OO00OO )#line:32
