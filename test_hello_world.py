import unittest
from hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world function."""
    
    def test_hello_world_returns_correct_string(self):
        """Test that hello_world returns the correct greeting."""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
    
    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string type."""
        result = hello_world()
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
