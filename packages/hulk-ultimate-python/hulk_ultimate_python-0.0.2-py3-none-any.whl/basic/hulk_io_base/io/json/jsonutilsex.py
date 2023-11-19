import json #line:1
from basic import FileUtilsEx #line:3
class JsonUtilsEx :#line:6
    ""#line:7
    def __init__ (OO000OOO0O00OOO0O ):#line:9
        ""#line:10
    @staticmethod #line:12
    def toPythonObjFromFile (O0O0O000OOOOOO0O0 ):#line:13
        ""#line:18
        with open (O0O0O000OOOOOO0O0 ,encoding ="utf-8")as OO0OOO0000OOO000O :#line:19
            O0OOOO00000OO00OO =json .load (OO0OOO0000OOO000O )#line:20
        return O0OOOO00000OO00OO #line:21
    @staticmethod #line:23
    def toStrByFile (OO0OO0OO000OO00O0 ,OO0000OOOO0OO0O00 ):#line:24
        ""#line:30
        O00O0OOO00OO0O00O =json .dumps (OO0000OOOO0OO0O00 ,ensure_ascii =False )#line:31
        FileUtilsEx .writeAllText (OO0OO0OO000OO00O0 ,O00O0OOO00OO0O00O )#line:32
