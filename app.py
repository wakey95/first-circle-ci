def main():
    # Nhập ba số từ người dùng
    try:
        a = float(input("Nhập giá trị cho a: "))
        b = float(input("Nhập giá trị cho b: "))
        c = float(input("Nhập giá trị cho c: "))
        
        # Kiểm tra nếu c không bằng 0 để tránh lỗi chia cho 0
        if c == 0:
            print("Lỗi: Không thể chia cho 0!")
            return

        # Thực hiện phép tính
        result1 = a + b - c
        result2 = a * b / c

        # In kết quả
        print(f"Kết quả của a + b - c là: {result1}")
        print(f"Kết quả của a * b / c là: {result2}")

    except ValueError:
        print("Lỗi: Vui lòng nhập giá trị hợp lệ cho các số!")

if __name__ == "__main__":
    main()
