#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        value = a_dictionary.get(key)
        print('{}: {}'.format(key, value))
