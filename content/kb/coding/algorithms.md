+++
title = "Algorithms"
description = "Notes about common algorithms and algorithm design"

[extra]
render_math = true
+++

## Breadth-First Search (BFS)

**Purpose:**  
Explores all vertices of a graph systematically, layer by layer, starting from a given source vertex; computes shortest path distances in unweighted graphs.

**Time Complexity:**  
$O(V + E)$, where $V$ is the number of vertices and $E$ is the number of edges.

**Description:**  
Breadth-First Search traverses a graph by visiting all vertices reachable from a starting vertex, exploring neighbors before moving to vertices at the next level. It uses a queue to keep track of the frontier of vertices to visit. Each vertex is marked as visited when first encountered, and its distance from the source is updated. BFS guarantees that when a vertex is dequeued, the shortest path from the source to that vertex has been found (in terms of number of edges). This makes BFS a foundation for many graph algorithms, including shortest path in unweighted graphs, connectivity checks, and bipartiteness testing.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Graph $G = (V, E)$, source vertex $s$
\State \textbf{Output:} Distance $dist[v]$ from $s$ to each vertex $v$, and predecessors $prev[v]$

\For{each vertex $v \in V$}
    \State $dist[v] \gets \infty$
    \State $prev[v] \gets \text{undefined}$
\EndFor
\State $dist[s] \gets 0$
\State $Q \gets$ empty queue
\State enqueue $s$ into $Q$

\While{$Q$ is not empty}
    \State $u \gets$ dequeue from $Q$
    \For{each neighbor $v$ of $u$}
        \If{$dist[v] = \infty$}
            \State $dist[v] \gets dist[u] + 1$
            \State $prev[v] \gets u$
            \State enqueue $v$ into $Q$
        \EndIf
    \EndFor
\EndWhile

\State \Return $dist$, $prev$
\end{algorithmic}
```

## Depth-First Search (DFS)

**Purpose:**  
Systematically explores all vertices and edges of a graph by going as deep as possible along each branch before backtracking.

**Time Complexity:**  
$O(V + E)$, where $V$ is the number of vertices and $E$ is the number of edges.

**Description:**  
Depth-First Search traverses a graph starting from a source vertex, visiting vertices by following one path as far as possible before backtracking. This can be implemented recursively or using a stack. Each vertex is marked as visited when first encountered. DFS is useful for many applications, including detecting cycles, computing connected components, topological sorting, and solving pathfinding problems. The traversal naturally forms a DFS tree or forest that can be analyzed to extract additional information about the graph structure.

**Pseudocode (recursive version):**

```latex
\begin{algorithmic}
\State \textbf{Input:} Graph $G = (V, E)$, source vertex $s$
\State \textbf{Output:} Set of visited vertices and DFS tree

\For{each vertex $v \in V$}
    \State $visited[v] \gets \text{false}$
\EndFor

\Function{DFS}{$v$}
    \State $visited[v] \gets \text{true}$
    \For{each neighbor $u$ of $v$}
        \If{not $visited[u]$}
            \State \Call{DFS}{$u$}
        \EndIf
    \EndFor
\EndFunction

\State \Call{DFS}{$s$}
\State \Return $visited$
\end{algorithmic}
```

## Dijkstra's Algorithm

**Purpose:**  
Finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

**Time Complexity:**  
$O((V + E) \log V)$ using a min-priority queue (e.g. with a binary heap).

**Description:**  
Dijkstra’s algorithm incrementally builds the set of vertices with known minimum distances from the source. It begins with the source vertex, assigning it a distance of zero and all others infinity. It repeatedly selects the vertex with the smallest known distance, then relaxes all edges leading from that vertex—updating the distances to neighboring vertices if a shorter path is found through the current one. The process continues until all vertices have been processed or the smallest distance in the queue is infinity, meaning unreachable vertices remain.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Graph $G = (V, E)$ with non-negative edge weights $w(u, v)$, source vertex $s$
\State \textbf{Output:} Shortest path distances $dist[v]$ from $s$ to all $v \in V$

\For{each vertex $v \in V$}
    \State $dist[v] \gets \infty$
    \State $prev[v] \gets \text{undefined}$
\EndFor
\State $dist[s] \gets 0$
\State $Q \gets$ all vertices in $V$ (min-priority queue keyed by $dist[v]$)

\While{$Q$ is not empty}
    \State $u \gets$ vertex in $Q$ with minimum $dist[u]$
    \State remove $u$ from $Q$
    \For{each neighbor $v$ of $u$}
        \State $alt \gets dist[u] + w(u, v)$
        \If{$alt < dist[v]$}
            \State $dist[v] \gets alt$
            \State $prev[v] \gets u$
            \State decrease-key($Q$, $v$, $alt$)
        \EndIf
    \EndFor
\EndWhile

\State \Return $dist$, $prev$
\end{algorithmic}
```

