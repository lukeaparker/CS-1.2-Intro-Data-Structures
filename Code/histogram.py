import sys 
import collections
import sample

def histogram():
    words = ""
    with open('src.txt', 'r') as file:
        data = file.read()
        text = data.split()
    histo = []
    for word in words:
        count = sum(word == s for s in text)
        cell = [word, count]
        if cell not in histo:
            histo.append(cell)
    return histo, len(text)


def unique_word_count(histogram):
    histo = histogram()
    total = []
    for list in histo:
        total.append(list[1])
    total = sum(total)
    return total 




# input:
#   word = "apple"
#   histogram = [['apple', 3], ['grapes', 2]]
# output -- 3
def frequency(word, histogram):
    histo = histogram()
    word = sys.argv[1:]
    word_frequency = 0
    for list in histo:
        if word[0] in list:
            word_frequency = list[1]
    return word_frequency
# frequency('jj', histogram)





    


    




