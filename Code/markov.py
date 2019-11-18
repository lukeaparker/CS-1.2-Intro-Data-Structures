import dictogram
import random 

class Markov(dict):
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov, self).__init__()  # Initialize this as a new dict
        self.word_list = ['one', 'fish', 'two', 'fish']

        def build_markov(self):
            previous = None
            for word in self.word_list:
                if previous is None:
                    prevoius = word
                    continue
                if previous not in self:
                    self[previous] = Dictogram()
                self[previous].add_count(word) 
        
        def sample_markov(self):
            ranum = random.random() * len(self.word_list)
            word = self.word_list[int(ranum)]
            sentence = [word]
            while len(sentence) <= 15:
                word = self[word].sample()
                sentence.append(word)
            return sentence
                 
            
            



             
        



            
