import sys 
import collections

def histogram(src_txt):
    f = open('src_txt.txt', 'r')
    lines = f.readlines()
    f.close()
    key = sys.argv[1:]
    keyword = str(key)
    count = sum(keyword in s for s in lines)
    print(keyword)
histogram('src_txt.txt')





