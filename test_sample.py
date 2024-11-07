import unittest
from unittest.mock import patch
from app import main

class TestApp(unittest.TestCase):
    @patch('builtins.print')  # Mô phỏng hàm print
    def test_main(self, mock_print):
        # Thực hiện các phép tính và kiểm tra output
        main(5, 3, 2)  # Gọi hàm main với các giá trị mẫu
        
        # Kiểm tra kết quả đầu ra của print
        mock_print.assert_any_call("Kết quả của a + b - c là: 6.0")
        mock_print.assert_any_call("Kết quả của a * b / c là: 7.5")

if __name__ == "__main__":
    unittest.main()
