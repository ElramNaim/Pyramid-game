# Pyramid-game
The pyramid game is a game that runs alone.
In the center of the game is a matrix inside which is a pyramid with three colors - blue, yellow and pink.
At the start of the game, each cell in the pyramid is randomly initialized to one of the colors.
In each round of the game, in each cell that does not comply with the following rules, a new cell is randomly chosen in its place.

The rules:
1. The blue cell cannot be within the boundaries of the pyramid. That is, in each of the three outer ribs - not only at the vertices (if there is a blue cell, grill a new cell in its place).
2. A pink cell cannot appear to the right/left/above/below a blue cell. If you encounter such a case, grill a new cell instead of the pink cell.
3. If there are more than 4 yellow cells in a row, grill the whole row again.

<hope you enjoy!>
*use only pygame and randome Libraries.*
