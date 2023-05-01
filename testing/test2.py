import unittest
from main import do_stuff

# Create a class for unitests
# Name it after the file that contains the code you wish to test
class TestMain(unittest.TestCase):
    
    def setUp(self):
        """Run code before each unit test"""
        print("About to start unit tests")
    
    # Each method is a test
    def test_do_stuff(self):
        """Fantastic"""
        test_param = 10
        result = do_stuff(test_param)
        
        # Makes sure two given parameters are equal
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        """Awesome"""
        result = do_stuff('sdfgfd')
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        
        result = do_stuff(None)
        self.assertEqual(result, "please enter a number")
    
    def test_do_stuff4(self):
        
        result = do_stuff("")
        self.assertEqual(result, "please enter a number")
    
    def tearDown(self):
        """Unset variables at the end of unit tests"""
        print("Cleaning up")

# Run all unit tests
if __name__ == "__main__":
    unittest.main()