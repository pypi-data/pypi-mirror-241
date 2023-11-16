"""
__init__.py for lexio
"""

from lexio.core.lexio import language_processor, datasets, apply_sigmoid





def get_similarity_score(word: str, dictionary: list):


    """
    Returns the probability of being similar

    args:

    word (str): The word for which the similarity  is to be found

    dictionary (list): A list of words from which the similarity score is to be extracted

    USAGE:

    >>> dictionary = ['example', 'exam', 'exact', 'exagerrate']
    >>> word = 'exma'
    >>> get_similarity_score('exam', dictionary)
    out: array([0.73105858, 0.98201379, 0.88079708, 0.04742587])

    """
    scores = []

    for word in dictionary:
        corrects = 0
        wrongs = 0
        errors = 0
        for i, letter in enumerate(word):
            try:
                if letter.lower() == word[i].lower():
                    corrects += 1
                   # print(word[i], letter)
                else:
                    wrongs += 1
            except IndexError:
                errors += 1
               # print(word[i], letter)
           # print(corrects, wrongs)

        # Avoid division by zero
        if wrongs == 0:
            similarity_score = (corrects / 1) - ((abs(len(word) - len(word))))

        else:
            similarity_score = (corrects / wrongs) - ((abs(len(word) - len(word))))

        scores.append(similarity_score)


    return apply_sigmoid(scores)



def get_closest(word: str, dictionary: list):
    """
    Gets the closest match of the word from the dictionary passed.

    args:

    word (str): The word for which the closest match is to be found

    dictionary (list): A list of words from which the closest match of the word is to be extracted
    

    USAGE:

    >>> word = 'exma'
    >>> d = ['exam', 'example', 'exact']
    >>> lexio.get_closest(word, d)
    out: 'exam'


    """
    scores = get_similarity_score(word, dictionary)
    return dictionary[np.argmax(scores)]