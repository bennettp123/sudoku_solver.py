# A simple sudoku solver

Usage:

```
./sudoku_solver.py <sudoku_puzzle>
```

where `<sudoku_puzzle>` is a file that contains a single puzzle.

Puzzles must contain exactly 81 digits. Use dots (".") to represent blank
spaces. All other characters are ignored.

## Known issues

* Only finds shallow solutions that can be solved by examining items within
  individual rows, columns or squares.

