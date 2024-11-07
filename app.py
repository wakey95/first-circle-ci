def add(a, b):
    return a + b

def main(a, b, c):
    try:
        if c == 0:
            print("Lỗi: Không thể chia cho 0!")
            return

        result1 = a + b - c
        result2 = a * b / c

        print(f"Kết quả của a + b - c là: {result1}")
        print(f"Kết quả của a * b / c là: {result2}")

    except ValueError:
        print("Lỗi: Vui lòng nhập giá trị hợp lệ cho các số!")

if __name__ == "__main__":
    main(5, 3, 2)  # Cung cấp giá trị mặc định cho a, b, c
