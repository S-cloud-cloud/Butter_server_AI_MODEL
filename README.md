# Serve_butter_AI_MODEL
This is an AI project which is developed based on AI Search algorithms by using python as a language

Problem specification : here the problem is serving butter to customers on a table, for this purpose an AI agent named robot has 
been developed that works based on AI search algorithms to serve customers ASAP.

2.Findings: My working shows in the end the path cost and steps that agent had to take to serve/find solution to the same above mentioned problem for three different search
algorithms,namely: A* Algorithm , Bidirectional BFS , Iterative Deepening Search.

● A* Algorithm:
A* Search algorithm is one of the best and popular
technique used in path-finding and graph traversals.

● Bidirectional BFS
Bidirectional search is a graph search algorithm which
find smallest path from source to goal vertex. 

* Iterative Deepening Search:
IDDFS combines depth-first search’s
space-efficiency and breadth-first search’s fast
search (for nodes closer to root).
How does IDDFS work?
IDDFS calls DFS for different depths starting from
an initial value. In every call, DFS is restricted from
going beyond given depth. So basically we do DFS

RESULT :

1.A* Algorithm :
PATH: RDRURDDRDL
Total moves: 10
Total cost: 14

2.Bidirectional BFS:
PATH:Found 2 possible ways.
Found a way with 10 moves.
DRRURDDRDL
Total cost: 15

3.Iterative Deepening Search:
PATH: Starting with depth 1
Starting with depth 2
Starting with depth 3
Starting with depth 4
Starting with depth 5
Starting with depth 6
Starting with depth 7
Starting with depth 8
Starting with depth 9
Starting with depth 10
RDRURDDRDL
Total moves: 10
Total cost: 14


in a BFS fashion.
