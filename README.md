# Two-Node Quadrature Rule: Degree of Exactness and Error Analysis

This exercise studies a two-node quadrature rule on [0, 1], determining its degree of exactness experimentally.
It then applies the rule to approximate ∫₀¹ x²e⁻ˣ dx and compares the result with the exact value to compute the absolute error.

## Problem Statement

On the interval [a, b], consider the partition x₀, x₁, x₂ with x₀ = a, x₁ = a + h and x₂ = b, where h = (b − a) / 3. The quadrature rule is

```
I[f] = (9/4)·h·f(x₁) + (3/4)·h·f(x₂)
```

**(a)** Determine experimentally the degree of exactness of the rule on the interval [0, 1].

**(b)** Apply the rule to estimate

```
∫₀¹ x² e⁻ˣ dx
```

**(c)** Compute analytically the exact value of the integral and show the absolute error with respect to the value obtained in part (b).

## Solution

On [0, 1], h = 1/3, x₁ = 1/3 and x₂ = 1, so the rule becomes:

```
I[f] = (3/4)·f(1/3) + (1/4)·f(1)
```

### (a) Degree of exactness

The rule is tested against monomials of increasing degree:

| f(x) | I[f]            | Exact integral | Exact? |
|------|-----------------|----------------|--------|
| 1    | 3/4 + 1/4 = 1   | 1              | Yes    |
| x    | 1/4 + 1/4 = 1/2 | 1/2            | Yes    |
| x²   | 1/12 + 1/4 = 1/3 | 1/3           | Yes    |
| x³   | 1/36 + 1/4 = 5/18 | 1/4          | No     |

The rule integrates exactly all polynomials up to degree 2 and fails for x³, so its **degree of exactness is 2**. This corresponds to the two-point Radau rule with nodes 1/3 and 1.

### (b) Approximation of ∫₀¹ x²e⁻ˣ dx

With f(x) = x²e⁻ˣ:

- f(1/3) = (1/9)·e^(−1/3) ≈ 0.0796146
- f(1) = e⁻¹ ≈ 0.3678794

```
I ≈ (3/4)(0.0796146) + (1/4)(0.3678794)
  ≈ 0.0597110 + 0.0919699
  ≈ 0.151681
```

### (c) Exact value and absolute error

Integrating by parts twice:

```
∫ x² e⁻ˣ dx = −e⁻ˣ (x² + 2x + 2)

∫₀¹ x² e⁻ˣ dx = 2 − 5e⁻¹ ≈ 0.160603
```

Absolute error:

```
|0.160603 − 0.151681| ≈ 8.92 × 10⁻³
```

The error is noticeable because the rule is exact only up to degree 2, while x²e⁻ˣ has higher-degree terms in its Taylor expansion.

## Summary

| Quantity                | Value        |
|-------------------------|--------------|
| Degree of exactness     | 2            |
| Approximation (rule)    | 0.151681     |
| Exact value (2 − 5/e)   | 0.160603     |
| Absolute error          | 8.92 × 10⁻³  |

## Opción B — Integración Numérica

Sobre $[a, b]$ se considera la partición $\{x_0, x_1, x_2\}$ con $x_0 = a$, $x_1 = a + h$ y $x_2 = b$, donde $h = (b - a)/3$. La regla de cuadratura es

$$
I[f] = \tfrac{9}{4}\, h\, f(x_1) + \tfrac{3}{4}\, h\, f(x_2).
$$

**(a)** Determina **experimentalmente** el grado de exactitud de la regla sobre el intervalo $[0, 1]$.

**(b)** Aplica la regla para estimar

$$
\int_0^1 x^2 e^{-x}\, dx.
$$

**(c)** Calcula **analíticamente** el valor exacto de la integral y muestra el **error absoluto** frente al valor obtenido en el apartado (b).
