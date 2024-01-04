#!/usr/bin/python3
import sys

def print_board(board):
   for i in range(len(board)):
       for j in range(len(board)):
           print('Q ' if board[i][j] else '. ', end='')
       print()

def is_safe(board, row, col):
   for i in range(col):
       if board[row][i]:
           return False

   for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
       if board[i][j]:
           return False

   for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
       if board[i][j]:
           return False

   return True

def solve_n_queens(board, col):
   if col >= len(board):
       return True

   for i in range(len(board)):
       if is_safe(board, i, col):
           board[i][col] = 1

           if solve_n_queens(board, col + 1):
               return True

           board[i][col] = 0

   return False

def nqueens(N):
   if N < 4:
       print("N must be at least 4\n")
       sys.exit(1)

   board = [[0]*N for _ in range(N)]

   if not solve_n_queens(board, 0):
       print("Solution does not exist")
       return

   print_board(board)

if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Usage: nqueens N\n")
       sys.exit(1)

   N = int(sys.argv[1])

   if not isinstance(N, int):
       print("N must be a number\n")
       sys.exit(1)

   nqueens(N)
