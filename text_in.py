#coding=utf-8
import uniout
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
def printl(text):
    fmt = '\033[0;3{}m{}\033[0m'.format
    for i in text:
        import random
        random.seed()
        time.sleep(0.05)
        print fmt(random.randint(0,7),i),
printl("hello,hacker")
print "\n"
printl("password:")
password=raw_input()
while password<>"mimashikong":
    printl("password:")
    password = raw_input()


print "\n"
printl("welcome\n")
printl("title:")
title=raw_input()
printl("title:"+title+"\n")
printl("content:")


from functools import partial
inputNew = partial(raw_input,'\n')
sentinel = 'end' # 遇到这个就结束
lines = ""
for line in iter(inputNew, sentinel):
    if lines=="":
        lines=line
    lines=lines+"\n"+line
printl(lines)
text='''
=====*=====
----------
***&*(***
===*
)(*
===*
----------
'''
a=open('text.txt', 'a')
a.write(text.replace("&*(",title).replace(")(*",lines))
a.close()