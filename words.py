#!/usr/bin/env python

import argparse
import re

DEBUG=False

def score(word):
    scores={'j':10, 'q':10, 'z':10, 'x':8, 'd':2, 'n':2, 'l':2, 'u':2, 'h':3, 'g':3, 'y':3, 'b':4, 'c':4, 'f':4, 'm':4, 'p':4, 'w':4, 'v':5, 'k':5, }

    s=0
    for c in word:
        s+=scores[c] if c in scores else 1
    return s

def alpha(val):
    only_alpha=''

    ## looping through the string to find out alphabets
    for char in val.lower():

        ## checking for lower case
        if ord(char) >= 97 and ord(char) <= 122:
            only_alpha += char

    ## printing the string which contains only alphabets
    return(only_alpha)

def hashVal(val):
    hv=dict()
    for i in val:
        hv[i] = (hv[i]+1) if i in hv else 1
    return hv

def compHashes(word, chars):
    if DEBUG: print("compHashes {0} --- {1}".format(word,chars))
    isFailure = False
    numWildCards=chars['*'] if '*' in chars else 0

    if DEBUG: print('numWildCards = {}'.format(numWildCards))

    for key in word.keys():
        if DEBUG: print("number of wild cards = {0}".format(numWildCards))
        if DEBUG: print("key:{0} {1}".format(key, word[key]))
        if key not in chars or chars[key] < word[key]:
            if numWildCards >= word[key]:
                numWildCards -= word[key]
            else:
                isFailure = True

    return not isFailure

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='find a word in dictionary')
    parser.add_argument('regex', type=str, help='regular expressions to search for')
    parser.add_argument('characters', type=str, nargs='?', default='', help='characters in hand')
    parser.add_argument('--dict', dest='dictionary', type=str, help='dictionary to use', default='enable1.txt')
    #parser.add_argument('--debug', dest='dictionary', type=str, help='dictionary to use', default='twl.txt')

    args = parser.parse_args()
    the_dict=open(args.dictionary, 'r').read().splitlines()
    pattern = re.compile(args.regex)

    non_special_chars = alpha(args.regex)

    if DEBUG: print('non special chars in regex == "{0}"'.format(non_special_chars))
    hashChars=hashVal(args.characters+non_special_chars)

    if DEBUG: print(hashChars)
    if DEBUG: print('----------------')

    answers=[]
    for dict_item in the_dict:
        foo=pattern.search(dict_item)
        if foo is not None:
            if compHashes(hashVal(dict_item),hashChars):
                if DEBUG: print('ANSWER:  ',)
                #print(dict_item)
                answers.append(dict_item)

    answers.sort(key=len)
    answers.sort(key=score)
    [ print(a, score(a)) for a in answers ]
