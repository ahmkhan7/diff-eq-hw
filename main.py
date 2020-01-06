# Problem:
# dx/dy = 2x + y
# y(0) = 1
# Solve the given differential equation using the Euler and Runge-Kutta methods

# Some background:

# Many useful first-order differential equations don't have a 'clean' algebraic solution
# We can still get an approximate solution using the Euler and Fourth Order Runge-Kutta methods

# I was given the above problem as homework for differential equations
# Runge-Kutta is very tedious to do by hand
# So, I wrote this program to do the tedious work for me

import math 

# Plugs x and y into given formula
def dxdy(x, y):
    return 2 * x + y

# Fourth Order Runge-Kutta method
def runge_kutta_solution(step, x, y):
    F1 = step * dxdy(x, y)
    F2 = step * dxdy(x + step / 2, y + F1 / 2)
    F3 = step * dxdy(x + step / 2, y + F2 / 2)
    F4 = step * dxdy(x + step, y + F3)
    return y + (1.0 / 6.0) * (F1 + 2 * F2 + 2 * F3 + F4)

# Euler method
def euler_solution(step, x, y):
    return y + step * dxdy(x, y)

# Finds exact solution (for comparison with approximations)
def exact_solution(x):
    return 3 * math.exp(x) - 2 * x - 2         # math.exp(x) = e^x

step = 0.1
x = 0.0
y = 1

iterations = (int)(1 / step) + 1

print("Runge-Kutta solution: ")
for i in range (iterations):
    print("x = " + str(x) + ": " + str(runge_kutta_solution(step, x, y)))
    y = runge_kutta_solution(step, x, y)
    x += step

x = 0.0
y = 1

print("Euler solution: ")
for i in range (iterations):
    print("x = " + str(x) + ": " + str(euler_solution(step, x, y)))
    y = euler_solution(step, x, y)
    x += step

x = 0
y = 1

print("Exact solution: ")
for i in range (iterations):
    x += step
    print("x = " + str(x - step) + ": " + str(exact_solution(x)))
