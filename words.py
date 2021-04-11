#!/usr/bin/env python

import argparse
import re

DEBUG=False

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
    parser.add_argument('--dict', dest='dictionary', type=str, help='dictionary to use', default='twl.txt')
    #parser.add_argument('--debug', dest='dictionary', type=str, help='dictionary to use', default='twl.txt')

    args = parser.parse_args()
    the_dict=open(args.dictionary, 'r').read().splitlines()
    pattern = re.compile(args.regex)

    non_special_chars = alpha(args.regex)

    if DEBUG: print('non special chars in regex == "{0}"'.format(non_special_chars))
    hashChars=hashVal(args.characters+non_special_chars)

    if DEBUG: print(hashChars)
    if DEBUG: print('----------------')

    for dict_item in the_dict:
        foo=pattern.search(dict_item)
        if foo is not None:
            if compHashes(hashVal(dict_item),hashChars):
                if DEBUG: print('ANSWER:  ',)
                print(dict_item)
