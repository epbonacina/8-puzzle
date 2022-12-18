A simple Python program that can solve the 8-puzzle game using 3 different algorithms.

## Requirements

pandas


## How to use

1. Run `python main.py` in the project directory;
2. The initial state will be requested. It should be similar to `2_3541687`, which represents the following board:

2 |  | 3 
--- | --- | ---
5 | 4 | 1
6 | 8 | 7

3. After that, the program will solve the game using BFS (Breadth First Search), DFS (Depth First Search) and two variations of A* and will display on screen the number of explored nodes, the cost, and the elapsed time in seconds for each solution.


## Example

Expected output for the initial state `2_3541687`

 Algorithm | Explored nodes | Cost | Elapsed time (in seconds)
--- | --- | --- | ---
BFS | 101425 | 23 | 0.642556
DFS | 71399 | 68539 | 0.296347
A* HAMMING | 14093 | 23 | 0.125270
A* MANHATTAN | 2013 | 23 | 0.018638


## Developers

- Enzo Pedro Bonacina [Turma B] 00313316;
- Thales Junqueira Albergaria Moraes Perez [Turma B] 00303035;
- Hiram [Turma B] xxxxxxxx;
