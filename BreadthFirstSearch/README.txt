Thuật giải
	Trước khi bắt đầu, tôi sẽ nêu ra một số quy ước để dễ dàng trong trình bày:

	Open: là tập hợp các đỉnh chờ được xét ở bước tiếp theo theo hàng đợi (hàng đợi: dãy các phần tử mà khi thêm phần tử vào sẽ thêm vào cuối dãy, còn khi lấy phần tử ra sẽ lấy ở phần tử đứng đầu dãy).
	Close: là tập hợp các đỉnh đã xét, đã duyệt qua.
	s: là đỉnh xuất phát, đỉnh gốc ban đầu trong quá trình tìm kiếm.
	g: đỉnh đích cần tìm.
	p: đỉnh đang xét, đang duyệt.

Trình bày thuật giải:
	Bước 1: Tập Open chứa đỉnh gốc s chờ được xét.
	Bước 2: Kiểm tra tập Open có rỗng không.
	Nếu tập Open không rỗng, lấy một đỉnh ra khỏi tập Open làm đỉnh đang xét p. Nếu p là đỉnh g cần tìm, kết thúc tìm kiếm.
	Nếu tập Open rỗng, tiến đến bước 4.
	Bước 3: Đưa đỉnh p vào tập Close, sau đó xác định các đỉnh kề với đỉnh p vừa xét. Nếu các đỉnh kề không thuộc tập Close, đưa chúng vào cuối tập Open. Quay lại bước 2.
	Bước 4: Kết luận không tìm ra đỉnh đích cần tìm.