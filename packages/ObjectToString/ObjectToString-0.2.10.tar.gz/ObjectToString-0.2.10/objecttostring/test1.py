# -*- coding: gbk -*-
import  sys
#import demo
import time
#import psycopg2
import pglib

#@cython.nogil
#@cython.cfunc
def progress( msg ):
    try:

        #con=a.getcon()
        #cur = con.cursor()
        #cur.execute('select  * from test')
        #records = cur.fetchall()
        #cur.execute('insert into  test( tt) values (2);')
        #con.commit()
        print( "PROGRESS:" )
        while 1:
            time.sleep(3)
            print(6666666666666)
            break
        print(7777777777)
        pass
    except Exception as e:
        print(e)
        pass

class a:
    def __init__(self):
        #self.con = psycopg2.connect(dbname='pds', user='postgres', password='123456', host='127.0.0.1')
        #self.cur = self.con.cursor()
        pass
    def getcon(self):
        #return self.con
        pass
    def run(self):
        return 6666
        pass
#print( demo.add( 1, 2 ) )
th=[]
thradnum=100
for i in range(thradnum):
    cc1=pglib.pglibconn("127.0.0.1",5432,'pds', 'postgres', '123456',i)
    if cc1!=-1:
        th.append(cc1)

for i in th:
    print(pglib.pglibselect("SELECT * FROM \"public\".\"test\" LIMIT 10",i))
l=[]
thradnum_real=len(th)
for i in range(5000):
    l.append("insert into  test (tt,bb) values(1,'你好')")
    l.append("insert into  test (tt,bb) values(1,'你好')")

for i in th:
    if i!=-1:
        print(pglib.pglibinsert(l,i))
#print(pglib.pglibselect("SELECT * FROM \"public\".\"test\" LIMIT 1",cc))

while 1:
    time.sleep(1)
    lex = []
    for tt in th:
        #print("status :%d" % pglib.getthreadstatus(tt))
        if pglib.getthreadstatus(tt)==2:
            lex.append(tt)
    if lex.__len__()==thradnum_real:
        break

for i in th:
    pglib.pglibclose(i)

#b=a()
#a1=demo.startthread( "3",a, thread=progress)
#print(a1)
'''
for i in range(2):
    #(demo.thread_lock())
    #dddd=demo.get_threadstatus(a1)
    #print(dddd)
    print(99999999)
    time.sleep(1)
    pass
    #(demo.thread_unlock())
print(111)

'''