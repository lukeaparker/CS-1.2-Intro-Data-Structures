from dictogram import Dictogram
import utils
import random 
import os 
# import app
from pprint import pprint


class Markov(Dictogram):
    def build_markov(self, file_name):
        previous = None
        self.word_list = utils.get_words(file_name) 
        for word in self.word_list:
            if previous is None:
                previous = word
                continue
            if previous not in self:
                self[previous] = Dictogram()
            self[previous].add_count(word) 
            previous = word
        
    
    # def after_word_list(self, word):
    #     i = 0 
    #     pword_list = []
    #     for pword in self.word_list:
    #         i += 1
    #         if pword == word and i < len(self.word_list):
    #             pword_list.append(self.word_list[i])  
    #     return pword_list



    
    def sample_markov(self):
        ranum = random.random() * len(self.word_list)
        word = self.word_list[int(ranum)]
        sentence = [word]
        while len(sentence) <= 15:
            word = self[word].sample() 
            sentence.append(word)
        return sentence




class Markov2nd(Dictogram):
    def build_markov_2nd(self, file_name):
        self.word_list = utils.get_words(file_name)
        for sentence in self.word_list:
            self.build_sentence(sentence)

    
    def build_sentence(self, sentence):
        next_word_index = 0
        next_next_word_index = 1
        words = "i like dogs and you like dogs i like cats but you hate cats"
        for _ in range(2):
            sentence.insert(0, '$START$')
        for word in sentence:
            next_word_index += 1
            next_next_word_index += 1 
            if next_next_word_index >= len(sentence):
                break 
            if next_word_index < len(sentence):
                next_word = sentence[next_word_index]                    
            if next_next_word_index < len(sentence):
                next_next_word = sentence[next_next_word_index]
            pair = (word, next_word)
            if pair not in self:
                self[pair] = Dictogram()
            if pair in self:
                self[pair].add_count(next_next_word) 
        return self


    def sample_markov(self):
        previous = "$START$"
        current = "$START$"
        sentence = []

        while current != '$END$':
            next_word = self[(previous, current)].sample()
            previous = current
            current = next_word
            if current != '$END$': 
                sentence.append(next_word)
            elif current == '$END$':
                break
        return " ".join(sentence)

markov = Markov2nd()

markov.build_markov_2nd('src.txt')
markov.sample_markov()


            




            

            













    

# if __name__ == "__main__":
    # mv = Markov()
    # build = mv.build_markov()
    # print(build)
    # sample = mv.sample_markov()
    # print(sample)
    # mv = Markov2nd()
    # build = mv.build_markov_2nd('src.txt')
    # pprint(build)



            
    



        
