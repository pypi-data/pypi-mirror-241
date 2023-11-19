import os #line:1
import shutil #line:2
import sys #line:3
import datetime #line:4
sys .path .append (os .getcwd ())#line:6
class FileUtilsEx :#line:9
    ""#line:10
    def __init__ (O0OOOO0O0O0O0O0O0 ):#line:12
        ""#line:13
    @staticmethod #line:15
    def delFileAndCreateFileEmpty (O0OOOO00O0OOOO0OO ):#line:16
        ""#line:21
        FileUtilsEx .priDelFile (O0OOOO00O0OOOO0OO )#line:23
        FileUtilsEx .priCreateFileEmpty (O0OOOO00O0OOOO0OO )#line:25
    @staticmethod #line:27
    def writeAllText (OOOOOOOO0OO0O00O0 ,O0O0OOOO000O0OO0O ):#line:28
        ""#line:34
        FileUtilsEx .delFileAndCreateFileEmpty (OOOOOOOO0OO0O00O0 )#line:35
        with open (OOOOOOOO0OO0O00O0 ,"w",encoding ="utf-8")as OOO0O0OOO000O000O :#line:36
            OOO0O0OOO000O000O .write (O0O0OOOO000O0OO0O )#line:37
    @staticmethod #line:39
    def readAllText (OOO0OO0O0O0OO000O ):#line:40
        ""#line:45
        with open (OOO0OO0O0O0OO000O ,"r",encoding ="utf-8")as O00000O0OOO0O0000 :#line:46
            OO0OOO0OO00O000O0 =O00000O0OOO0O0000 .read ()#line:47
        return OO0OOO0OO00O000O0 #line:48
    @staticmethod #line:50
    def appendFile (O000O0O0O000OO00O ,OO000O00O00OO0000 ):#line:51
        ""#line:57
        FileUtilsEx .priCreateFileEmpty (O000O0O0O000OO00O )#line:58
        with open (O000O0O0O000OO00O ,"a",encoding ="utf-8")as O00O0OO00OO0O0OOO :#line:59
            O00O0OO00OO0O0OOO .write (OO000O00O00OO0000 )#line:60
    @staticmethod #line:62
    def appendFileWithDateTime (OO0O00O00OO00O0OO ,OO0O0OOO0O00OO00O ):#line:63
        ""#line:69
        OO0OO0OO0O00O0O00 =FileUtilsEx .priGenFilePathByDateTime (OO0O00O00OO00O0OO )#line:70
        FileUtilsEx .appendFile (OO0OO0OO0O00O0O00 ,OO0O0OOO0O00OO00O )#line:71
    @staticmethod #line:73
    def copyFile (OOOO00O00O000OO00 ,OOOO0OO00000OO00O ):#line:74
        ""#line:80
        FileUtilsEx .priCreateFileEmpty (OOOO0OO00000OO00O )#line:83
        shutil .copy2 (OOOO00O00O000OO00 ,OOOO0OO00000OO00O )#line:85
    @staticmethod #line:87
    def iterAllFiles (O0OOO00O00OO0O00O ,O0OO0O0OOOOO00O00 ):#line:88
        ""#line:94
        for OO000O0O0OOOOO000 ,OOO000OOOOO000000 ,O0OO00OOO00OOO0O0 in os .walk (O0OOO00O00OO0O00O ):#line:95
            for O000O00OOO0000OO0 in O0OO00OOO00OOO0O0 :#line:96
                if O000O00OOO0000OO0 .endswith (O0OO0O0OOOOO00O00 ):#line:97
                    OOOOOO0000O0OO00O =os .path .join (OO000O0O0OOOOO000 ,O000O00OOO0000OO0 )#line:98
                    yield OOOOOO0000O0OO00O #line:99
    @staticmethod #line:101
    def priGetDirPath (O00OO00OO000OOO00 ):#line:102
        ""#line:107
        return os .path .dirname (O00OO00OO000OOO00 )#line:108
    @staticmethod #line:110
    def priCreateDirEmpty (O0OOO0O0000O0O0OO ):#line:111
        ""#line:116
        if not os .path .exists (O0OOO0O0000O0O0OO ):#line:117
            os .makedirs (O0OOO0O0000O0O0OO ,exist_ok =True )#line:118
    @staticmethod #line:120
    def priCreateFileEmpty (OO00O000OO00OOO0O ):#line:121
        ""#line:126
        OOOOOOO0OOOO0O00O =FileUtilsEx .priGetDirPath (OO00O000OO00OOO0O )#line:128
        FileUtilsEx .priCreateDirEmpty (OOOOOOO0OOOO0O00O )#line:130
        if not os .path .exists (OO00O000OO00OOO0O ):#line:132
            with open (OO00O000OO00OOO0O ,"w",encoding ="utf-8"):#line:133
                pass #line:134
    @staticmethod #line:136
    def priDelFile (OOO0O0OO00O0OO00O ):#line:137
        ""#line:142
        if os .path .exists (OOO0O0OO00O0OO00O ):#line:143
            os .remove (OOO0O0OO00O0OO00O )#line:144
    @staticmethod #line:146
    def priGenFilePathByDateTime (OOO0OOO00O00O0O00 ):#line:147
        ""#line:153
        OOOO0O0OO0O000OOO =os .path .splitext (OOO0OOO00O00O0O00 )#line:154
        OO00OOOOO0OO0OOO0 =OOOO0O0OO0O000OOO [0 ]#line:155
        OO0000000O0000OOO =OOOO0O0OO0O000OOO [-1 ]#line:156
        OO000O00O00O0000O =datetime .date .today ().strftime ("%Y-%m-%d")#line:157
        return OO00OOOOO0OO0OOO0 +"_"+OO000O00O00O0000O +OO0000000O0000OOO #line:158
if __name__ =='__main__':#line:161
    print (1 )#line:169
