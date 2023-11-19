from loguru import logger #line:1
import os #line:2
import sys #line:3
sys .path .append (os .getcwd ())#line:5
TEMPLATE_FILE_LOG ="[{0}]{1}"#line:7
"""日志模板"""#line:8
class LogUtilsEx :#line:11
    ""#line:12
    def __init__ (OO0O0OOOO0OO0OOO0 ):#line:14
        ""#line:15
        OO0O0OOOO0OO0OOO0 .logFilterVoList =[]#line:17
        OO0O0OOOO0OO0OOO0 .logger =logger #line:20
    def init (OO0000O000O0O0OO0 ,dirPathRelativeConf ="",bDebug =False ,fileNameLog ="app.log",logRotationTime ="02:00"):#line:23
        ""#line:31
        O000000O00O00OO00 =dirPathRelativeConf +"resources/logs"#line:33
        if not os .path .exists (O000000O00O00OO00 ):#line:34
            os .makedirs (O000000O00O00OO00 )#line:35
        O0OO0O0O0O0O00O0O =os .path .join (O000000O00O00OO00 ,fileNameLog )#line:36
        OO0000O000O0O0OO0 .priInitLogFilterKeyVoList (dirPathRelativeConf )#line:39
        logger .remove ()#line:42
        O00OO0O0O0OO000OO ="DEBUG"if bDebug else "INFO"#line:45
        logger .add (sys .stdout ,level =O00OO0O0O0OO000OO )#line:46
        logger .add (O0OO0O0O0O0O00O0O ,rotation =logRotationTime ,level =O00OO0O0O0OO000OO )#line:47
    def debug (OO000OO00000O0O00 ,OOO0O00OOO0OO000O ,O0OO000OOOOO00OO0 ,logFilterKey =""):#line:49
        ""#line:56
        OO00OO0O0O0OOOOOO =OO000OO00000O0O00 .priGetLogFilterVo (logFilterKey )#line:57
        if OO00OO0O0O0OOOOOO is not None and OO00OO0O0O0OOOOOO .open is False :#line:58
            return #line:59
        LOG .logger .debug (TEMPLATE_FILE_LOG .format (OOO0O00OOO0OO000O ,O0OO000OOOOO00OO0 ))#line:60
    def info (O000O0O00O00OO00O ,O00OO00OO0000OO00 ,OOO0OOOO00O0O0OO0 ,logFilterKey =""):#line:62
        ""#line:69
        O0OOOOOO0000O0OOO =O000O0O00O00OO00O .priGetLogFilterVo (logFilterKey )#line:70
        if O0OOOOOO0000O0OOO is not None and O0OOOOOO0000O0OOO .open is False :#line:71
            return #line:72
        LOG .logger .info (TEMPLATE_FILE_LOG .format (O00OO00OO0000OO00 ,OOO0OOOO00O0O0OO0 ))#line:73
    def warn (O0O00000O00O0O00O ,OOO000O00O00O0OO0 ,OO0000O0O00OOO000 ,logFilterKey =""):#line:75
        ""#line:82
        O000OOO00O000O000 =O0O00000O00O0O00O .priGetLogFilterVo (logFilterKey )#line:83
        if O000OOO00O000O000 is not None and O000OOO00O000O000 .open is False :#line:84
            return #line:85
        LOG .logger .warning (TEMPLATE_FILE_LOG .format (OOO000O00O00O0OO0 ,OO0000O0O00OOO000 ))#line:86
    def error (OOO00O00O000000OO ,OOOO00O0OOO0O0000 ,OO0OO000OO00O0OO0 ,logFilterKey =""):#line:88
        ""#line:95
        O0O0OO000O000O0OO =OOO00O00O000000OO .priGetLogFilterVo (logFilterKey )#line:96
        if O0O0OO000O000O0OO is not None and O0O0OO000O000O0OO .open is False :#line:97
            return #line:98
        LOG .logger .error (TEMPLATE_FILE_LOG .format (OOOO00O0OOO0O0000 ,OO0OO000OO00O0OO0 ))#line:99
    def priInitLogFilterKeyVoList (O000O00O00O0OO00O ,OOO000O0000O0OO0O ):#line:101
        O000O00O00O0OO00O .logFilterVoList =[]#line:102
        for OO000O0OO00OO00O0 in open (OOO000O0000O0OO0O +"resources/logFilter.txt",encoding ="utf-8"):#line:104
            O00OOOO00OO000O00 =OO000O0OO00OO00O0 .replace ("\n","").split (",")#line:105
            if len (O00OOOO00OO000O00 )==3 :#line:106
                O00OO00O0OOOO0O0O =O00OOOO00OO000O00 [0 ]#line:107
                OOOOOOO00O0000OOO =False if O00OOOO00OO000O00 [1 ]=="-"else True #line:108
                OO0O0OOOOOOOO000O =True if O00OOOO00OO000O00 [2 ]=="A"else False #line:109
                O000O00O00O0OO00O .logFilterVoList .append (LogFilterVo (O00OO00O0OOOO0O0O ,OOOOOOO00O0000OOO ,OO0O0OOOOOOOO000O ))#line:110
        return 1 #line:112
    def priGetLogFilterVo (O0O0OOO0O0OOO0O0O ,O0O0O00OOO0O0O0O0 ):#line:114
        for O0OO0O0O0OO0000O0 ,O0O0OO0000OOO0000 in enumerate (O0O0OOO0O0OOO0O0O .logFilterVoList ):#line:115
            if O0O0OO0000OOO0000 .logFilterKey ==O0O0O00OOO0O0O0O0 :#line:116
                return O0O0OO0000OOO0000 #line:117
        return None #line:118
class LogFilterVo :#line:121
    ""#line:122
    def __init__ (O00OO00OO0O00000O ,OOO0OO000O00OOOOO ,bOpen =False ,full =True ):#line:124
        ""#line:130
        O00OO00OO0O00000O .logFilterKey =OOO0OO000O00OOOOO #line:131
        O00OO00OO0O00000O .open =bOpen #line:132
        O00OO00OO0O00000O .full =full #line:133
LOG =LogUtilsEx ()#line:136
"""日志对象"""#line:137
if __name__ =="__main__":#line:141
    LOG .init ("../../../appqa/",True )#line:142
    LOG .debug ("WpRun","日志测试1...","调度器-L1-mesInit")#line:143
    LOG .info ("WpRun","日志测试2...","调度器-L1-mesInit")#line:144
    LOG .warn ("WpRun","日志测试3...","调度器-L1-mesInit")#line:145
    LOG .error ("WpRun","日志测试4...","调度器-L1-mesInit")#line:146
