# A simple sudoku solver

Usage:

```
./sudoku_solver.py <sudoku-puzzle>
```

Puzzles must contain exactly 81 digits. Use dots (".") to represent blank
spaces. All other characters are ignored.

## Known issues

* Only finds "shallow" solutions, that can be solved within an single row,
  column or square.

