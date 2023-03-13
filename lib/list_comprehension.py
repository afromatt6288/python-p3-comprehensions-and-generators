#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return(evens)
    pass

def make_exclamation(sentence_list):
    return [f'{n}!' for n in sentence_list]
    # return [(n, end="!") for n in sentence_list]
    pass