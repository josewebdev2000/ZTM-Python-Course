# Write unit tests for the main.py file that contains code for a guess my number game
import unittest
import main

class TestGame(unittest.TestCase):
    
    def test_input(self):
        """Test when user guesses the number"""
        answer = 5
        guess = 5
        result = main.run_guess(answer, guess)
        self.assertTrue(result)
    
    def test_input_wrong(self):
        """Test when user makes a wrong guess"""
        
        result = main.run_guess(5,6)
        self.assertFalse(result)
    
    def test_input_wrong_number(self):
        """Test when user enters a number out of range"""
        result = main.run_guess(5,11)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()