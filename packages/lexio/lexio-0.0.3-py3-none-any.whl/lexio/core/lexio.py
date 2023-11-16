#Importing a necessary library called numpy 

import numpy as np
from lexio.core import  dataset  #'dataset' is not a library but rather -  
                # - a python file that contains some datasets and stopwords
import string

class language_processor():

    def __init__(self):
        self.about = dataset.about
        self.get_stopwords = dataset.stopwords


    def letter_similarity(self, word1, word2):
        max_length, min_len, long_word, short_word = self.max_len(word1, word2)
        small_word_letters = list(short_word)
        big_word_letters = list(long_word)
        similars = []
        for letter in small_word_letters:
            if letter in big_word_letters:
                similars.append(letter)
                
        return len(similars) / max_length
        

    def max_len(self, word1, word2):
        if len(word2) < len(word1):
            max_len = len(word1)
            long_word = word1
            short_word = word2
            min_len = len(word2)
        else:
            max_len = len(word2)
            long_word = word2
            short_word = word1
            min_len = len(word1)
        return max_len, min_len, long_word, short_word


#a = 'apple'
#b = 'app'
#print(max_len(a, b))
#print(letter_similarity(a, b))


    

    def tokenize(self, text, return_list=False):
        text = text.lower()
        stopwords = dataset.stopwords
        punctuations = list(string.punctuation)
        punctuations.append('\n')
        for punctuation in punctuations:
            text = text.replace(punctuation, ' ')
        text_preprocessed = []
        for word in text.split(' '):
            text_preprocessed.append(word.strip())
        
        for word in text_preprocessed:
            if word == '' or word == ' ' or word in stopwords: #or word in stopwords:
                text_preprocessed.remove(word)
        text_preprocessed = [word for word in text_preprocessed if word.strip() and word not in stopwords]

        if return_list == False:
            return ' '.join(text_preprocessed)
        else:
            return text_preprocessed


    def max_pos(self, lis):
        m = np.max(lis)
        for i in range(len(lis)):
            if lis[i] == m:
                return i


    def get_topic(self, txt, tokenized=False):

        if type(txt) is list: 

            if tokenized is False:
                text = ' '.join(text)
                text = self.tokenize(txt, return_list=False)
                text_as_words = text.split(' ')
            else:
                text_as_words = txt
        else:
            text = self.tokenize(txt, return_list=True)
            text_as_words = text 
        popularity_dict = {}
        for word in text_as_words:
            if word in popularity_dict:
                popularity_dict[word] += 1 
            else:
                popularity_dict[word] = 1
        #return popularity_dict

        hot_words = list(popularity_dict.keys())
        hot_values = list(popularity_dict.values())
        popular_word_value = max(hot_values)
        for idx, value in enumerate(hot_values):
            if value == popular_word_value:
                return hot_words[idx]
        #return topic

    def highlights(self, text, highlights=10):
        text = self.tokenize(text)
        text_as_words = text.split(' ')
        popularity_dict = {}
        for word in text_as_words:
            if word in popularity_dict:
                popularity_dict[word] += 1 
            else:
                popularity_dict[word] = 1
        hot_words = list(popularity_dict.keys())
        hot_values = list(popularity_dict.values())
        hot_indices = (np.argsort(hot_values))[::-1]
        hot_vals = np.argsort(hot_values)[::-1]
        most_populars = [hot_words[idx] for idx in hot_indices][:highlights]
        most_populars_value = [hot_values[idx] for idx in hot_vals][:highlights]
        return dict(zip(most_populars, most_populars_value))

    def summarize(self, text):
        tokenized = self.tokenize(text)
        n = int(20 / len(tokenized.split(' ')) * 100)
        highlights = self.highlights(tokenized, highlights=n)
        return ' '.join(list(highlights.keys()))

"""
    def word_root(self, words):
        if not isinstance(words, list):
            return None

        suffixes_to_remove = ['ment', 'less', 'able', 'less', 'ness', 'ful', 'est', 'ing', 'ly', 'er', 'ed', 's']
        words_rooted = []"""

def apply_sigmoid(scores):
    # Apply sigmoid function element-wise to each score
    sigmoid_scores = 1 / (1 + np.exp(-np.array(scores)))
    return sigmoid_scores
 


class datasets():
        load_apple = dataset.load_apple  
        load_earth = dataset.load_earth
        load_AI = dataset.load_AI
        load_nepal = dataset.load_nepal
        load_discipline = dataset.load_discipline
        load_essay_AI = dataset.load_essay_AI
        load_nature = dataset.load_nature
        load_google = dataset.load_google   
        availables = ['load_apple', 'load_earth', 
        'load_nepal', 'load_AI', 'load_discipline', 'load_essay_AI', 'load_nature', 'load_google']

    
if __name__ == '__main__':
    text = "lexIO is a Natural Language Processing (NLP) library in python"
    processor = language_processor()
    print(processor.get_topic(text))
    print(processor.highlights(text, highlights=5))
    print(datasets.availables)
