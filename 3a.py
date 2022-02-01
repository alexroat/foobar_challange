'''
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to 
make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to 
build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different 
types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different 
types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be 
lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of 
bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the 
second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or 
(3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be 
built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because 
Commander Lambda's not made of money!
'''

def test(expect,*parm):
    out=solution(*parm)
    print "%s : for input %s , output %s , should be %s"%(out==expect and "OK" or "FAIL",repr(parm),repr(out),repr(expect))


def plot(s):
    for i in s:
        print '#'*i


#function which compute the smaller base of a staircase
#it is derived from the gauss formula n=(n)+(b-1)+...+1=(n*(n+1))/2
b=lambda n:math.ceil((math.sqrt(8*n+1)-1)/2)




def solution(n):
    if n<3:
        return 0
    cnt=[-1]
    #print "----", n
    def crawl(s):
        #print s[1:], sum(s),len(s[1:])       
        cnt[0]+=1
        for i in xrange(s[-2]+1,(s[-1]+1)//2):
            crawl(s[:-1]+[i]+[s[-1]-i])
    crawl([0,n])
    return cnt[0]



def solution(n):
    if n<3:
        return 0
    cnt=[-1]
    def crawl(b,e,l=0):
        #print " "*l,b,e,e-b
        cnt[0]+=1
        for i in xrange(b+1,(e+1)//2):
            crawl(i,e-i,l+1)
    crawl(0,n)
    return cnt[0]

def solution(n):
    if n<3:
        return 0
    cnt=[0]
    def crawl(b,e,l=0):
        #print " "*l,b,e,e-b
        #cnt[0]+=1
        for i in xrange(b+1,(e+1)//2):
            crawl(i,e-i,l+1)
        d=(e+1)//2-(b+1)
        if d>0:
            cnt[0]+=d
    crawl(0,n)
    return cnt[0]

def solution(n):
    if n<3:
        return 0
    def crawl(b,e,l=0):
        #print " "*l,b,e,e-b
        #cnt[0]+=1
        n=1
        for i in xrange(b+1,(e+1)//2):
            n+=crawl(i,e-i,l+1)
        return n
    r=crawl(0,n)
    return r-1



def solution(n):
    cache={}
    if n<3:
        return 0
    def crawl(b,e,l=0):
        if (b,e) in cache:
            return cache[b,e]
        n=1
        for i in xrange(b+1,(e+1)//2):
            n+=crawl(i,e-i,l+1)
        cache[b,e]=n
        return n
    r=crawl(0,n)
    return r-1


#test(26,200)
#quit()

test(0,0)
test(0,1)
test(0,2)
test(1,3)
test(1,4)
test(2,5)
test(3,6)
test(4,7)
test(5,8)
test(7,9)
test(9,10)
test(11,11)
test(14,12)
test(17,13)
test(21,14)
test(26,15)
test(31,16)
test(37,17)
test(45,18)
test(53,19)
test(63,20)
test(487067745,200)

#import pylab
#data=[solution(i) for i in xrange(100)]
#pylab.plot(data)
#pylab.show()

#test(444792,100)
#test(444792,120)
#test(444792,200)
#test(0,200)















