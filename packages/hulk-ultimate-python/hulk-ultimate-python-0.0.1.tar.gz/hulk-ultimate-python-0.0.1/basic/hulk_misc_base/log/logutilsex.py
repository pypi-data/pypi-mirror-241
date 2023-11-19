from loguru import logger #line:1
import os #line:2
import sys #line:3
sys .path .append (os .getcwd ())#line:5
TEMPLATE_FILE_LOG ="[{0}]{1}"#line:7
"""日志模板"""#line:8
class LogUtilsEx :#line:11
    ""#line:12
    def __init__ (O0O0OO00O00O00O00 ):#line:14
        ""#line:15
        O0O0OO00O00O00O00 .logFilterVoList =[]#line:17
        O0O0OO00O00O00O00 .logger =logger #line:20
    def init (O0OOOO0O0OOO00OOO ,dirPathRelativeConf ="",bDebug =False ,fileNameLog ="app.log",logRotationTime ="02:00"):#line:23
        ""#line:31
        OO000O0000000OO00 =dirPathRelativeConf +"resources/logs"#line:33
        if not os .path .exists (OO000O0000000OO00 ):#line:34
            os .makedirs (OO000O0000000OO00 )#line:35
        O000OOO0O0OOO0000 =os .path .join (OO000O0000000OO00 ,fileNameLog )#line:36
        O0OOOO0O0OOO00OOO .priInitLogFilterKeyVoList (dirPathRelativeConf )#line:39
        logger .remove ()#line:42
        O0O0OO00O0OO0O00O ="DEBUG"if bDebug else "INFO"#line:45
        logger .add (sys .stdout ,level =O0O0OO00O0OO0O00O )#line:46
        logger .add (O000OOO0O0OOO0000 ,rotation =logRotationTime ,level =O0O0OO00O0OO0O00O )#line:47
    def debug (OO0OO0OO00O00O0O0 ,O0O00OO0OOOO0O000 ,O0000OOO0000OO00O ,logFilterKey =""):#line:49
        ""#line:56
        O0OOOO0OOO00000O0 =OO0OO0OO00O00O0O0 .priGetLogFilterVo (logFilterKey )#line:57
        if O0OOOO0OOO00000O0 is not None and O0OOOO0OOO00000O0 .open is False :#line:58
            return #line:59
        LOG .logger .debug (TEMPLATE_FILE_LOG .format (O0O00OO0OOOO0O000 ,O0000OOO0000OO00O ))#line:60
    def info (O0O00O0OOOOO0OO0O ,OOO0O00O0O0O0OO00 ,OO0O00000O0OOOO00 ,logFilterKey =""):#line:62
        ""#line:69
        OOO000OO00OOO0OOO =O0O00O0OOOOO0OO0O .priGetLogFilterVo (logFilterKey )#line:70
        if OOO000OO00OOO0OOO is not None and OOO000OO00OOO0OOO .open is False :#line:71
            return #line:72
        LOG .logger .info (TEMPLATE_FILE_LOG .format (OOO0O00O0O0O0OO00 ,OO0O00000O0OOOO00 ))#line:73
    def warn (OO0OO0OOO00OO0000 ,OOO0OOO0000O00O0O ,OOOO00O00OO0O00OO ,logFilterKey =""):#line:75
        ""#line:82
        O00O0O00OO000O0O0 =OO0OO0OOO00OO0000 .priGetLogFilterVo (logFilterKey )#line:83
        if O00O0O00OO000O0O0 is not None and O00O0O00OO000O0O0 .open is False :#line:84
            return #line:85
        LOG .logger .warning (TEMPLATE_FILE_LOG .format (OOO0OOO0000O00O0O ,OOOO00O00OO0O00OO ))#line:86
    def error (OOO000OOOOOOO00O0 ,O00OOO0OO00OO0OO0 ,O00O0OOO0OOOO000O ,logFilterKey =""):#line:88
        ""#line:95
        O0OO000O0000OOOOO =OOO000OOOOOOO00O0 .priGetLogFilterVo (logFilterKey )#line:96
        if O0OO000O0000OOOOO is not None and O0OO000O0000OOOOO .open is False :#line:97
            return #line:98
        LOG .logger .error (TEMPLATE_FILE_LOG .format (O00OOO0OO00OO0OO0 ,O00O0OOO0OOOO000O ))#line:99
    def priInitLogFilterKeyVoList (O0OO0OOOOOO000OO0 ,OO00O0O0OO00O00OO ):#line:101
        O0OO0OOOOOO000OO0 .logFilterVoList =[]#line:102
        for O00000O000000O0OO in open (OO00O0O0OO00O00OO +"resources/logFilter.txt",encoding ="utf-8"):#line:104
            O0OOO00O000O000O0 =O00000O000000O0OO .replace ("\n","").split (",")#line:105
            if len (O0OOO00O000O000O0 )==3 :#line:106
                OO0OO00OOOOOO000O =O0OOO00O000O000O0 [0 ]#line:107
                OOOOOOO0O0O00O00O =False if O0OOO00O000O000O0 [1 ]=="-"else True #line:108
                O0OOO00O00OO000O0 =True if O0OOO00O000O000O0 [2 ]=="A"else False #line:109
                O0OO0OOOOOO000OO0 .logFilterVoList .append (LogFilterVo (OO0OO00OOOOOO000O ,OOOOOOO0O0O00O00O ,O0OOO00O00OO000O0 ))#line:110
        return 1 #line:112
    def priGetLogFilterVo (OOO00OO0O0OOO00O0 ,OO000OOO0O0O00O00 ):#line:114
        for O0000OOO0O000O00O ,OOOOO0O00OOOO0O00 in enumerate (OOO00OO0O0OOO00O0 .logFilterVoList ):#line:115
            if OOOOO0O00OOOO0O00 .logFilterKey ==OO000OOO0O0O00O00 :#line:116
                return OOOOO0O00OOOO0O00 #line:117
        return None #line:118
class LogFilterVo :#line:121
    ""#line:122
    def __init__ (OO0O00000OO0000O0 ,OOO0O0O00OO0OOO0O ,bOpen =False ,full =True ):#line:124
        ""#line:130
        OO0O00000OO0000O0 .logFilterKey =OOO0O0O00OO0OOO0O #line:131
        OO0O00000OO0000O0 .open =bOpen #line:132
        OO0O00000OO0000O0 .full =full #line:133
LOG =LogUtilsEx ()#line:136
"""日志对象"""#line:137
if __name__ =="__main__":#line:141
    LOG .init ("../../../appqa/",True )#line:142
    LOG .debug ("WpRun","日志测试1...","调度器-L1-mesInit")#line:143
    LOG .info ("WpRun","日志测试2...","调度器-L1-mesInit")#line:144
    LOG .warn ("WpRun","日志测试3...","调度器-L1-mesInit")#line:145
    LOG .error ("WpRun","日志测试4...","调度器-L1-mesInit")#line:146
