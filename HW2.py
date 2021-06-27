import matplotlib.pyplot as plt
import numpy as np

def problem12():
    PMF = [0.3, 0.1, 0.15, 0.25, 0.1, 0.08, 0.02]
    bins = [0.5]
    for i in range(len(PMF)):
        bins.append(i+1.5)
    array = np.random.uniform(0,1,100000)
    emperical = []
    for data in array:
        value = 0
        for prob in PMF:
            value += 1
            if data < prob:
                emperical.append(value)
                break
            else:
                data -= prob

    plt.hist(emperical, bins, rwidth=0.8)
    plt.show()


problem12()