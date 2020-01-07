#Serdar Gürler
#Minimize          w = 2*y1 + 3*y2 + 5*y3
#Subject to:       y1 - y2 + y3 >= 500
#                  y1 - 2*y2    >= 0
#                            y3 >= 30
#with              y1 >= 0, y2 >= 0

import numpy as np
from scipy.optimize import linprog

A = np.array([[-1, 1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
b = np.array([-500, 0, -30, 0, 0])
c = np.array([2,3,5])

res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal değer:',res.fun)
print('X:',res.x)

