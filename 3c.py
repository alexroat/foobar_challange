'''
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

-- Java cases --
Input:
Solution.solution('4')
Output:
    2

Input:
Solution.solution('15')
Output:
    5

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''



def test(expect,*parm):
    out=solution(*parm)
    print "%s : for input %s , output %s , should be %s"%(out==expect and "OK" or "FAIL",repr(parm),repr(out),repr(expect))




def solution(n):
    cache={1:0,2:1}
    n=int(n)
    def crawl(n):
        if n in cache:
            return cache[n]
        if not n%2:
            cache[n]=crawl(n/2)+1
        else:
            cache[n]=min([crawl(n-1),crawl(n+1)])+1
        return cache[n]
    r=crawl(n)
    return r



def solution(n):
  n=int(n)
  c=0
  while n>1:
      if not n%2:
          n>>=1
      elif n==3 or n%4==1:
          n-=1
      else:
          n+=1
      c+=1
  return c
    
test(0,'0')
test(0,'1')        
test(1,'2')
test(2,'3')
test(2,'4')
test(5,'15')


test(0,105177)
test(0,1500000000000000020000200200202020)







