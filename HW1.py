import matplotlib.pyplot as plt
import numpy as np
from operator import add
import math 

def problem9():
    # 9c start
    array = np.random.uniform(0,1,10000)
    plt.hist(array, bins='auto', rwidth = 0.8)
    plt.show()
    # 9c end
    """
    print(np.arange(1,10).reshape((3,3)) * np.arange(1,4).reshape((3,1))) # 9a

    steps = 1000 # 9b start
    start = -math.pi
    stop = math.pi
    x = np.linspace(start, stop, steps)
    y = []
    for i in x:
        y.append(math.sin(i))

    plt.plot(x,y)
    plt.show() # 9b end
    """


def problem10():
    
    tests = 100000
    count = 0

    for i in range(tests):
        if problem10helper():
            count += 1

    probability = count / tests
    print(probability) # simulated result

    product = 1
    for i in range(49):
        product *= (364-i) / 365
    print(1-product) # calculated result

def problem10helper():
    numStudents = 50
    days = 365
    birthdays = np.random.randint(0,days, numStudents)
    if len(birthdays) == len(set(birthdays)):
        return False
    return True



def problem11():
    valuesz = 10000 * [0]
    np.random.seed()
    k = 100
    bins = [k-0.5]
    for i in range(k,6*k):
        bins.append(i+0.5)
    for i in range(k):
        valuesi = np.random.randint(1,7,10000)
        valuesz = list(map(add, valuesi, valuesz))

    plt.hist(valuesz, bins, rwidth=0.8)
    plt.show()

problem9()
#problem10()
#problem11()

