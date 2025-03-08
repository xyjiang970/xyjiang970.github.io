---
layout: default
title: Calculus 1 Notes
permalink: /notes/calculus/calc1notes/
description:
---

# Calculus 1 Notes

[Home](../../../) >> [Notes](../../) >> Calculus 1 Notes

# Table of Contents

- [Calculus 1 Notes](#calculus-1-notes)
  - [Introduction to Limits](#introduction-to-limits)
  - [Calculus 1: Major Rules and Concepts](#calculus-1-major-rules-and-concepts)
- [Limits](#limits)
  - [Constant Rule for Limits](#constant-rule-for-limits)
  - [Limit of a Linear Function](#limit-of-a-linear-function)
  - [Sum, Difference, Product, and Quotient Rules](#sum-difference-product-and-quotient-rules)
  - [Special Limits](#special-limits)
- [Derivatives](#derivatives)
  - [Definition of a Derivative](#definition-of-a-derivative)
  - [Power Rule](#power-rule)
  - [Constant Rule](#constant-rule)
  - [Sum and Difference Rules](#sum-and-difference-rules)
  - [Product Rule](#product-rule)
  - [Quotient Rule](#quotient-rule)
  - [Chain Rule](#chain-rule)
  - [Derivatives of Trigonometric Functions](#derivatives-of-trigonometric-functions)
- [Applications of Derivatives](#applications-of-derivatives)
  - [Critical Points and Extrema](#critical-points-and-extrema)
  - [Mean Value Theorem](#mean-value-theorem)
  - [Related Rates](#related-rates)
  - [L'Hôpital's Rule](#lhôpitals-rule)
- [Integration](#integration)
  - [Indefinite Integrals](#indefinite-integrals)
  - [Basic Integral Rules](#basic-integral-rules)
  - [Substitution Rule](#substitution-rule)
  - [Definite Integrals and the Fundamental Theorem of Calculus](#definite-integrals-and-the-fundamental-theorem-of-calculus)
  - [Integration by Parts](#integration-by-parts)

## Limits

### Constant Rule for Limits

The constant rule states that the limit of a constant is the constant itself. If $c$ is a constant, then:

$$
\lim_{x \to a} c = c
$$

### Limit of a Linear Function

For a linear function $f(x) = x$, the limit is straightforward:

$$
\lim_{x \to a} x = a
$$

### Sum, Difference, Product, and Quotient Rules

1. **Sum Rule**: The limit of a sum is the sum of the limits:

$$
\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)
$$

2. **Difference Rule**: The limit of a difference is the difference of the limits:

$$
\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)
$$

3. **Product Rule**: The limit of a product is the product of the limits:

$$
\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)
$$

4. **Quotient Rule**: The limit of a quotient is the quotient of the limits, as long as the denominator does not approach zero:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if } \lim_{x \to a} g(x) \neq 0
$$

### Special Limits

1. **Sine Limit**: One of the most important special limits is:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

2. **Exponential Limit**: Another crucial limit is:

$$
\lim_{x \to 0} (1 + x)^{1/x} = e
$$

## Derivatives

### Definition of a Derivative

The derivative of a function at a point is defined as the limit of the difference quotient:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

### Power Rule

The power rule is used to differentiate functions of the form $f(x) = x^n$, where $n$ is any real number:

$$
\frac{d}{dx} x^n = n x^{n-1}
$$

### Constant Rule

The derivative of a constant is always zero:

$$
\frac{d}{dx} c = 0
$$

### Sum and Difference Rules

1. **Sum Rule**: The derivative of the sum of two functions is the sum of the derivatives:

$$
\frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x)
$$

2. **Difference Rule**: The derivative of the difference of two functions is the difference of the derivatives:

$$
\frac{d}{dx} [f(x) - g(x)] = f'(x) - g'(x)
$$

### Product Rule

The derivative of the product of two functions is given by the product rule:

$$
\frac{d}{dx} [f(x) g(x)] = f'(x) g(x) + f(x) g'(x)
$$

### Quotient Rule

The derivative of a quotient of two functions is given by the quotient rule:

$$
\frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}
$$

### Chain Rule

The chain rule is used to differentiate composite functions:

$$
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
$$

### Derivatives of Trigonometric Functions

Here are the derivatives of the basic trigonometric functions:

$$
\frac{d}{dx} \sin x = \cos x
$$

$$
\frac{d}{dx} \cos x = -\sin x
$$

$$
\frac{d}{dx} \tan x = \sec^2 x
$$

$$
\frac{d}{dx} \cot x = -\csc^2 x
$$

$$
\frac{d}{dx} \sec x = \sec x \tan x
$$

$$
\frac{d}{dx} \csc x = -\csc x \cot x
$$

## Applications of Derivatives

### Critical Points and Extrema

Critical points occur where the derivative is zero or undefined. These points are used to find local maxima and minima, which can be determined using:

- The **First Derivative Test**: Analyze the sign of the derivative before and after the critical point.
- The **Second Derivative Test**: If $f''(x) > 0$, the function is concave up, and if $f''(x) < 0$, the function is concave down at the critical point.

### Mean Value Theorem

The Mean Value Theorem states that there exists at least one point $c$ in the interval $(a, b)$ such that:

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$

### Related Rates

To solve related rates problems, differentiate both sides of an equation with respect to time $t$, and solve for the unknown rates.

### L'Hôpital's Rule

L'Hôpital's Rule is used to evaluate indeterminate limits of the form $\frac{0}{0}$ or $\frac{\pm \infty}{\pm \infty}$:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{if } \lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \text{ or } \pm \infty
$$

## Integration

### Indefinite Integrals

Indefinite integrals are used to find antiderivatives. The general formula for the power rule is:

$$
\int x^n \,dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1
$$

### Basic Integral Rules

1. **Constant Rule**:

$$
\int c \,dx = cx + C
$$

2. **Exponential Rule**:

$$
\int e^x \,dx = e^x + C
$$

3. **Sine Rule**:

$$
\int \sin x \,dx = -\cos x + C
$$

4. **Cosine Rule**:

$$
\int \cos x \,dx = \sin x + C
$$

### Substitution Rule

The substitution rule is used when the integrand contains a composite function. The rule is:

$$
\int f(g(x)) g'(x) \,dx = \int f(u) \,du
$$

### Definite Integrals and the Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus relates differentiation and integration. It states that:

$$
\int_a^b f(x) \,dx = F(b) - F(a)
$$

### Integration by Parts

The integration by parts formula is:

$$
\int u \, dv = uv - \int v \, du
$$

<br>
