#!/usr/bin/python3
"""Defines a rectangle"""
import sys

def solve(board, col):
    if col >= len(board):
        print_board(board)
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1)
            board[i][col] = 0

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for _ in range(N)] for _ in range(N)]
solve(board, 0)
