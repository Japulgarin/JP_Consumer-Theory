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
        
        # Assert expected outcomes
        self.assertIsNotNone(result)  # Ensure the result is not None
        
        # You can add more specific assertions based on your function's behavior
        # For example, check if the result is a numeric value
        self.assertIsInstance(result, (int, float)) 
        
        # You can also check if the result is within a certain range or meets specific criteria
        # For example, check if the result is greater than or equal to 0
        self.assertGreaterEqual(result, 0)
        
    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
