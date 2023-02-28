import unittest
import numpy as np
from Galilean_Model import outfielder
import matplotlib.pyplot as plt

class TestOutfileder(unittest.TestCase):
    def book_polynomial(self, x):
        return 10*x - 5*(x**2)
    
    def comparision_test(self, show_diagram = False):
        xs = np.array([x/100 for x in list(range(201))])
        xs_array = np.linspace(0.00, 2.00, 201)
        self.assertTrue(np.all(np.isclose(xs, xs_array) == True))
        
        outfield = outfielder.outfilder_simulation()
        ys = self.book_polynomial(xs)
        ys_array = outfield.ball_trajectory(xs_array, v1=0.99, v2=9.99)
        #self.assertTrue(np.all(np.isclose(ys, ys_array) == True))
        
        if show_diagram == True:
            fig, ax = plt.subplots()
            ax.plot(ys)
            ax.plot(ys_array)
            plt.show()

def main():
    outfielder = TestOutfileder()
    outfielder.comparision_test(show_diagram=True)

if __name__ == "__main__":
    main()