'''
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

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
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''

from fractions import Fraction

def mPrint(m):
    for r in m:
        print ",".join(map(str,r))
    print

def mEye(n):
    return [[n]*n for _ in xrange(n)]

mDot=lambda a,b:[ [ sum(map(lambda (u,v): u*v,zip(i,j))) for i in zip(*b)] for j in a]
mDotV= lambda m,v: zip(*mDot(m,zip(*[v])))[0]

def mTranspose(m):
    return map(list,zip(*m))

def mMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def mDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*mDeterminant(mMinor(m,0,c))
    return determinant

def mInverse(m):
    determinant = Fraction(mDeterminant(m))
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = mMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * mDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = mTranspose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors




def gcd(l):
    def _gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    d=l[0]
    for i in xrange(1,len(l)):
        d=_gcd(d,l[i])
    return d

def mcm(l):
    def _mcm(x,y):
        return x*y/gcd([x,y])
    m=l[0]
    for i in xrange(1,len(l)):
        m=_mcm(m,l[i])
    return m


def rescale(v):
    d=gcd(v)
    return map(lambda x:x/d,v)

def solution(m):
    n=len(m)
    if not any(m[0]):
        return [1,1]
    #find the terminal states and fix the values
    terminals=[i for i,v in enumerate(m) if sum(v)==0]   
    for i in terminals:
        m[i][i]=1
    #sort standard form
    smap=sorted(xrange(n),key=lambda i:i not in terminals)
    nt=len(terminals)
    m=mTranspose(m)
    m=[m[smap[i]] for i in xrange(n)]
    m=mTranspose(m)
    m=[m[smap[i]] for i in xrange(n)]
    #normalize probabilities
    sums=map(sum,m)
    m=[[Fraction(c,sums[i]) for c in r] for i,r in enumerate(m)]
    #extract R and Q matrix
    mr=[ [c for c in r[:nt] ] for r in m[nt:]]
    mq=[ [c for c in r[nt:] ] for r in m[nt:]]
    #compute fundamental matrix
    nnt=n-nt
    tmf=[[ (i==j)-mq[i][j] for j in xrange(nnt) ] for i in xrange(nnt)]
    mf=mInverse(tmf)
    mfr=mDot(mf,mr)
    sol=mfr[0]
    dprod=reduce(lambda a,x:a*x.denominator,sol,1)
    sol=rescale(map(lambda x:int(x*dprod),sol))
    return sol+[sum(sol)]
    


def test(expect,*parm):
    out=solution(*parm)
    print "%s : for input %s , output %s , should be %s"%(out==expect and "OK" or "FAIL",repr(parm),repr(out),repr(expect))







test([0, 3, 2, 9, 14],[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
])

test([7, 6, 8, 21],[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
test([0, 3, 2, 9, 14],[[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

test([1,1],[[0, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])







