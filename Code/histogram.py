import sys 
import collections

def histogram():
    words = sys.argv[1:]
    with open('src.txt', 'r') as file:
        data = file.read()
        text = data.split()
    histo = []
    for word in words:
        count = sum(word == s for s in text)
        cell = [word, count]
        histo.append(cell)
    return histo


def unique_word_count(histogram):
    histo = histogram()
    total = []
    for list in histo:
        total.append(list[1])
    total = sum(total)
    print(total)
    return total 



unique_word_count(histogram)    

# input:
#   word = "apple"
#   histogram = [['apple', 3], ['grapes', 2]]
# output -- 3
def frequency(word, histogram):
    word = sys.argv[1:]
    with open('src_txt.txt', 'r') as file:
        data = file.read()
        text = data.split()
    frequency = sum(word == s for s in text)
    return frequency

    


    




