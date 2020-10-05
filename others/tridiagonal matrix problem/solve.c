#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

	/**
	 * n - число уравнений (строк матрицы)
	 * b - диагональ, лежащая над главной (нумеруется: [0;n-2])
	 * c - главная диагональ матрицы A (нумеруется: [0;n-1])
	 * a - диагональ, лежащая под главной (нумеруется: [1;n-1])
	 * f - правая часть (столбец)
	 * x - решение, массив x будет содержать ответ
	 */
void solveMatrix (int n, double *a, double *c, double *b, double *f, double *x)
{
	double m;
	for (int i = 1; i < n; i++)
	{
		m = a[i]/c[i-1];
		c[i] = c[i] - m*b[i-1];
		f[i] = f[i] - m*f[i-1];
	}

	x[n-1] = f[n-1]/c[n-1];

	for (int i = n - 2; i >= 0; i--)
    {
		x[i]=(f[i]-b[i]*x[i+1])/c[i];
    }
}

int main(int argc, char const *argv[])
{
    clock_t begin = clock();


    int n = atoi(argv[1]);
    int a_ = atoi(argv[2]);
    int c_ = atoi(argv[3]);
    int b_ = atoi(argv[4]);
    int f_ = atoi(argv[5]);
    // int n = 100000000, a_ = 1, c_ = 3, b_ = 1, f_ = 1;

    double *a = malloc(n * sizeof(double));
    double *c = malloc(n * sizeof(double));
    double *b = malloc(n * sizeof(double));
    double *f = malloc(n * sizeof(double));
    double *x = malloc(n * sizeof(double));


    a[0] = 0;
    c[0] = c_;
    b[0] = b_;
    f[0] = f_;

    for (size_t i = 1; i < n - 1; i++)
    {
        a[i] = a_;
        c[i] = c_;
        b[i] = b_;
        f[i] = f_;
    }

    a[n-1] = a_;
    c[n-1] = c_;
    b[n-1] = 0;
    f[n-1] = f_;



    solveMatrix(n, a, c, b, f, x);


    double elapsed = (double)(clock() - begin) / CLOCKS_PER_SEC;
    printf("Elapsed: %f s\n", elapsed);


    if ((argc > 6) && (!strcmp(argv[6], "show")))
    {
        printf("\n");
        for (size_t i = 0; i < n; i++)
            printf("%.8f ", x[i]);
    }


    return 0;
}
