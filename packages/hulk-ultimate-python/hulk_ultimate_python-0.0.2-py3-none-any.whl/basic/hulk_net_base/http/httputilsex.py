import json #line:1
import requests #line:3
class HttpUtilsEx :#line:6
    ""#line:7
    @staticmethod #line:9
    def post (O0000OOO00O00OO0O ,O00OOOO0000OOOOOO ,OOOO0O000O00O0000 ):#line:10
        ""#line:17
        O0000O00O00O0O000 =requests .request ("POST",O0000OOO00O00OO0O ,headers =O00OOOO0000OOOOOO ,data =OOOO0O000O00O0000 )#line:18
        return json .loads (O0000O00O00O0O000 .text )#line:19
