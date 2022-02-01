'''
Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambdas collapsing space station in an escape pod with the rescued bunny prisoners - but Commander Lambda isnt about to let you get away that easily. She's sent her elite fighter pilot squadron after you - and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Commander Lambdas assistant, she asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution('77')
Output:
    4208

Input:
Solution.solution('5')
Output:
    19

-- Python cases --
Input:
solution.solution('77')
Output:
    4208

Input:
solution.solution('5')
Output:
    19

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''


def test(expect,*parm):
    out=solution(*parm)
    print "%s : for input %s , output %s , should be %s"%(out==expect and "OK" or "FAIL",repr(parm),repr(out),repr(expect))

import math

def solution(str_n):
    n=int(str_n)
    s2=math.sqrt(2)
    s2r=s2-1
    print int(n*s2)
    print int(n)+int(s2r*n)
    r=sum(map(lambda x: int(x*s2),xrange(1,n+1)))
    return r


import math
from decimal import Decimal, localcontext

def solution(str_n):
    n=int(str_n)
    a=0
    with localcontext() as ctx:
        ctx.prec = 101
        a=Decimal(2).sqrt()
    def s(a,n):
        if not n:
            return 0
        np=int(n*(a-1))
        q=n*np+n*(n+1)/2-np*(np+1)/2
        return q-s(a,np)
    return str(s(a,n))

import math
from decimal import Decimal, localcontext,ROUND_FLOOR

dfoor=lambda x:Decimal(str(x).split(".")[0])

def solution(str_n):
    #applying https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
    #sum of beatty sequence BUT we need to take care about the error
    #float and int are not enough, we need to pass to Decimal with enough precision
    with localcontext() as ctx:
        ctx.prec = 1000
        #ctx.rounding = ROUND_FLOOR
        d2=Decimal(2)
        d1=Decimal(1)
        d0=Decimal(0)
        a=d2.sqrt()
        n=Decimal(str_n)
        def s(a,n):
            if not n:
                return d0
            np=dfoor(n*(a-d1))
            q=n*np+n*(n+d1)/d2-np*(np+d1)/d2
            return q-s(a,np)
        return str(s(a,n))



test('12','4')
test('4208','77')
test('19','5')
test('0','9'*101)



'''
for i in xrange(100):
    print i,solution(str(i))
'''




