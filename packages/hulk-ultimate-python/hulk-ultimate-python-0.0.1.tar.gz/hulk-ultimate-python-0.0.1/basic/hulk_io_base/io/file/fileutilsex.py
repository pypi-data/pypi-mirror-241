import os #line:1
import shutil #line:2
import sys #line:3
import datetime #line:4
sys .path .append (os .getcwd ())#line:6
class FileUtilsEx :#line:9
    ""#line:10
    def __init__ (O0OOOOOO000OO000O ):#line:12
        ""#line:13
    @staticmethod #line:15
    def delFileAndCreateFileEmpty (O0OOOO0O00O00OO0O ):#line:16
        ""#line:21
        FileUtilsEx .priDelFile (O0OOOO0O00O00OO0O )#line:23
        FileUtilsEx .priCreateFileEmpty (O0OOOO0O00O00OO0O )#line:25
    @staticmethod #line:27
    def writeFile (O0OO000000OOOOO0O ,O0OOO0000OOOOOO0O ):#line:28
        ""#line:34
        FileUtilsEx .delFileAndCreateFileEmpty (O0OO000000OOOOO0O )#line:35
        with open (O0OO000000OOOOO0O ,"w",encoding ="utf-8")as OO0O0O0OO0O000O0O :#line:36
            OO0O0O0OO0O000O0O .write (O0OOO0000OOOOOO0O )#line:37
    @staticmethod #line:39
    def appendFile (O00OO0OO0O000O00O ,OOO00OO0O0O0O0OOO ):#line:40
        ""#line:46
        FileUtilsEx .priCreateFileEmpty (O00OO0OO0O000O00O )#line:47
        with open (O00OO0OO0O000O00O ,"a",encoding ="utf-8")as O0OOO000OOO00OO00 :#line:48
            O0OOO000OOO00OO00 .write (OOO00OO0O0O0O0OOO )#line:49
    @staticmethod #line:51
    def appendFileWithDateTime (O0O00OO0OOOO00000 ,OO0O00O0O0O0OOO00 ):#line:52
        ""#line:58
        OO000O0OOOOOO0O0O =FileUtilsEx .priGenFilePathByDateTime (O0O00OO0OOOO00000 )#line:59
        FileUtilsEx .appendFile (OO000O0OOOOOO0O0O ,OO0O00O0O0O0OOO00 )#line:60
    @staticmethod #line:62
    def copyFile (OOO0O00O0O00O0O00 ,O000OO00OO000O00O ):#line:63
        ""#line:69
        FileUtilsEx .priCreateFileEmpty (O000OO00OO000O00O )#line:72
        shutil .copy2 (OOO0O00O0O00O0O00 ,O000OO00OO000O00O )#line:74
    @staticmethod #line:76
    def priGetDirPath (OO0O0O0O0O00OOOO0 ):#line:77
        ""#line:82
        return os .path .dirname (OO0O0O0O0O00OOOO0 )#line:83
    @staticmethod #line:85
    def priCreateDirEmpty (O000OOOOO0OOOOOOO ):#line:86
        ""#line:91
        if not os .path .exists (O000OOOOO0OOOOOOO ):#line:92
            os .makedirs (O000OOOOO0OOOOOOO ,exist_ok =True )#line:93
    @staticmethod #line:95
    def priCreateFileEmpty (O0O0OO00O0OO0O0O0 ):#line:96
        ""#line:101
        OOO000O00O00000O0 =FileUtilsEx .priGetDirPath (O0O0OO00O0OO0O0O0 )#line:103
        FileUtilsEx .priCreateDirEmpty (OOO000O00O00000O0 )#line:105
        if not os .path .exists (O0O0OO00O0OO0O0O0 ):#line:107
            with open (O0O0OO00O0OO0O0O0 ,"w",encoding ="utf-8"):#line:108
                pass #line:109
    @staticmethod #line:111
    def priDelFile (OO0OO0O00000O0OOO ):#line:112
        ""#line:117
        if os .path .exists (OO0OO0O00000O0OOO ):#line:118
            os .remove (OO0OO0O00000O0OOO )#line:119
    @staticmethod #line:121
    def priGenFilePathByDateTime (OOO00OOOOOO0OO0O0 ):#line:122
        ""#line:128
        OOO00O0O000O0O00O =os .path .splitext (OOO00OOOOOO0OO0O0 )#line:129
        O000OOO0O00O00O0O =OOO00O0O000O0O00O [0 ]#line:130
        OOOO00000000O0OOO =OOO00O0O000O0O00O [-1 ]#line:131
        O000O000O000OOO0O =datetime .date .today ().strftime ("%Y-%m-%d")#line:132
        return O000OOO0O00O00O0O +"_"+O000O000O000OOO0O +OOOO00000000O0OOO #line:133
if __name__ =='__main__':#line:136
    print (1 )#line:144
