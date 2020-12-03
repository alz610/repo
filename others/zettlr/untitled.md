$$
\displaystyle
S = \int\limits_a^b f(x) \, \mathrm dx
$$

$$
\displaystyle
S_n = \sum_{i=1}^n a_i
$$

$$
\displaystyle
\lim_{n \rightarrow \infty} S_n = S
$$

$$
\displaystyle
a_i = f(x_i) \, \Delta x
$$

$$
\displaystyle
\Delta x = \frac {b - a} n
$$

$$
\displaystyle
x_i = i \, \Delta x - a
$$

$$
\displaystyle
a_i = f\left(i \, \frac {b - a} n - a\right) \, \frac {b - a} n
$$

Найти неопределенный интеграл от $x$ 
$$
\displaystyle
S = \int\limits_0^x x \, \mathrm dx
$$

$$
\displaystyle
S = \lim_{n \rightarrow \infty} \sum_{i=1}^n i \, \frac {x^2} {n^2} 
$$

$$
\displaystyle
a_i = i \, \frac {x^2} {n^2}
$$

$$
\displaystyle
\sum_{i=1}^n i = \frac {1 + n} 2 \, n
$$

$$
\displaystyle
S_n = \frac {1 + n} 2 \, n \, \frac {x^2} {n^2} = \frac {1 + n} {2 n} \, x^2
$$

$$
\displaystyle
S = x^2 \lim_{n \rightarrow \infty} \frac {1 + n} {2 n} = \frac {x^2} 2
$$