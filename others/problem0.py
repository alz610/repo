# %%
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

# %% [markdown]
# $$x_0, \, x_1 \sim \mathcal {U}[0, 1)$$
# $$a = \min \left\{x_0, \, x_1\right\}$$
# $$b = \max \left\{x_0, \, x_1\right\} - \min \left\{x_0, \, x_1\right\}$$
# $$c = 1 - \max \left\{x_0, \, x_1\right\}$$
# $$P\left( a + b > c \ \land \ c + a > b \ \land \ b + c > a \right) \, ?$$

# %% [markdown]
# \begin{equation}
#   P\left( a + b > c \ \land \ c + a > b \ \land \ b + c > a \right)
# \neq P\left( a + b > c \right) P\left( c + a > b \right) P\left( b + c > a \right)
# \end{equation}

# %% [markdown]
# \begin{align}
#   a + b &> c \\
#   \min + \max - \min &> 1 - \max \\
#   2 \max &> 1 \\
#   \max &> \frac 1 2
# \end{align}
# \begin{align}
#   c + a &> b \\
#   1 - \max + \min &> \max - \min \\
#   1 - \max + \min &> \max - \min \\
#   - 2\max + 2\min &> -1 \\
#   \max - \min &> \frac 1 2
# \end{align}
# \begin{align}
#   b + c &> a \\
#   \max - \min + 1 - \max &> \min \\
#   -2\min &> -1 \\
#   \min &< \frac 1 2
# \end{align}

# %% [markdown]
# \begin{equation}
#   a + b > c { \ \Rightarrow \ }
#   1 - c > c { \ \Rightarrow \ }
#   c < \frac 1 2 
# \end{equation}
# \begin{equation}
#   c + a > b { \ \Rightarrow \ }
#   1 - b > b { \ \Rightarrow \ }
#   b < \frac 1 2
# \end{equation}
# \begin{equation}
#   b + c > a { \ \Rightarrow \ }
#   1 - a > a { \ \Rightarrow \ }
#   a < \frac 1 2
# \end{equation}

# %%
n = 10000  # samples
# n = 100

x0_smpl = np.random.uniform(0, 1, n)
x1_smpl = np.random.uniform(0, 1, n)

min_smpl = np.minimum(x0_smpl, x1_smpl)
max_smpl = np.maximum(x0_smpl, x1_smpl)

P = np.arange(1, n + 1) / n


# plt.figure(figsize=(6*2, 4))


plt.subplot(221)

plt.plot(np.sort(max_smpl), P, label=r'$P(\max \leq x)$')

x = np.linspace(0, 1, 1000)
plt.plot(x, x**2, '--', label=r'$x^2$')

plt.xlabel('x')
plt.legend()


plt.subplot(222)

plt.plot(np.sort(min_smpl), P, label=r'$P(\min \leq x)$')

x = np.linspace(0, 1, 1000)
plt.plot(x, 1 - (x - 1)**2, '--', label=r'$1 - (x - 1)^2$')

plt.xlabel('x')
plt.legend()


plt.subplot(223)

plt.plot(np.sort(max_smpl - min_smpl), P, label=r'$P(\max - \min \leq x)$')

x = np.linspace(0, 1, 1000)
plt.plot(x, 1 - (x - 1)**2, '--', label=r'$1 - (x - 1)^2$')

plt.xlabel('x')
plt.legend()


plt.subplot(224)

plt.plot(np.sort(- min_smpl), P, label=r'$P(\max - \min \leq x)$')

x = np.linspace(-1, 0, 1000)
plt.plot(x, (x + 1)**2, '--', label=r'$(x + 1)^2$')

plt.xlabel('x')
plt.legend()

# plt.plot(np.sort(x0_smpl), P, label=r'$P(x_0 < x)$')
# plt.plot(np.sort(m_min_smpl), P, label=r'$P(\max - \min \leq x)$')

# %% [markdown]
# $$P(AB) = P(A) P(B|A)$$
# $$P(ABC) = P(AB) P(C|AB) = P(A) P(B|A) P(C|AB)$$
# $$f_{X, Y}(x, y) = f_X(x) \, f_{Y|X}(x, y)$$
# $$f_{X, Y, Z}(x, y, z) = f_{X, Y}(x, y) \, f_{Z|XY}(x, y, z)
# = f_{X, Y}(x, y) \, f_{Z|XY}(x, y, z)$$


# %% [markdown]
# $$P\left(\max \leq x\right) = x^2, \quad x \in [0, 1)$$
# $$P\left(\max - \min \leq x\right) = 1 - (x - 1)^2, \quad x \in [0, 1)$$
# $$P\left(\max \leq x\right) = x^2, \quad x \in [0, 1)$$
# $$P\left(\max\{x_0, x_1\} > x\right) = 1 - x^2$$
# $$P\left(a + b > c\right) = P\left(\max\{x_0, x_1\} > \frac 1 2\right) = \frac 3 4$$

# %%
np.count_nonzero(max_smpl > 1 / 2) / n

# %%
%%time
n = 10000  # samples
# n = 100

x0_smpl = np.random.uniform(0, 1, n)
x1_smpl = np.random.uniform(0, 1, n)

a_smpl = np.minimum(x0_smpl, x1_smpl)
c_smpl = 1 - np.maximum(x0_smpl, x1_smpl)
b_smpl = 1 - a_smpl - c_smpl

np.count_nonzero((a_smpl + b_smpl > c_smpl)) / n * \
np.count_nonzero((c_smpl + a_smpl > b_smpl)) / n * \
np.count_nonzero((b_smpl + c_smpl > a_smpl)) / n, \
np.count_nonzero((a_smpl + b_smpl > c_smpl)
            #    & (c_smpl + a_smpl > b_smpl)
               & (b_smpl + c_smpl > a_smpl)) / n
