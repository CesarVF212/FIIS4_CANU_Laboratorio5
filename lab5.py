import numpy as np

# Pesos. (coeficientes que multiplican a h).
PESOS = (9 / 4, 3 / 4)

a = 0.0
b = 1.0
h = (b - a) / 3

# Monomio. Se usa para comprobar hasta que grado somos capaces de acertar.
def monomio(x, k):
    return x**k

# Función usada.
def f(x):
    return x**2 * np.e**(-x)

# Fórmula del enunciado.
def cuadratura(f, a, b, h):
    x1 = a + h
    x2 = b

    # Evaluamos la integral en dos puntos concretos.
    return PESOS[0] * h * f(x1) + PESOS[1] * h * f(x2)


def main(tol = 1e-12):

    # Comprobamos usando un monomio hasta que grado somos capaces de integrar en ese intervalo.
    print("(a) Grado de exactitud sobre [0, 1]")

    grado = -1
    
    for k in range(0, 8):
    
        aprox = cuadratura(lambda x: monomio(x, k), a, b, h)

        # Valor correcto, analítico de la integral.
        exacto = 1 / (k + 1)

        err = abs(aprox - exacto)
        print(f"  k = {k}:  aprox = {aprox:.10f}   exacto = {exacto:.10f}   error = {err:.2e}")
    
        # Si nuestro error crece demasiado, asumimos que no podemos hacer mas aproximaciones.
        if err < tol:
            grado = k
    
        else:
            break
 
    print(f"  Grado de exactitud experimental: {grado}")

    # Aplicamos la cuadracattura.
    I_aprox = cuadratura(f, a, b, h)
    print(f"\n(b) Aproximacion de la integral: I_aprox = {I_aprox:.10f}")

    # Hacemos mediante integración por partes la integral de forma analítica.
    I_exacto = 2 - 5 * np.exp(-1)
    error = abs(I_aprox - I_exacto)

    print(f"(c) Valor exacto:     I_exacto = {I_exacto:.10f}")
    print(f"    Error absoluto:   |I_aprox - I_exacto| = {error:.10f}")

main()