def calculate(a, b, c):
    result1 = a + b - c
    result2 = a * b / c
    return result1, result2

def main(a, b, c):
    result1, result2 = calculate(a, b, c)
    print(f"Kết quả của a + b - c là: {result1}")
    print(f"Kết quả của a * b / c là: {result2}")

if __name__ == "__main__":
    a = float(input("Nhập giá trị cho a: "))
    b = float(input("Nhập giá trị cho b: "))
    c = float(input("Nhập giá trị cho c: "))
    main(a, b, c)
