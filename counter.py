# -*- coding: utf-8 -*-

import re
import os
from dictEn import *


def word_count_dict(text_files_list='Texts', dict_common_words=enTop500, dict_my_vocab=enVocabulary, min_count=0,  is_for_dict=False):
    """Returns a dictionary with key being number of counts
    and value being a list of words with that key.
    :type is_for_dict: object
    dictList is an optional argument: it is to eliminate
    the most common words. Default is the dictionary of
    the most common English words"""

    total_words = 0
    new_words = 0
    counts = dict()
    for text in text_files_list:
        handle = open(text, 'r')
        text = handle.read().lower()
        text = re.sub('[,.!?":;()*|<>{}0123456789]', '', text)
        words = text.split()

        """for word in words:
            if not word in count:
                count[word] = 1
        else:
            count[word] += 1"""
        for word in words:
            counts[word] = counts.get(word, 0) + 1
            total_words += 1

    print "New words:"
    for item in sorted(counts.items(), key=lambda (k, v): v, reverse=True):
        if (not dict_common_words.__contains__(item[0]) or is_for_dict is True) and item[1] >= min_count:
            # Как лучше? Вытащить проверку на словарь на уровень выше или оставить тут?
            if is_for_dict:
                print ('"' + item[0] + '",')
            else:
                new_words += 1
                if dict_my_vocab.__contains__(item[0]):
                    print (item[0] + ":   " + str(item[1]))
                else:
                    print (item[0].upper() + ": " + str(item[1]))

    print "Total words: " + str(total_words)
    print "New words with min " + str(min_count) + " counts: " + str(new_words)




# name = raw_input("Input path to file (Ex: C:/1.txt): ")

if __name__ == '__main__':  # if program was started like a script
    print('Do you like to choose texts directory and vocabularies?')
    print('Default - "Texts" dir, trash vocab - engTop100, learning - myVocab')
    #рассказать Свете, где были эти записи:
    user_path = 'Texts'
    user_trash = enTop1000
    user_vocab = enVocabulary
    user_min = 10
    choose = raw_input('"1" - Choose all \n"2" - Choose only directory \nOther key - default values\n')
    if choose == '1':
        user_path = raw_input('Input path to folder that contains text files (e.g."Texts" or C:/1):')
        user_trash = raw_input('Input name of most used words vocabulary:')
        user_vocab = raw_input('Input name of your words vocabulary:')
        user_min = raw_input("Input number of counts. Program will print only words with count >= this")
    elif choose == '2':
        user_path = raw_input('Input path to folder that contains text files (e.g."Texts" or C:/1):')

    text_files = []
    for root, dirs, files in os.walk(user_path):
            for f in files:
                text_files.append(os.path.join(root, f))
    word_count_dict(text_files, user_trash, user_vocab, user_min, False)

    raw_input("Print any key to exit")
    #compare_words_lists("lingvaleo.txt", "wordsteps.txt")