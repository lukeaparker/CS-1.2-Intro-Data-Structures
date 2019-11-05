import random
import sys 
from histogram import histogram

    

def get_word(histogram):
    histo, corp_length = histogram()
    index = int(random.random()*corp_length)
    summed = 0
    for word, freq in histo:
        summed += freq
        if summed > index:
            return word


# from collections import Counter
# print(Counter([get_word(histogram) for _ in range(10000)]))
        



if __name__ == "__main__":
    get_word(histogram)










   
    



        


