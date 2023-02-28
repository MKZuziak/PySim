import numpy as np
import matplotlib.pyplot as plt

class outfilder_simulation:
    def __init__(self) -> None:
        self.a = -9.81
    def ball_trajectory(self, x: object, v1: float, v2: float) -> object:
        """
        Args:
        x: np.array|int, horizontal position of ball
        v1: float, the starting speed of the ball in the x (horizontal) direction
        v2: float, the starting speed of the ball in the y (vertical) direction

        Returns:
        y: np.array|int, vertical position of the ball.
        """
        location = (v2 / v1)*x + (self.a * (x**2)) / (2 * (v1**2))
        if type(location) != int:
            location[location < 0] = 0
        return location
    
    def plot_ball_trajectory(self, x: object, v1: float, v2: float) -> object:
        """
        Args:
        x: np.array|int, horizontal position of ball
        v1: float, the starting speed of the ball in the x (horizontal) direction
        v2: float, the starting speed of the ball in the y (vertical) direction

        Returns:
        y: np.array|int, vertical position of the ball.
        """
        y = self.ball_trajectory(x=x, v1=v1, v2=v2)
        plt.plot(y)
        plt.title("The trajectory of a Thrown Ball")
        plt.xlabel("Horizontal Position of ball")
        plt.ylabel("Vertical position of ball")
        plt.axhline(y = 0)
        plt.show()
