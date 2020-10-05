# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from scipy.linalg import solve_banded


def solve(n, a_, c_, b_, f_):

    ab = np.empty((3, n))

    # ab[((0, 2), (0, n - 1))] = 0

    ab[0] = b_
    ab[1] = c_
    ab[2] = a_

    f = np.full(n, f_)

    x = solve_banded((1, 1), ab, f)

    return x


!gcc solve.c

# %% [markdown]
# $$
# \begin{pmatrix}
# c & b &&& \\
# a & c & b && \\
#   & a & \ddots & \ddots & \\
#   &   & \ddots & \ddots & b \\
# &&& a & c
# \end{pmatrix}
# \times
# \begin{pmatrix}
# x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n
# \end{pmatrix}
# =
# \begin{pmatrix}
# f \\ f \\ \vdots \\ \vdots \\ f
# \end{pmatrix}
# $$
#
# $$(a, c, b, f) = (1, 3, 1, 1)$$

# %%
print('n =', 20, '\n\n')
print("Python code:\n")
x = %time solve(20, 1, 3, 1, 1)
print(x)

print("\n\nC code:\n")
!./a.out 20 1 3 1 1 show
# %%
print('n =', 100000000, '\n\n')
print("Python code:\n")
%time solve(100000000, 1, 3, 1, 1)

print("\n\nC code:\n")
!./a.out 100000000 1 3 1 1