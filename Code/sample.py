import random 
import sys 
from histogram import histogram

def random_word(histogram):
    histo = histogram()
    randint = random.randint(0, 4)
    print(histo[randint])
    return histo[randint]

def random_word_anaylsis():
    random_word(histogram)
    
random_word_anaylsis()







   
    



        


