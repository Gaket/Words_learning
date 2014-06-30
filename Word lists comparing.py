__author__ = 'Virt'
# -*- coding: utf-8 -*-

import re


def compare_words_lists(word_list1 = 'lingvaleo.txt', word_list2 = 'wordsteps.txt'):
    """
    This method compares two word lists, both must be text files,
    and prints words that contains one list but doesn't contain another
    for both lists

    :type word_list1: object
    :param word_list1: path to first text file
    :param word_list2: path to second text file
    """
    handle = open(word_list1, 'r')
    text1 = handle.read().lower()
    text1 = re.sub('[,.!?":;()*|<>{}0123456789]', '', text1)
    words1 = text1.split()

    handle = open(word_list2, 'r')
    text2 = handle.read().lower()
    text2 = re.sub('[,.!?":;()*|<>{}0123456789]', '', text2)
    words2 = text2.split()

    print "Слова, присутствующие в " + word_list1 + ", но отсутствующие в " + word_list2
    for word in words1:
        if not words2.__contains__(word):
            print word
    print "Слова, присутствующие в " + word_list2 + ", но отсутствующие в " + word_list1
    for word in words2:
        if not words1.__contains__(word):
            print word


if __name__ == '__main__':
    print('Do you like to input what text files do you want to compare?')
    print('By default, we use "lingvaleo.txt" and "wordsteps.txt"')
    mode = raw_input('1 - choose, other keys - default')
    if mode == 1:
        try:
            first_file = raw_input('Input first path to text file: \n')
            second_file = raw_input('Input second path to text file: \n')
            compare_words_lists(first_file, second_file)
        except:
            print "Please, import valid paths"
    else:
        compare_words_lists()

    raw_input('Press any key to continue')