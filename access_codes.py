#!/usr/bin/env python

'''
Author: John D. Anderson (TigerJ)
Usage: access_codes -case1 | -case2 | -case3
Origin: Google "foo.bar" project - Problem 2.2
Problem Description:

    Access codes
    ============

    You've discovered the evil laboratory of Dr. Boolean, and you've found that
    the vile doctor is transforming your fellow rabbit kin into terrifying
    rabbit-zombies! Naturally, you're less-than-happy about this turn of events.

    Of course where there's a will, there's a way. Your top-notch assistant,
    Beta Rabbit, managed to sneak in and steal some access codes for
    Dr. Boolean's lab in the hopes that the two of you could then return and
    rescue some of the undead rabbits. Unfortunately, once an access code is
    used it cannot be used again. Worse still, if an access code is used,
    then that code backwards won't work either! Who wrote this security system?

    Your job is to compare a list of the access codes and find the number of
    distinct codes, where two codes are considered to be "identical"
    (not distinct) if they're exactly the same, or the same but reversed.
    The access codes only contain the letters a-z, are all lowercase, and have
    at most 10 characters. Each set of access codes provided will have at most
    5000 codes in them.

    For example, the access code "abc" is identical to "cba" as well as "abc."
    The code "cba" is identical to "abc" as well as "cba."
    The list ["abc," "cba," "bac"] has 2 distinct access codes in it.

    Write a function answer(x) which takes a list of access code strings, x,
    and returns the number of distinct access code strings using this definition
    of identical.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (string list) x = ["foo", "bar", "oof", "bar"]
    Output:
        (int) 2

    Inputs:
        (string list) x = ["x", "y", "xy", "yy", "", "yx"]
    Output:
        (int) 5

    Use verify [file] to test your solution and see how it does. When you are
    finished editing your code, use submit [file] to submit your answer.
    If your solution passes the test cases, it will be removed from your
    home folder.
'''

# libs
import sys

# functions
def answer(x):

    # starting index
    start = 0

    while start + 1 < len(x):

        # matches
        matches = []

        # iterate from starting point to end
        for i in range(start + 1, len(x)):
            if x[start] == x[i]:
                matches.append(i)
            elif x[start][::-1] == x[i]:
                matches.append(i)

        print 'Start: {0} | Matches: {1}'.format(x[start], matches)

        # delete matches
        for i, m in enumerate(matches):
            del x[m-i:m-i+1]


        # print results
        print 'Start: {0} | Values: {1}'.format(x[start], x)

        # next
        start+=1

    # return distinct access codes
    return len(x)


# executable
if __name__ == '__main__':

    if len(sys.argv) == 2:

        if sys.argv[1] == '-case1':
            x = ["foo", "bar", "oof", "bar"]
            print answer(x)

        elif sys.argv[1] == '-case2':
            x = ["x", "y", "xy", "yy", "", "yx"]
            print answer(x)

        elif sys.argv[1] == '-case3':
            x = ["a", "b", "c", "a", "a", "foo", "bar", "foo", "oof", "rab"]
            print answer(x)
