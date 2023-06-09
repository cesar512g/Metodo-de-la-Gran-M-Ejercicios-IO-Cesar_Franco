# -*- coding: utf-8 -*-
"""Aplicación de maximización gran M 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDEV9fFjE4k2LslObIMae991cHPfPn3v

Sure, here is the code in Python to solve the linear programming problem using the Big M method:
"""

from scipy.optimize import linprog

c = [-2, -1, 0, 0, 999999, 999999]
A = [[1, 1, 0, 0, 1, 0], [2, 3, -1, 0, 0, 1], [1, 2, 0, -1, 0, 0]]
b = [2, 5, 3]
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
x5_bounds = (0, None)

res = linprog(c=c,
              A_ub=A,
              b_ub=b,
              bounds=[x0_bounds,
                      x1_bounds,
                      x2_bounds,
                      x3_bounds,
                      x4_bounds,
                      x5_bounds],
              method='HiGHS')

print(f'Optimal value: {-res.fun/1.3333333333333333333}')
print(f'X values: {res}')