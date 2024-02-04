import unittest
from jp_consumer_theory.optimization import utility_optimize

class TestOptimization(unittest.TestCase):
    
    def test_optimization_result(self):
        # Define the parameters for the test
        PA = 50  # Price of good A
        PB = 50  # Price of good B
        Y = 100  # Income
        alpha = 0.5  # Utility function parameter
        
        # Call the function you want to test
        result = utility_optimize(PA, PB, Y, alpha)
        
        # Assert expected outcomes (you'll need to replace these with your expected results)
        self.assertIsNotNone(result)  # For example, check if the result is not None
        # Add more assertions here as needed
        
    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
