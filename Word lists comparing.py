__author__ = 'Virt'
# -*- coding: utf-8 -*-

import re


def compare_words_lists(word_list1='Dictionaries/lingvaleo.txt', word_list2='Dictionaries/wordsteps.txt') -> int:
    """
    This method compares two word lists, both must be text files,
    and prints words that one list contains but another doesn't contain
    for both lists

    :param word_list1: path to first text file
    :param word_list2: path to second text file
    """
    if isinstance(word_list1, str) and isinstance(word_list2, str):
        handle = open(word_list1, 'r')
        text1 = handle.read().lower()
        text1 = re.sub('[,.!?":;()*|<>{}0123456789]', '', text1)
        words1 = text1.split()

        handle = open(word_list2, 'r')
        text2 = handle.read().lower()
        text2 = re.sub('[,.!?":;()*|<>{}0123456789]', '', text2)
        words2 = text2.split()

        print("Слова, присутствующие в " + word_list1 + ", но отсутствующие в " + word_list2)
        for word in words1:
            if word not in words2:
                print(word)
        print("Слова, присутствующие в " + word_list2 + ", но отсутствующие в " + word_list1)
        for word in words2:
            if word not in words1:
                print(word)
        return 0


if __name__ == '__main__':
    print('Do you like to input what text files do you want to compare?')
    print('By default, we use "Dictionaries/lingvaleo.txt" and "Dictionaries/wordsteps.txt"')
    mode = input('1 - choose, other keys - default \n')
    if mode == '1':
        try:
            first_file = input('Input first path to text file: \n')
            second_file = input('Input second path to text file: \n')
            compare_words_lists(first_file, second_file)
        except FileNotFoundError:
            print('Error. Please, import valid paths')
    else:
        compare_words_lists()
    input('Press any key to continue')