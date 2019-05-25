```
    A depth-limited search algorithm is similar to depth-first search with a predetermined limit. Depth-limited search can solve the drawback of the infinite path in the Depth-first search. In this algorithm, the node at the depth limit will treat as it has no successor nodes further.

    Depth-limited search can be terminated with two Conditions of failure:

    Standard failure value: It indicates that problem does not have any solution.
    Cutoff failure value: It defines no solution for the problem within a given depth limit.
```
### Advantage:
```
Depth-limited search is Memory efficient.
```
### Disadvantage:
```
Depth-limited search also has a disadvantage of incompleteness.
It may not be optimal if the problem has more than one solution.
```
### Ý tưởng thuật toán
```
Từ đỉnh (nút) gốc ban đầu, thuật toán duyệt đi xa nhất theo từng nhánh, khi nhánh đã duyệt hết, lùi về từng đỉnh để tìm và duyệt những nhánh tiếp theo. Quá trình duyệt chỉ dừng lại khi tìm thấy đỉnh cần tìm hoặc tất cả đỉnh đều đã được duyệt qua.Ý tưởng thuật toán.
```
###	Thuật giải
```	
*   Open: là tập hợp các đỉnh chờ được xét ở bước tiếp theo theo ngăn xếp (ngăn xếp: dãy các phần tử mà khi thêm phần tử vào sẽ thêm vào đầu dãy, còn khi lấy phần tử ra sẽ lấy ở phần tử đứng đầu dãy).
*   Close: là tập hợp các đỉnh đã xét, đã duyệt qua.
*   s: là đỉnh xuất phát, đỉnh gốc ban đầu trong quá trình tìm kiếm.
*   g: đỉnh đích cần tìm.
*   p: đỉnh đang xét, đang duyệt.

```

###	Trình bày thuật giải:
```	
    Bước 1: Tập Open chứa đỉnh gốc s chờ được xét.
    Bước 2: Kiểm tra tập Open có rỗng không.
    Nếu tập Open không rỗng, lấy một đỉnh ra khỏi tập Open làm đỉnh đang xét p. Nếu p là đỉnh g cần tìm, kết thúc tìm kiếm.
    Nếu tập Open rỗng, tiến đến bước 4.
    Bước 3: Đưa đỉnh p vào tập Close, sau đó xác định các đỉnh kề với đỉnh p vừa xét. Nếu các đỉnh kề không thuộc tập Close, đưa chúng vào đầu tập Open. Quay lại bước 2.
    Bước 4: Kết luận không tìm ra đỉnh đích cần tìm.
```
###	Hình ảnh minh họa
![alt](https://static.javatpoint.com/tutorial/ai/images/depth-limited-search-algorithm.png)
### Completeness: 
`DLS search algorithm is complete if the solution is above the depth-limit.`

### Time Complexity: 
`Time complexity of DLS algorithm is O(bℓ).`
### Space Complexity: 
`Space complexity of DLS algorithm is O(b×ℓ).`
### Optimal: 
`Depth-limited search can be viewed as a special case of DFS, and it is also not optimal even if ℓ>d.`