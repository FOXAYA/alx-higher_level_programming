#!/usr/bin/python3
"""Task 6. Find a peak"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        p = 0
        x = len(list_of_integers) - 1
        while p < x:
            mid = (p + x) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                x = mid
            else:
                p = mid + 1
        return list_of_integers[p]
