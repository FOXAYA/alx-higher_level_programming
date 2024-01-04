#!/usr/bin/env python3
"""
Solving the N Queens problem in Python.
https://en.wikipedia.org/wiki/N_queens_problem

It's easy to take the brute-force approach to solve the N Queens problem:
generate every possible position for the N queens, and check which ones work.
However, the brute-force approach quickly becomes unusably slow:
there are 4,426,165,368 (over 4 billion) possible combinations for N=8.
Too many to check in a reasonable amount of time!

Rather than generating every possible position for all queens, we place one
queen on the board at a time. Each time we place a queen, we take a look at
the board and see which positions are still available for the next queen to go.
If we manage to place the last queen, then great: we have a solution! However,
if we've run out of places on the board before placing the last queen, then
we must back-track -- pick up the most recently-placed queen, and move her to
a different position before placing the next one. This is a recursive
algorithm, and it makes the solution quite elegant.

This code is extensively commented, to explain the logic one step at a time.
If you want to know how it works, keep reading!
"""
__author__ = "David Baumgold <david@davidbaumgold.com>"

import itertools


def remaining_positions(board, size):
    """
    This function looks at the current state of the board, and determines
    which positions are still available for placing the next queen.
    If the board is empty, then every position is available!

    Args:
        board (frozenset): The set of (x, y) tuples where queens have
            already been placed on the board. To represent an empty board,
            pass an empty set.
        size (int): The number of rows and columns this board has.

    Returns:
        generator: A generator of (x, y) positions, where each position
            does not conflict with any existing queen on the board.
    """
    # There can only be one queen per row.
    # Generate all rows, and remove the ones that are taken.
    taken_rows = frozenset(x for x, y in board)
    free_rows = (x for x in range(size) if x not in taken_rows)
    # There can only be one queen per column.
    # Generate all columns, and remove the ones that are taken.
    taken_columns = frozenset(y for x, y in board)
    free_columns = (y for y in range(size) if y not in taken_columns)
    # Make a generator of positions that have free rows and free columns.
    free_row_col = itertools.product(free_rows, free_columns)
    # There can only be one queen per diagonal, in either direction.
    # There are two kinds of diagonals:
    # bottom left to top right, and top left to bottom right.
    # By adding together the two coordinates of the position,
    # we get a number that corresponds to the first kind of diagonal.
    taken_first_diagonals = frozenset(x + y for x, y in board)
    # By subtracting one coordinate from the other,
    # we get a number that corresponds to the second kind of diagonal.
    taken_second_diagonals = frozenset(x - y for x, y in board)
    # Return a new generator that filters out the positions
    # that conflict with existing queens on either diagonal.
    return (
        (x, y) for x, y in free_row_col
        if x + y not in taken_first_diagonals
        and x - y not in taken_second_diagonals
    )


def ordered_remaining_positions(board, size):
    """
    This function is a wrapper around the `remaining_positions` function.
    It uses an arbitrary ordering function to filter the output, and only
    allows positions that are greater than any other position already on
    the board. In this case, the arbitrary ordering function is the
    row of the position, but you could use any ordering function you want
    to fulfill the same purpose.

    The main reason we use this wrapper is to avoid duplicate solutions.
    The set {A, B} is exactly the same as the set {B, A}, but without
    a way to order our responses, both responses will be generated. The first
    will occur when we start with the set {A} and add B to it; the second
    will occur when we start with the set {B} and add A to it. However,
    if we say that position B is "greater" than position A, and we only allow
    adding a value to a set when the new value is greater than any existing
    value in the set, then this problem goes away. If we start with
    the set {A}, then we can add B to it, because B is greater than A.
    But if we start with the set {B}, we *cannot* add A to it, because A is
    *not* greater than B.

    In addition to avoiding duplicate solutions, this also gives us a big
    performance boost. Because we are dramatically reducing the number of
    options to search at each step, the amount of time required to search
    all the options also goes down dramatically.

    Args:
        board (frozenset): The set of (x, y) tuples where queens have
            already been placed on the board. To represent an empty board,
            pass an empty set, or None.
        size (int): The number of rows and columns this board has.

    Returns:
        generator: A generator of (x, y) positions, where each position
            does not conflict with any existing queen on the board,
            and each position is greater than any other already on
            the board with respect to an arbitrary ordering function.
    """
    # Find the maximum row number of all the queens on the board.
    # If no queens have been placed, use -1: every row is larger than that!
    if board:
        max_x = max(x for x, y in board)
    else:
        max_x = -1
    # Call the `remaining_positions` function, and filter the results
    # so that we only return positions where the row number of the position
    # is greater than the maximum row number of all the queens on the board.
    return (
        (x, y) for x, y in remaining_positions(board, size)
        if x > max_x
    )


def nqueens(size=8, board=None):
    """
    This is our main function. To generate all solutions to the 8 Queens
    puzzle, call it with the default arguments. To use a different size board,
    set the `size` argument to the number you want. Generally, you want
    to leave the second argument blank, but if you want to place a few queens
    on the board before calling this function, you can do so.

    Args:
        size (int): The number of rows and columns this board has.
            This defaults to 8, because the 8 Queens puzzle is the most
            common version of this problem.
        board (frozenset): The set of (x, y) tuples where queens have
            already been placed on the board. To represent an empty board,
            pass an empty set, or None. Generally we want to start with
            an empty board, so this argument defaults to None.

    Returns:
        generator: A generator of solution sets. Each solution set
            contains (x, y) coordinates where queens may be placed on the board
            without conflicting with any other queen.
    """
    # Make sure we have a set, rather than None
    board = board or frozenset()
    # This solution uses recursion, which requires a base case:
    # somewhere for the recursive calls to stop. This is that base case.
    # If we have as many queens on the board as rows/columns, then we can't
    # place any more, so stop and yield this solution.
    if len(board) == size:
        yield board
    # Here, we're going to use the `ordered_remaining_positions` function that
    # we defined earlier to get all possible locations that we could place
    # one more queen on the board, and iterate through them.
    for position in ordered_remaining_positions(board, size):
        # Try placing a new queen in this position, which will mean
        # generating a new board state.
        new_board = board.union((position,))
        # Make the recursive call with the new board state.
        # If it's possible to place the rest of the queens you need using this
        # position, then the recursive call will yield a value.
        # If it's not possible to place the rest of the queens you need
        # using this position, then the recursive call will *not* yield
        # a value, so the wrong positions will get filtered out automatically.
        yield from nqueens(size, new_board)


def print_board(board):
    """
    This is a convenience function, to pretty-print the queens on a board.
    Queens will be represented by the character "Q".
    Spaces without queens will be represented by the character "-".

    Args:
        board (frozenset): A set of (x, y) tuples where queens have
            been placed on the board.
    """
    size = len(board)
    for row in range(size):
        cells = (
            "Q" if (row, col) in board else "-"
            for col in range(size)
        )
        print("".join(cells))


# If you run this file as a script,
# it will print out all the solutions to the 8 Queens problem,
# followed by the total number of solutions.
if __name__ == "__main__":
    size = 8
    solution_count = 0
    for solution in nqueens(size):
        solution_count += 1
        print_board(solution)
        print("*" * size)
    print("{count} solutions".format(count=solution_count))
