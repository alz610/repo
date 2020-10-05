# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from scipy.linalg import solve_banded

# %%
%%time
n = 100000000
a_, c_, b_, f_ = 1, 3, 1, 1

ab = np.zeros((3, n))

ab[((0, 2), (0, n - 1))] = 0

ab[0] = b_
ab[1] = c_
ab[2] = a_

f = np.full(n, f_)

x = solve_banded((1, 1), ab, f)

# %%
!gcc solve.c
!./a.out 100000000 1 3 1 1
