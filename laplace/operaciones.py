import sympy as smp
from sympy.abc import s, t, x, y, z, a, u, U, k, X, Y, Z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
from sympy import Heaviside
from sympy import Eq, sympify, limit
from sympy import symbols, Function, solve, integrate, Integral, Matrix, solve_linear_system


def L(f):
    return laplace_transform(f, t, s, noconds=True)


def inv_L(F, variable_retorno):
    return inverse_laplace_transform(F, s, variable_retorno, noconds=True)


def L_diff(f, f0, fp0, fpp0=0, orden_derivada=1):  # esta función es para calcular transformadas de derivadas
    """
    input:
    f es una variable simbólica de sympy que representa a la función f(t) a la que se quiere calcular
      la transformada de alguna de sus derivadas.

    n puede asumir los valores de 0,1,2,3 y representa el orden de la derivada de la función f(t)
    """
    F = str(f).upper().split('(')[0]
    F = symbols(F)
    F = Function(F)(s)
    if orden_derivada == 0:
        L = F
    elif orden_derivada == 1:
        L = s * F - f0
    elif orden_derivada == 2:
        L = s ** 2 * F - s * f0 - fp0
    elif orden_derivada == 3:
        L = s ** 3 * F - s ** 2 * f0, -s * fp0 - fpp0
    return L


def armar_ecuacion(primer_miembro, segundo_miembro):
    return Eq(primer_miembro, segundo_miembro)


def resolver_ecuacion(ecuacion, incognita):
    return solve([ecuacion], (incognita))


def resolver_sistema_ecuaciones(ecuaciones, incognita):
    return solve(ecuaciones, (incognita))


def transformada_division_por_t(funcion):
    return smp.integrate(funcion, (U, s, limit(funcion, s, smp.oo)))


x = Function('x')(t)  # Definimos a x, y, z como funciones del tiempo
y = Function('y')(t)
z = Function('z')(t)
X = Function('X')(s)  # Defnimos a X, Y, Z como funciones de s
Y = Function('Y')(s)
Z = Function('Z')(s)

u = smp.Symbol('u', positive=True)
