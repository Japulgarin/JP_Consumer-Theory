import unittest
import matplotlib.pyplot as plt  # Import matplotlib for testing
from jp_consumer_theory.plotting import optimum_plot

class TestPlotting(unittest.TestCase):
    
    def test_optimum_plot(self):
        # Define the parameters for the test
        PA = 20  # Price of good A
        PB = 30  # Price of good B
        Y = 100  # Income
        alpha = 0.7  # Utility function parameter
        
        # Call the function you want to test
        plt.figure()  # Create a figure for testing
        optimum_plot(PA, PB, Y, alpha)
        
        # You can add assertions related to the plot if needed
        # For example, check if certain elements exist in the plot
        
    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
