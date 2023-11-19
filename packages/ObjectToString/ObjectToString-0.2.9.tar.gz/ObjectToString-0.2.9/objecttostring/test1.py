#!/usr/bin/env python3

import demo
import time
def progress( msg ):
    a=msg()
    print( "PROGRESS:", a.run() )
    pass

class a:
    def __init__(self):
        pass
    def run(self):
        return 1
        #pass
#print( demo.add( 1, 2 ) )
b=a()
a=demo.startthread( "3",a, thread=progress)
print(a)
print(demo.thread_lock())
print(demo.get_threadstatus(a))
print(demo.thread_unlock())
print(111)

