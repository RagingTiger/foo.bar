#!/usr/bin/env python

'''
Author: John D. Anderson (TigerJ)
Usage: line_up_the_captives -case1 | -case2 | -n x.y.n
Origin: Google "foo.bar" project - Problem 4.1
Program Description:

    Line up the captives
    ====================

    As you ponder sneaky strategies for assisting with the great rabbit escape,
    you realize that you have an opportunity to fool Professor Booleans guards
    into thinking there are fewer rabbits total than there actually are.

    By cleverly lining up the rabbits of different heights, you can obscure the
    sudden departure of some of the captives.

    Beta Rabbits statisticians have asked you for some numerical analysis of
    how this could be done so that they can explore the best options.

    Luckily, every rabbit has a slightly different height, and the guards are
    lazy and few in number. Only one guard is stationed at each end of the
    rabbit line-up as they survey their captive population. With a bit of
    misinformation added to the facility roster, you can make the guards think
    there are different numbers of rabbits in holding.

    To help plan this caper you need to calculate how many ways the rabbits can
    be lined up such that a viewer on one end sees x rabbits, and a viewer on
    the other end sees y rabbits, because some taller rabbits block the view of
    the shorter ones.

    For example, if the rabbits were arranged in line with heights 30 cm,
    10 cm, 50 cm, 40 cm, and then 20 cm, a guard looking from the left side
    would see 2 rabbits (30 and 50 cm) while a guard looking from the right
    side would see 3 rabbits (20, 40 and 50 cm).

    Write a method answer(x,y,n) which returns the number of possible ways to
    arrange n rabbits of unique heights along an east to west line, so that
    only x are visible from the west, and only y are visible from the east.
    The return value must be a string representing the number in base 10.

    If there is no possible arrangement, return "0".

    The number of rabbits (n) will be as small as 3 or as large as 40
    The viewable rabbits from either side (x and y) will be as small as 1 and
    as large as the total number of rabbits (n).

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
    Output:
    (string) "2"

    Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
    Output:
    (string) "24"

    Use verify [file] to test your solution and see how it does. When you are
    finished editing your code, use submit [file] to submit your answer. If
    your solution passes the test cases, it will be removed from your home
    folder.
'''

# libraries
import sys


# functions
def answer(x, y, n):

    # bounds test
    if x + y > n + 1 or x + y < 3:
        return '0'

    # create factorial function
    def factorial(n):
        '''
        Function to calculate factorial of n value.
        '''
        if n == 0:
            return 1
        else:
            f = 1
            for i in range(2, n+1):
                f *= i
            return f

    # creating stirling triangle
    def gen_stirling(p, n):
        '''
        Function to create stirling numbers.
        '''
        # initialize [n k] = [0 0] to 1
        s = [1]

        # building stirling triangle
        for i in range(1, n + 1):
            # initialize k=0 partition to 0
            r = [0]
            for k in range(1, i):
                r.append((i-1)*s[k] + s[k-1])
            r.append(1)
            s = r[:]

        # return numbers
        return s[p]

    # calculate number of partitions
    left, right = x-1, y-1
    partitions = left + right

    # calcule number of partitioning rabbits
    rabbits = n-1

    # p coefficient named after Ping Guo who found it:
    # ref: https://github.com/PingGuo0201
    Ping = factorial(partitions)/(factorial(left)*factorial(right))

    # get stirling numbers
    S = gen_stirling(partitions, rabbits)

    # get X.Y.N combos
    return str(Ping * S)


# executable
if __name__ == '__main__':

    # usage info
    usage = '\nUsage: line_up_the_captives -case1 | -case2 | -n x.y.n\n'

    # CLA check
    if len(sys.argv) > 1:
        if sys.argv[1] == '-case1':
            x = 2
            y = 2
            n = 3

        elif sys.argv[1] == '-case2':
            x = 1
            y = 2
            n = 6

        elif sys.argv[1] == '-n':
            x, y, n = [int(x) for x in sys.argv[2].split('.')]
            print 'x={0}, y={1}, n={2}'.format(x, y, n)

        # wrong argument used
        else:
            sys.exit(usage)

        # correct arguments used
        print answer(x, y, n)
        sys.exit()

    # no argument passed
    sys.exit(usage)
