import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        print("test_one_word")
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")
    
    def test_multiple_words(self):
        print("test_multiple_words")
        text = "python hello world"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python Hello World")

if __name__ == "__main__":
    unittest.main()