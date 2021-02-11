# POLYOMINO - a Python package for polyomino tiling problems

This is a package for manipulating polyominos and in particular, solving tiling problems. It uses the 'exact-cover' python package as the main engine for solving cover problems.

To solve a tiling problem, you need to create a 'board', the set of squares to be covered, and a 'tileset', the collection of polyominos which can be used. There are examples of the syntax to do this in examples/fluid.md The example file examples/gardner.md uses the package to solve a number of problems from the chapter on polyominos from Martin Gardner's book 'Mathematical Puzzles and Diversions'.

## Design
Both polyominos and boards are represented internally as lists of integer tuples (x, y). There are constants defined for all polyominos up to pentominos in polyomino.constant
