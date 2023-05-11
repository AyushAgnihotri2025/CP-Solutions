import 'dart:core';

class Solution {
  void solveSudoku(List<List<String>> board) {
    this.backtrack(board);
  }

  bool backtrack(List<List<String>> board) {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (board[i][j] == '.') {
          for (int c = 1; c <= 9; c++) {
            if (this.isPointValid(board, i, j, c)) {
              board[i][j] = c.toString();
              if (this.backtrack(board)) {
                return true;
              } else {
                board[i][j] = '.';
              }
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  bool isPointValid(List<List<String>> board, int x, int y, int c) {
    for (int i = 0; i < 9; i++) {
      if (board[i][y] == c.toString()) {
        return false;
      }
      if (board[x][i] == c.toString()) {
        return false;
      }
      if (board[3 * (x ~/ 3) + i ~/ 3][3 * (y ~/ 3) + i % 3] == c.toString()) {
        return false;
      }
    }
    return true;
  }
}