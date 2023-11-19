import json #line:1
import random #line:2
import time #line:3
from basic import HttpUtilsEx #line:5
class ObfuscatorUtilsEx :#line:8
    URL ="https://pyob.oxyry.com/obfuscate"#line:11
    @staticmethod #line:17
    def run (O0O0000OOO0OOO0O0 ):#line:18
        ""#line:23
        O0O0O00000OO0OOO0 ={'content-type':'application/json'}#line:26
        O0OO00O00O0O0O00O =json .dumps ({"append_source":False ,"remove_docstrings":True ,"rename_nondefault_parameters":True ,"rename_default_parameters":False ,"preserve":"","source":O0O0000OOO0OOO0O0 })#line:34
        O00O00O0OOOOO0000 =HttpUtilsEx .post (ObfuscatorUtilsEx .URL ,O0O0O00000OO0OOO0 ,O0OO00O00O0O0O00O )#line:35
        time .sleep (random .randint (1 ,5 ))#line:36
        return O00O00O0OOOOO0000 ["dest"]#line:38
