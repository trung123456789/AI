```
    Greedy best-first search algorithm always selects the path which appears best at that moment. It is the combination of depth-first search and breadth-first search algorithms. It uses the heuristic function and search. Best-first search allows us to take the advantages of both algorithms. With the help of best-first search, at each step, we can choose the most promising node. In the best first search algorithm, we expand the node which is closest to the goal node and the closest cost is estimated by heuristic function, i.e.

    f(n)= g(n).   
    Were, h(n)= estimated cost from node n to the goal.

    The greedy best first algorithm is implemented by the priority queue.
```
### Advantage:
```
    Best first search can switch between BFS and DFS by gaining the advantages of both the algorithms.
    This algorithm is more efficient than BFS and DFS algorithms.
```
### Disadvantage:
```
    It can behave as an unguided depth-first search in the worst case scenario.
    It can get stuck in a loop as DFS.
    This algorithm is not optimal.
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

### Các bước thực hiện
```
    Step 1: Place the starting node into the OPEN list.
    Step 2: If the OPEN list is empty, Stop and return failure.
    Step 3: Remove the node n, from the OPEN list which has the lowest value of h(n), and places it in the CLOSED list.
    Step 4: Expand the node n, and generate the successors of node n.
    Step 5: Check each successor of node n, and find whether any node is a goal node or not. If any successor node is goal node, then return success and terminate the search, else proceed to Step 6.
    Step 6: For each successor node, algorithm checks for evaluation function f(n), and then check if the node has been in either OPEN or CLOSED list. If the node has not been in both list, then add it to the OPEN list.
    Step 7: Return to Step 2.
```
###	Trình bày thuật giải:
```	
    procedure Best_First_Search;
    begin
    Khởi tạo danh sách L chỉ chứa trạng thái ban đầu;
    loop do
        if L rỗng then
        {thông báo thất bại; stop};
        Loại trạng thái u ở đầu danh sách L;
        if u là trạng thái kết thúc then
        {thông báo thành công; stop};
        for mỗi trạng thái v kề u do
        Xen v vào danh sách L sao cho L được sắp theo thứ tự tăng dần
        của hàm đánh giá;
    end;
```
###	Hình ảnh minh họa
`   Example`
![alt](https://images.viblo.asia/85a2babd-2ce1-4041-9133-5a7ad9409d0f.jpg)
`   Description Example`
![alt](https://images.viblo.asia/5bb26e11-428a-40e2-baac-6fe19ea7a0bd.jpg)
### Completeness: 
`   Greedy best-first search is also incomplete, even if the given state space is finite.`

### Time Complexity: 
`   The worst case time complexity of Greedy best first search is O(bm)`
### Space Complexity: 
`   The worst case space complexity of Greedy best first search is O(bm). Where, m is the maximum depth of the search space.`
### Optimal: 
`   Greedy best first search algorithm is not optimal.`