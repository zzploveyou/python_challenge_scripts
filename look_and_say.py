# coding:utf-8
'''
look and say sequence
1 -> 11 one 1,
11 -> 21 two 1,
21 -> 1211 one 2, one 1(1211)

Problem:
    find the length of 30th of the sequence

index, length
0, 1
1, 2
...
30, 5808
50, 1166642
60, 16530884
'''
import sys


def look_and_say(string):
    new_string = ""
    num = 1
    temp = string[0]
    for idx in range(1, len(string)):
        if string[idx] == temp:
            num += 1
        else:
            new_string += str(num) + temp
            temp = string[idx]
            num = 1
    new_string += str(num) + temp
    return new_string

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print "Usage: python %s %s" % (__file__, 10)
        sys.exit(1)
    MAX_LENGTH = int(sys.argv[1])
    string = '1'
    tick = 0
    print "tick: %d -> len: %d" % (tick, len(string))
    tick = 1
    while tick <= MAX_LENGTH:
        string = look_and_say(string)
        # print string,
        print "tick: %d -> len: %d" % (tick, len(string))
        tick += 1

    # print len(string)
