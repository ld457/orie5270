import numpy as np
from scipy.optimize import minimize, rosen

if __name__ == '__main__':
    trials = 100
    n = 3
    min_value = []
    x0_list = np.random.uniform(-100., 100, size=(trials, n))
    for i in range(trials):
        x0 = x0_list[i, :]
        res = minimize(rosen, x0, method='L-BFGS-B')
        min_value.append(res.fun)
    print "The average of the minimized value is %f" % np.mean(min_value)
