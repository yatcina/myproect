import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x = np.linspace(0, 10, num=11, endpoint=True)
y = [10,34,23,34,45,67,45,2,34,45,3]
f = interp1d(x, y)
f2 = interp1d(x, y, kind='quadratic')
xnew = np.linspace(0, 10, num=50, endpoint=True)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
#asaasasas
