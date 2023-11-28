#!/usr/bin/python3
for item in range(ord('a'), ord('z') + 1):
    if item != ord('e') and item != ord('q'):
        print("{:c}".format(item), end="")
