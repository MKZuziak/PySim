if __name__ == '__main__':
    from Galilean_Model import outfielder
    import numpy as np
    x = np.linspace(0, 4.0, 400)
    outfielder_problem = outfielder.outfilder_simulation()
    outfielder_problem.plot_ball_trajectory(x=x, v1=1, v2=10)