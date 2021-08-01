from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
def quadratic(a=1,b=1,c=1):
    x = np.linspace(-10, 10, 1000)

    # calculate the y value for each element of the x vector
    a=0.1
    b=2
    c=2
    y = a*x*x + b*x + c
    fig=Figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    plt.show()
    return 
quadratic()