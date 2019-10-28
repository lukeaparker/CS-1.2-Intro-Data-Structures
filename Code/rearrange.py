import random 
import sys


def python_rearrange(words):
    words = sys.argv[1:]
    last_index = len(words)
    updated_last_index = last_index - 1
    s = " "
    
    while updated_last_index > 0: 
        ran_index = random.randint(0, updated_last_index)
        words[ran_index], words[updated_last_index] = words[updated_last_index], words[ran_index]
        # save_word = words[ran_index]
        # words[ran_index] = words[updated_last_index]
        # words[updated_last_index] = save_word
        updated_last_index = updated_last_index - 1
    s = s.join(words)
    print(s)

python_rearrange(sys.argv[1:])


        








