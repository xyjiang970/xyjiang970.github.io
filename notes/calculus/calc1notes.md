---
layout: default
title: Calculus 1 Notes
permalink: /notes/calculus/calc1notes/
description:
---

# Calculus 1 Notes

[Home](../../../) >> [Notes](../../) >> Calculus 1 Notes

## Introduction to Limits

### Constant Rule for Limits

$$ \lim\_{{x \to a}} c = c $$

### Limit of a Linear Function

$$ \lim\_{{x \to a}} x = a $$

### Sum, Difference, Product, and Quotient Rules

$$ \lim*{{x \to a}} [f(x) \pm g(x)] = \lim*{{x \to a}} f(x) \pm \lim*{{x \to a}} g(x) $$
$$ \lim*{{x \to a}} [f(x) g(x)] = \lim*{{x \to a}} f(x) \cdot \lim*{{x \to a}} g(x) $$
$$ \lim*{{x \to a}} \frac{f(x)}{g(x)} = \frac{\lim*{{x \to a}} f(x)}{\lim*{{x \to a}} g(x)}, \quad \text{if } \lim*{{x \to a}} g(x) \neq 0 $$

### Special Limits

$$ \lim*{{x \to 0}} \frac{\sin x}{x} = 1 $$
$$ \lim*{{x \to 0}} (1 + x)^{1/x} = e $$

## Derivatives

### Definition of a Derivative

$$ f'(x) = \lim\_{{h \to 0}} \frac{f(x+h) - f(x)}{h} $$

### Power Rule

$$ \frac{d}{dx} x^n = n x^{n-1} $$

### Constant Rule

$$ \frac{d}{dx} c = 0 $$

### Sum and Difference Rules

$$ \frac{d}{dx} [f(x) \pm g(x)] = f'(x) \pm g'(x) $$

### Product Rule

$$ \frac{d}{dx} [f(x) g(x)] = f'(x) g(x) + f(x) g'(x) $$

### Quotient Rule

$$ \frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2} $$

### Chain Rule

$$ \frac{d}{dx} f(g(x)) = f'(g(x)) g'(x) $$

### Derivatives of Trigonometric Functions

$$ \frac{d}{dx} \sin x = \cos x $$
$$ \frac{d}{dx} \cos x = -\sin x $$
$$ \frac{d}{dx} \tan x = \sec^2 x $$
$$ \frac{d}{dx} \cot x = -\csc^2 x $$
$$ \frac{d}{dx} \sec x = \sec x \tan x $$
$$ \frac{d}{dx} \csc x = -\csc x \cot x $$

## Applications of Derivatives

### Critical Points and Extrema

- Find where $$ f'(x) = 0 $$ or is undefined.
- Use the First or Second Derivative Test.

### Mean Value Theorem

$$ f'(c) = \frac{f(b) - f(a)}{b - a}, \quad \text{for some } c \in (a, b) $$

### Related Rates

- Differentiate both sides with respect to $$ t $$ and solve for unknown rates.

### L'Hôpital's Rule

$$ \lim*{{x \to a}} \frac{f(x)}{g(x)} = \lim*{{x \to a}} \frac{f'(x)}{g'(x)} \quad \text{if } \lim*{{x \to a}} f(x) = \lim*{{x \to a}} g(x) = 0 \text{ or } \pm \infty $$

## Integration

### Indefinite Integrals

$$ \int x^n \,dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1 $$

### Basic Integral Rules

$$ \int c \,dx = cx + C $$
$$ \int e^x \,dx = e^x + C $$
$$ \int \sin x \,dx = -\cos x + C $$
$$ \int \cos x \,dx = \sin x + C $$

### Substitution Rule

$$ \int f(g(x)) g'(x) \,dx = \int f(u) \,du $$

### Definite Integrals and the Fundamental Theorem of Calculus

$$ \int_a^b f(x) \,dx = F(b) - F(a) $$

### Integration by Parts

$$ \int u \, dv = uv - \int v \, du $$

<br>
