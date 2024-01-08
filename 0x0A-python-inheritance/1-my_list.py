#!/usr/bin/python3
"""
   1-my_list
   Class MyList that inherits from list that contain \
   Public instance method: def print_sorted(self): that \
   prints the list, but sorted (ascending sort)
"""


class MyList:
    """MyList that inhertance from list"""
    def print_sorted(self):
        """Method prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
