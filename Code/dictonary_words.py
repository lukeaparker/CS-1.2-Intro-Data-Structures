import random 
import sys


def ran_word():
    arg = sys.argv[1:]
    val = int(arg[0])
    words = []
    f = open('/usr/share/dict/words', 'r')
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()
    for word in range(val):
        ran_index = random.randint(0, 235886)
        words.append(lines[ran_index])
    print(words)

ran_word()
