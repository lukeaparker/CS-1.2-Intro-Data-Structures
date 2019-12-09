import sys 
import collections

def histogram_list(input):
    with open('src.txt', 'r') as file:
        data = file.read()
        text = data.split()
    histo = []
    for word in input:
        count = sum(word == s for s in text)
        cell = [word, count]
        if cell not in histo:
            histo.append(cell)
    return histo, len(text)

def histogram_tup():
    text = ['red', 'fish', 'two', 'fish', 'blue', 'fish']
    histog = []
    for word in text:
        count = sum(word == s for s in text)
        cell = (word, count)
        if cell not in histog:
            histog.append(cell)
    return histog

def histo_counts():
    histog = histogram_tup()
    histocount = {}
    for word, count in histog:
        if count in histcount: 
            histocount[count].append(word)
        else:
            histocount[count] = [word]




def histogram_dict(text):
    histo = {}
    for word in text:
        histo[word] = histo.get(word, 0) + 1
    return histo 

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





    


    




