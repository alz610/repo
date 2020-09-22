# %% [markdown]
# 
# .. _demo_poisson_equation:
# 
# Poisson equation
# ================
# 
# This demo is implemented in a single Python file,
# :download:`demo_poisson.py`, which contains both the variational forms
# and the solver.
# 
# This demo illustrates how to:
# 
# * Solve a linear partial differential equation
# * Create and apply Dirichlet boundary conditions
# * Define Expressions
# * Define a FunctionSpace
# * Create a SubDomain
# 
# The solution for :math:`u` in this demo will look as follows:
# 
# .. image:: poisson_u.png
#    :scale: 75 %
# 
# 
# Equation and problem definition
# -------------------------------
# 
# The Poisson equation is the canonical elliptic partial differential
# equation.  For a domain :math:`\Omega \subset \mathbb{R}^n` with
# boundary :math:`\partial \Omega = \Gamma_{D} \cup \Gamma_{N}`, the
# Poisson equation with particular boundary conditions reads:
# 
# .. math::
#    - \nabla^{2} u &= f \quad {\rm in} \ \Omega, \\
#                 u &= 0 \quad {\rm on} \ \Gamma_{D}, \\
#                 \nabla u \cdot n &= g \quad {\rm on} \ \Gamma_{N}. \\
# 
# Here, :math:`f` and :math:`g` are input data and :math:`n` denotes the
# outward directed boundary normal. The most standard variational form
# of Poisson equation reads: find :math:`u \in V` such that
# 
# .. math::
#    a(u, v) = L(v) \quad \forall \ v \in V,
# 
# where :math:`V` is a suitable function space and
# 
# .. math::
#    a(u, v) &= \int_{\Omega} \nabla u \cdot \nabla v \, {\rm d} x, \\
#    L(v)    &= \int_{\Omega} f v \, {\rm d} x
#    + \int_{\Gamma_{N}} g v \, {\rm d} s.
# 
# The expression :math:`a(u, v)` is the bilinear form and :math:`L(v)`
# is the linear form. It is assumed that all functions in :math:`V`
# satisfy the Dirichlet boundary conditions (:math:`u = 0 \ {\rm on} \
# \Gamma_{D}`).
# 
# In this demo, we shall consider the following definitions of the input
# functions, the domain, and the boundaries:
# 
# * :math:`\Omega = [0,1] \times [0,1]` (a unit square)
# * :math:`\Gamma_{D} = \{(0, y) \cup (1, y) \subset \partial \Omega\}`
#   (Dirichlet boundary)
# * :math:`\Gamma_{N} = \{(x, 0) \cup (x, 1) \subset \partial \Omega\}`
#   (Neumann boundary)
# * :math:`g = \sin(5x)` (normal derivative)
# * :math:`f = 10\exp(-((x - 0.5)^2 + (y - 0.5)^2) / 0.02)` (source
#   term)

# %%
from dolfin import *

def closure(n=1):
    # Create mesh and define function space
    mesh = UnitSquareMesh(n*32, n*32)
    V = FunctionSpace(mesh, "Lagrange", 1)

    # Define Dirichlet boundary (x = 0 or x = 1)
    def boundary(x):
        return x[0] < DOLFIN_EPS or x[0] > 1.0 - DOLFIN_EPS

    # Define boundary condition
    u0 = Constant(0.0)
    bc = DirichletBC(V, u0, boundary)

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Expression("10*exp(-(pow(x[0] - 0.5, 2) + pow(x[1] - 0.5, 2)) / 0.02)", degree=2)
    g = Expression("sin(5*x[0])", degree=2)
    a = inner(grad(u), grad(v))*dx
    L = f*v*dx + g*v*ds

    # Compute solution
    u = Function(V)
    solve(a == L, u, bc)

    return u

# %%
n = 5

parameters["linear_algebra_backend"] = "PETScCusp"
%timeit closure(n)

parameters["linear_algebra_backend"] = "PETSc"
%timeit closure(n)

# %%
import matplotlib.pyplot as plt
n = 5

parameters["linear_algebra_backend"] = "PETScCusp"
u = %time closure(n)
plot(u)
plt.show()

parameters["linear_algebra_backend"] = "PETSc"
u = %time closure(n)
plot(u)
plt.show()

# %% [markdown]
PETScCusp
CPU times: user 5.07 s, sys: 233 ms, total: 5.3 s
Wall time: 5.29 s

PETSc
CPU times: user 6.59 s, sys: 3.2 s, total: 9.78 s
Wall time: 4.99 s