## Gale–Shapley Algorithm

**Purpose:**  
Finds a stable matching between two equally sized sets (e.g., men and women) given each participant’s ranked preferences.

**Time Complexity:**  
$O(n^2)$, where $n$ is the number of participants in each group.

**Description:**  
The Gale–Shapley algorithm (also called the *Stable Marriage Algorithm*) solves the stable matching problem by iteratively pairing members of two sets based on mutual preferences. In the classic version, each unengaged man proposes to the most-preferred woman on his list who has not yet rejected him. Each woman then considers all her proposals and tentatively accepts the one she prefers most, rejecting the rest. Rejected men propose again in the next round. This continues until everyone is matched. The result is guaranteed to be stable—no unmatched pair would both prefer each other over their current partners—and optimal for the proposing group.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Sets $M$ (men) and $W$ (women), with preference lists for each
\State \textbf{Output:} Stable matching between $M$ and $W$

\For{each man $m \in M$}
    \State $m$ is free
\EndFor
\For{each woman $w \in W$}
    \State $w$ is free
\EndFor

\While{there exists a free man $m$ who has not proposed to every woman}
    \State $w \gets$ highest-ranked woman on $m$'s list to whom $m$ has not yet proposed
    \State $m$ proposes to $w$
    \If{$w$ is free}
        \State $(m, w)$ become engaged
    \ElsIf{$w$ prefers $m$ to her current fiancé $m'$}
        \State $w$ breaks engagement with $m'$
        \State $(m, w)$ become engaged
        \State $m'$ becomes free
    \Else
        \State $w$ rejects $m$
    \EndIf
\EndWhile

\State \Return \text{set of engagements as the stable matching}
\end{algorithmic}
```

## Topological Sort

**Purpose:**  
Determines a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before v in the ordering.

**Time Complexity:**  
$O(V + E)$

**Description:**  
Topological sort produces an ordering of vertices consistent with the dependencies defined by a DAG. It can be performed using depth-first search (DFS) or by repeatedly removing vertices with no incoming edges (Kahn’s algorithm). In the DFS-based version, the algorithm explores all unvisited vertices, recursively visiting each neighbor before marking the current vertex as finished and pushing it onto a stack. Once all vertices are processed, the stack’s reverse order gives a valid topological ordering. This ordering is especially useful for scheduling tasks, resolving symbol dependencies, and performing build order computations.

**Pseudocode (DFS-based):**

```latex
\begin{algorithmic}
\State \textbf{Input:} Directed acyclic graph $G = (V, E)$
\State \textbf{Output:} List $L$ of vertices in topological order

\For{each vertex $v \in V$}
    \State $visited[v] \gets \text{false}$
\EndFor
\State $L \gets$ empty list

\Function{DFS}{$v$}
    \State $visited[v] \gets \text{true}$
    \For{each neighbor $u$ of $v$}
        \If{not $visited[u]$}
            \State \Call{DFS}{$u$}
        \EndIf
    \EndFor
    \State prepend $v$ to $L$
\EndFunction

\For{each vertex $v \in V$}
    \If{not $visited[v]$}
        \State \Call{DFS}{$v$}
    \EndIf
\EndFor

\State \Return $L$
\end{algorithmic}
```

## Prim's Algorithm

**Purpose:**  
Finds a minimum spanning tree (MST) for a connected, weighted, undirected graph—connecting all vertices with the minimum possible total edge weight.

**Time Complexity:**  
$O((V + E) \log V)$ when implemented with a min-priority queue (e.g., binary heap).

**Description:**  
Prim’s algorithm grows a minimum spanning tree by starting from an arbitrary vertex and repeatedly adding the smallest edge that connects a vertex in the tree to a vertex outside it. It maintains a set of vertices already included in the MST and a priority queue of candidate edges, prioritized by weight. Each time a vertex is added, the algorithm updates the queue with its outgoing edges that connect to unvisited vertices. The process continues until all vertices are included, ensuring the resulting tree has the minimal total weight.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Connected, weighted, undirected graph $G = (V, E)$
\State \textbf{Output:} Set of edges forming the minimum spanning tree (MST)

\For{each vertex $v \in V$}
    \State $key[v] \gets \infty$
    \State $parent[v] \gets \text{undefined}$
\EndFor

\State Choose an arbitrary start vertex $r$
\State $key[r] \gets 0$
\State $Q \gets$ all vertices in $V$ (min-priority queue keyed by $key[v]$)

\While{$Q$ is not empty}
    \State $u \gets$ vertex in $Q$ with minimum $key[u]$
    \State remove $u$ from $Q$
    \For{each vertex $v$ adjacent to $u$ with edge weight $w(u, v)$}
        \If{$v \in Q$ and $w(u, v) < key[v]$}
            \State $parent[v] \gets u$
            \State $key[v] \gets w(u, v)$
            \State decrease-key($Q$, $v$, $w(u, v)$)
        \EndIf
    \EndFor
\EndWhile

\State \Return $\{(parent[v], v) \mid v \in V \setminus \{r\}\}$
\end{algorithmic}
```

## Kruskal's Algorithm

**Purpose:**  
Finds a minimum spanning tree (MST) for a connected, weighted, undirected graph by adding edges in increasing order of weight while avoiding cycles.

**Time Complexity:**  
$O(E \log E)$ due to sorting the edges; near-linear with union-find optimizations.

**Description:**  
Kruskal’s algorithm builds the MST by considering all edges in order of increasing weight and adding each edge to the growing forest if it does not form a cycle. To efficiently detect cycles, the algorithm uses a disjoint-set (union-find) data structure. Initially, each vertex is its own set. For each edge (u, v), if u and v belong to different sets, the edge is added to the MST, and the sets of u and v are merged. This process continues until the MST contains exactly V-1 edges, guaranteeing a minimum total weight while connecting all vertices.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Connected, weighted, undirected graph $G = (V, E)$
\State \textbf{Output:} Set of edges forming the minimum spanning tree (MST)

\State Sort all edges $E$ in non-decreasing order of weight
\State Initialize a disjoint-set data structure $DS$ with each vertex $v \in V$ in its own set
\State $MST \gets \emptyset$

\For{each edge $(u, v)$ in sorted $E$}
    \If{$DS.\text{Find}(u) \neq DS.\text{Find}(v)$}
        \State $MST \gets MST \cup \{(u, v)\}$
        \State $DS.\text{Union}(u, v)$
    \EndIf
\EndFor

\State \Return $MST$
\end{algorithmic}
```

## Interval Scheduling

**Purpose:**  
Selects the maximum number of non-overlapping intervals (tasks) from a set of intervals with start and end times.

**Time Complexity:**  
$O(n \log n)$, dominated by the sorting step, where $n$ is the number of intervals.

**Description:**  
Interval Scheduling uses a greedy strategy to maximize the number of compatible tasks. The algorithm first sorts all intervals by their finishing times. It then iteratively selects the earliest-finishing interval that does not overlap with previously selected intervals, adding it to the schedule. This approach guarantees an optimal solution because, at each step, choosing the interval with the earliest finish leaves the maximum room for subsequent intervals, ensuring the schedule can include as many tasks as possible.

**Pseudocode:**

```latex
\begin{algorithmic}
\State \textbf{Input:} Set of intervals $I = \{1, 2, \dots, n\}$ with start times $s_i$ and finish times $f_i$
\State \textbf{Output:} Maximum-size subset of non-overlapping intervals

\State Sort intervals by increasing $f_i$
\State $A \gets \emptyset$ \Comment{selected intervals}
\State $t \gets 0$ \Comment{end time of last added interval}

\For{each interval $i$ in sorted order}
    \If{$s_i \ge t$}
        \State $A \gets A \cup \{i\}$
        \State $t \gets f_i$
    \EndIf
\EndFor

\State \Return $A$
\end{algorithmic}
```
