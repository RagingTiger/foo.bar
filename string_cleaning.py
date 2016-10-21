#!/usr/bin/env python

'''
Author: John D. Anderson (TigerJ)
Usage: string_cleaning [-m chunk word] -case1|case2|case3
Origin: Google "foo.bar" project - Problem 3.2
Problem Description:

    String cleaning
    ===============

    Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists
    who are turning rabbits into zombies. He sends a text transmission to you,
    but it is intercepted by a pirate, who jumbles the message by repeatedly
    inserting the same word into the text some number of times. At each step,
    he might have inserted the word anywhere, including at the beginning or end,
    or even into a copy of the word he inserted in a previous step. By offering
    the pirate a dubloon, you get him to tell you what that word was. A few
    bottles of rum later, he also tells you that the original text was the
    shortest possible string formed by repeated removals of that word, and that
    the text was actually the lexicographically earliest string from all the
    possible shortest candidates. Using this information, can you work out what
    message your spy originally sent?

    For example, if the final chunk of text was "lolol," and the inserted word
    was "lol," the shortest possible strings are "ol" (remove "lol" from the
    beginning) and "lo" (remove "lol" from the end). The original text therefore
    must have been "lo," the lexicographically earliest string.

    Write a function called answer(chunk, word) that returns the shortest,
    lexicographically earliest string that can be formed by removing occurrences
    of word from chunk. Keep in mind that the occurrences may be nested, and
    that removing one occurrence might result in another. For example, removing
    "ab" from "aabb" results in another "ab" that was not originally present.
    Also keep in mind that your spy's original message might have been an empty
    string.

    chunk and word will only consist of lowercase letters [a-z].
    chunk will have no more than 20 characters.
    word will have at least one character, and no more than the number of
    characters in chunk.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (string) chunk = "lololololo"
        (string) word = "lol"
    Output:
        (string) "looo"

    Inputs:
        (string) chunk = "goodgooogoogfogoood"
        (string) word = "goo"
    Output:
        (string) "dogfood"

    Use verify [file] to test your solution and see how it does. When you are
    finished editing your code, use submit [file] to submit your answer. If your
    solution passes the test cases, it will be removed from your home folder.

--------------------------------------------------------------------------------

SOLUTION: Tree Data Structure

    Description: A tree structure is generated from all possible
                 combinations. The "del i" command simply means
                 "delete" the given "word" at the "ith" instance.

                 Example:

                     chunk = lololololo
                     word = lol

                         lololololo
                              |
                      - del 1 |_olololo

                      NOTE: del 1 removed "lol"olololo
                            from the chunk, leaving the
                            remaining "olololo" chunk

    FULL SOLUTION:

        lololololo
            |
 -split 1   |________oloo
            |
 -split 2   |________looo
            |
 -split 3   |________oolo
            |
 -split 4   |________looo

'''
# libs
import sys


# funcs
def answer(chunk, word):

    # print initial start
    print 'Starting Values: {0} {1}'.format(chunk, word)

    # messages
    messages = []

    # word/chunk length
    wlen = len(word)

    # recursively scan word
    def recursive_chunk(chunkee, word):

        # chunk size
        clen = len(chunkee)

        # check chunk
        for i, _ in enumerate(chunkee):

            if chunkee[i:i+wlen] == word:
                new_chunk = chunk[0:i].replace(word, '') \
                            + chunk[i+wlen:clen].replace(word, '')
                if new_chunk.find(word) < 0:
                    messages.append(new_chunk)
                else:
                    recursive_chunk(new_chunk, word)

    # start recursion
    recursive_chunk(chunk, word)

    # sort/return
    messages.sort()
    return messages[0]


# executable
if __name__ == '__main__':

    # check CLA
    if len(sys.argv) == 2:

        if sys.argv[1] == '-case1':
            print '\nFinal List: {0}'.format(answer('aaabbb', 'ab'))
            sys.exit()

        elif sys.argv[1] == '-case2':
            print '\nFinal List: {0}'.format(answer('lololololo', 'lol'))
            sys.exit()

        elif sys.argv[1] == '-case3':
            print '\nFinal List: {0}'.format(answer('goodgooogoogfogoood',
                                                    'goo'))
            sys.exit()

    elif len(sys.argv) > 3:
        if sys.argv[1] == '-m':
            print '\nFinal List: {0}'.format(answer(sys.argv[2], sys.argv[3]))
            sys.exit()

    sys.exit('\nusage: string_cleaning [-m chunk word]'
             ' -case1|case2|case3')
