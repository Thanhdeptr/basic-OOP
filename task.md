# Bài toán: Mô phỏng Zombie Apocalypse (turn-based)

Tài liệu mô tả **luật chơi**, **input**, và **luồng lượt** khớp với code trong `real_test/`.

---

## Bản đồ và kết thúc

- Lưới **20×20**, tọa độ nguyên **x**, **y** với **0 ≤ x, y ≤ 19** (trục hiển thị: hàng = `y`, cột = `x`).
- `**m`**: số lượt tối đa mô phỏng (mỗi lượt = một vòng hành động bên dưới).
- **Điều kiện dừng** (cả `zombie_apocalypse_oop.py` và `visualize_game.py`): kết thúc khi `turn >= m` **hoặc** không còn người (`human_array` rỗng) **hoặc** không còn zombie (`zombie_array` rỗng) — ví dụ phe người bị nhiễm hết, hoặc lính tiêu diệt hết zombie. Sau khi xử lý nhiễm hoãn đầu lượt, nếu một trong hai phe đã không còn ai thì **dừng ngay**, không chạy các pha di chuyển / tấn công / săn của lượt đó.

---

## Đề bài

Mô phỏng **thành phố bị zombie** trên **mặt phẳng 2D**. Mỗi đối tượng có **ID**, **type** (1–3), tọa độ **x**, **y**.

- **Quân lính (type = 1)** — thêm **cấp**: tương đương **số zombie tiêu diệt tối đa mỗi lượt** và **khoảng cách tấn công**; tự **tấn công zombie gần nhất**; **tốc độ di chuyển thấp** hơn các loại khác; bị zombie **tiếp cận** → biến thành zombie **ở lượt kế**, zombie mới có **tốc độ di chuyển = 1**.
- **Dân thường (type = 2)** — thêm **tốc độ `s`** và **tầm nhìn `v`**: nếu có zombie trong tầm nhìn thì **chạy trốn zombie gần nhất**; **không** có zombie trong `v` thì **đứng yên**; khi bị biến đổi, zombie mới **giữ tốc độ di chuyển như lúc còn là dân**.
- **Zombie (type = 3)** — thêm **tốc độ `s`**: tự **tiến về dân / lính gần nhất**; **không** còn người thì **đứng yên**; **tiếp cận** quân lính / dân → biến họ thành zombie **trong lượt kế**. **Đầu mỗi lượt** zombie **xác định mục tiêu**, ưu tiên **quân lính cấp cao hơn** và **dân có tốc độ di chuyển thấp hơn** (theo quy tắc ưu tiên trong đề).
- **Quy tắc di chuyển:** quân lính **luôn đứng yên**; dân và zombie có thể **đi thẳng hoặc chéo**; zombie ưu tiên hướng **rút ngắn khoảng cách** nhất; dân di chuyển **ngược hướng** so với hướng tới zombie gần nhất.
- **Thứ tự trong một lượt (theo đề):** **dân di chuyển** → **zombie di chuyển** → **quân lính tấn công**.
- **Yêu cầu kỹ thuật:** áp dụng **kế thừa** và **đa hình** để mô phỏng **lây lan dịch bệnh**.

**Ghi chú đối chiếu code:** Trong `real_test/`, thứ tự pha đang là nhiễm hoãn (đầu lượt) → **dân** → **lính tấn công** → **zombie**.

---

## Cá thể và ID

- `**n`**: số cá thể cần nhập.
- **ID tự tăng** theo thứ tự dòng: `1, 2, 3, …` — **không nhập ID** trong file/input tay.


| Type | Tên     | Dòng input  | Ý nghĩa tham số                                                              |
| ---- | ------- | ----------- | ---------------------------------------------------------------------------- |
| 1    | Soldier | `1 x y lvl` | `lvl`: cấp; **RNG = AD = lvl** . Tốc độ cố định **1** (không thể di chuyển). |
| 2    | Citizen | `2 x y s v` | `s`: tốc độ ; `v`: tầm nhìn                                                  |
| 3    | Zombie  | `3 x y s`   | `s`: tốc độ                                                                  |


---

## Input: stdin hoặc file

- **Dòng 1:** `n m`
- **Tiếp theo `n` dòng**, mỗi dòng một cá thể đúng format type ở bảng trên.
- **Chạy với file:** tham số dòng lệnh là đường dẫn file (ví dụ `python zombie_apocalypse_oop.py sample_input.txt` trong thư mục `real_test/`).
- Không tham số → nhập interative từ bàn phím.

---

## Input mẫu (`real_test/sample_input.txt`)

```text
10 20
1 2 3 1
2 3 4 1 2
3 6 5 1
1 4 3 1 
2 5 6 1 2
3 13 13 1
3 12 13 1 
3 13 10 1
3 12 11 1
3 11 10 1
```

- **10 20**: 10 cá thể, tối đa 20 lượt.
- Các dòng sau: hỗn hợp Soldier / Citizen / Zombie theo đúng số cột quy định.

---

## Chạy nhanh

```bash
cd real_test
python zombie_apocalypse_oop.py sample_input.txt    # text log
python visualize_game.py sample_input.txt           # map màu + delay ~1.5s/lượt
```

---

## File liên quan


| File                       | Vai trò                                 |
| -------------------------- | --------------------------------------- |
| `zombie_apocalypse_oop.py` | Engine: class, `get_input_data`, `main` |
| `visualize_game.py`        | Hiển thị terminal (màu theo type)       |
| `io_utils.py`              | Đọc stdin / file qua `argv`             |
| `movement_utils.py`        | Ô bận, bước trượt tường                 |
| `README.md`                | Hướng dẫn tổng quan + góc nhìn OOP      |


