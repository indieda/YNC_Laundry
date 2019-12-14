#Learning1
'''
addr_var = ['00:15:f4:34:a5:4b','d6:58:12:5b:00:0g']
test=[]

for ii in range(len(addr_var)):
    test.append(0)

print(test)'''

#learning2
'''
def s1(add) :
    z = s2(add)
    i = add
    print(i)

def s2(add):
    try:
        1+2
        return
    except:
        pass
    

s1(1)
'''

#LEarning 3
'''
from concurrent import futures
import os
l=[1,2]
def test(a):
    b = a+1
    print(b)

ex = futures.ProcessPoolExecutor(max_workers = os.cpu_count())
results = ex.map(test,l)
'''

"""
Learning4
IS this a shortcut to include a condition to print something? Found from Bluepy's waitForNotifications function.
Learning


return (resp != None)"""


#Learning 5
"""
def bleh(a):
    return (None != None)

print(bleh(1))
"""
# Learning 6: Use of Global variables within functions.
"""
https://www.programiz.com/python-programming/global-local-nonlocal-variables
If we had:
    
x=1
def test(bleh)
    x+1
    print()

It will throw an error that the function's x is not readable by the x called outside the function.ArithmeticError
Instead, to access the x from outside while within the function, we need to edit the code to look like this:

x=1
def test(bleh)
    global x """Notice this global"""
    x+1
    print()
"""
