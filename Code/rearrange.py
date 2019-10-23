import random 
import sys
words = sys.argv[1:]


def python_rearrange(words):
    last_index = len(words)
    updated_last_index = last_index - 1
    
    while updated_last_index > 0: 
        ran_index = random.randint(0, updated_last_index)
        save_word = words[ran_index]
        words[ran_index] = words[updated_last_index]
        words[updated_last_index] = save_word
        updated_last_index = updated_last_index - 1
    return words 

print(python_rearrange(words))

        








print(len(words))