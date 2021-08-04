import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams["figure.figsize"] = 10,6
np.random.seed(42)

norm_rv = stats.norm(loc=30, scale=5)
samples = np.trunc(norm_rv.rvs(365))
print(samples[:30])
