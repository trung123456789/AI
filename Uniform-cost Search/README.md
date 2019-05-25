```
    Uniform-cost search is a searching algorithm used for traversing a weighted tree or graph. This algorithm comes into play when a different cost is available for each edge. The primary goal of the uniform-cost search is to find a path to the goal node which has the lowest cumulative cost. Uniform-cost search expands nodes according to their path costs form the root node. It can be used to solve any graph/tree where the optimal cost is in demand. A uniform-cost search algorithm is implemented by the priority queue. It gives maximum priority to the lowest cumulative cost. Uniform cost search is equivalent to BFS algorithm if the path cost of all edges is the same.
```
### Advantage:
```
    Uniform cost search is optimal because at every state the path with the least cost is chosen.
```
### Disadvantage:
```
    It does not care about the number of steps involve in searching and only concerned about path cost. Due to which this algorithm may be stuck in an infinite loop.
```
### Ý tưởng thuật toán
```
Từ đỉnh (nút) gốc ban đầu, thuật toán duyệt đi xa nhất theo từng nhánh, khi nhánh đã duyệt hết, lùi về từng đỉnh để tìm và duyệt những nhánh tiếp theo. Quá trình duyệt chỉ dừng lại khi tìm thấy đỉnh cần tìm hoặc tất cả đỉnh đều đã được duyệt qua.Ý tưởng thuật toán.
```
###	Thuật giải
```	
    fringe : là một cấu trúc kiểu hàng đợi (FIFO) lưu giữ các nút sẽ được duyệt
    closed : cấu trúc hàng đợi queue  lưu giữ các nút đã được duyệt .
    graph(N, A) : cây biểu diễn không gian trạng thái bài toán.
    s : trạng thái đầu của bài toán
    g : tập hợp các trạng thái đích của bài toán.
    NB(n) : tập hợp các trạng thái con của cua nút đang xét n.

```

###	Trình bày thuật giải:
```	
    begin
    procedure UniformCostSearch(Graph, root, goal)
    node:= root, cost = 0
    frontier:= priority queue containing node only
    explored:= empty set
    do
        if frontier is empty
        return failure
        node:= frontier.pop()
        if node is goal
        return solution
        explored.add(node)
        for each of node's neighbors n
        if n is not in explored
            if n is not in frontier
            frontier.add(n)
            else if n is in frontier with higher cost
            replace existing node with n
```
###	Hình ảnh minh họa
![alt](https://static.javatpoint.com/tutorial/ai/images/uniform-cost-search-algorithm.png)
### Completeness: 
`   Uniform-cost search is complete, such as if there is a solution, UCS will find it.`

### Time Complexity: 
```
    Let C* is Cost of the optimal solution, and ε is each step to get closer to the goal node. Then the number of steps is = C*/ε+1. Here we have taken +1, as we start from state 0 and end to C*/ε.

    Hence, the worst-case time complexity of Uniform-cost search isO(b1 + [C*/ε])/.
```
### Space Complexity: 
`   The same logic is for space complexity so, the worst-case space complexity of Uniform-cost search is O(b1 + [C*/ε]).`
### Optimal: 
`   Uniform-cost search is always optimal as it only selects a path with the lowest path cost.`