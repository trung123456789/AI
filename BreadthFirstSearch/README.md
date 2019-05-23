```
*	Breadth-first search is the most common search strategy for traversing a tree or graph. This algorithm searches breadthwise in a tree or graph, so it is called breadth-first search.
*	BFS algorithm starts searching from the root node of the tree and expands all successor node at the current level before moving to nodes of next level.
*	The breadth-first search algorithm is an example of a general-graph search algorithm.
*	Breadth-first search implemented using FIFO queue data structure.
```
#	Advantages:
```
BFS will provide a solution if any solution exists.
If there are more than one solutions for a given problem, then BFS will provide the minimal solution which requires the least number of steps.
```
#	Disadvantages:
```
It requires lots of memory since each level of the tree must be saved into memory to expand the next level.
BFS needs lots of time if the solution is far away from the root node.
```
#	Thuật giải
```	
	Trước khi bắt đầu, tôi sẽ nêu ra một số quy ước để dễ dàng trong trình bày:

	Open: là tập hợp các đỉnh chờ được xét ở bước tiếp theo theo hàng đợi (hàng đợi: dãy các phần tử mà khi thêm phần tử vào sẽ thêm vào cuối dãy, còn khi lấy phần tử ra sẽ lấy ở phần tử đứng đầu dãy).
	Close: là tập hợp các đỉnh đã xét, đã duyệt qua.
	s: là đỉnh xuất phát, đỉnh gốc ban đầu trong quá trình tìm kiếm.
	g: đỉnh đích cần tìm.
	p: đỉnh đang xét, đang duyệt.
```

#	Trình bày thuật giải:
```	
	Bước 1: Tập Open chứa đỉnh gốc s chờ được xét.
	Bước 2: Kiểm tra tập Open có rỗng không.
	Nếu tập Open không rỗng, lấy một đỉnh ra khỏi tập Open làm đỉnh đang xét p. Nếu p là đỉnh g cần tìm, kết thúc tìm kiếm.
	Nếu tập Open rỗng, tiến đến bước 4.
	Bước 3: Đưa đỉnh p vào tập Close, sau đó xác định các đỉnh kề với đỉnh p vừa xét. Nếu các đỉnh kề không thuộc tập Close, đưa chúng vào cuối tập Open. Quay lại bước 2.
	Bước 4: Kết luận không tìm ra đỉnh đích cần tìm.
```
#	Hình ảnh minh họa
![alt](https://static.javatpoint.com/tutorial/ai/images/breadth-first-search.png)
#	Độ phức tạp
```
	Độ phức tạp thời gian của thuật toán BFS có thể thu được bằng số lượng nút đi qua trong BFS cho đến khi nút Node nông nhất. Trong đó d = độ sâu nông nhất và b là một nút ở mọi trạng thái.
	T (b) = 1+b2+b3+.......+ bd= O (bd)
```
#	Khả năng hoàn thành(Có kết quả)
```
	BFS có thể hoàn thành, có nghĩa là nếu nút mục tiêu nông nhất ở độ sâu hữu hạn, thì BFS sẽ tìm ra giải pháp.
```