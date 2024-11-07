import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        with self.assertLogs(level='INFO') as log:
            main(5, 3, 2)  # Truyền tham số vào thay vì nhập qua input
            self.assertIn("Kết quả của a + b - c là: 6.0", log.output)
            self.assertIn("Kết quả của a * b / c là: 7.5", log.output)

if __name__ == "__main__":
    unittest.main()
