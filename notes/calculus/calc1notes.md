---
layout: default
title: Calculus 1 Notes
permalink: /notes/calculus/calc1notes/
description:
---

# Calculus 1 Notes

[Home](../../../) >> [Notes](../../) >> Calculus 1 Notes

# Table of Contents

- [Limits](#limits)
  - [Constant Rule for Limits](#constant-rule-for-limits)
  - [Limit of a Linear Function](#limit-of-a-linear-function)
  - [Sum, Difference, Product, and Quotient Rules](#sum-difference-product-and-quotient-rules)
  - [Special Limits](#special-limits)
  - [L'Hôpital's Rule](#lhôpitals-rule)
- [Derivatives](#derivatives)
  - [Definition of a Derivative](#definition-of-a-derivative)
  - [Mean Value Theorem](#mean-value-theorem)
  - [Power Rule](#power-rule)
  - [Constant Rule](#constant-rule)
  - [Sum and Difference Rules](#sum-and-difference-rules)
  - [Product Rule](#product-rule)
  - [Quotient Rule](#quotient-rule)
  - [Chain Rule](#chain-rule)
  - [Derivatives of Trigonometric Functions](#derivatives-of-trigonometric-functions)
- [Applications of Derivatives](#applications-of-derivatives)
  - [Critical Points and Extrema](#critical-points-and-extrema)
  - [Related Rates](#related-rates)
  - [Implicit Differentiation](#implicit-differentiation)

<H2 id="limits"> Limits </H2>

<H3 id="constant-rule-for-limits"><u>Constant Rule for Limits</u></H3>

The constant rule states that the limit of a constant is the constant itself. If $c$ is a constant, then:

$$
\lim_{x \to a} c = c
$$

<H3 id="limit-of-a-linear-function"><u>Limit of a Linear Function</u></H3>

For a linear function $f(x) = x$, the limit is straightforward:

$$
\lim_{x \to a} x = a
$$

<H3 id="sum-difference-product-and-quotient-rules"><u>Sum, Difference, Product, and Quotient Rules</u></H3>

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

<H3 id="special-limits"><u>Special Limits</u></H3>

1. **Sine Limit**: One of the most important special limits is:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

2. **Exponential Limit**: Another crucial limit is:

$$
\lim_{x \to 0} (1 + x)^{1/x} = e
$$

<H3 id="lhôpitals-rule"><u>L'Hôpital's Rule</u></H3>

L'Hôpital's Rule is used to evaluate indeterminate limits of the form $\frac{0}{0}$ or $\frac{\pm \infty}{\pm \infty}$:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{if } \lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \text{ or } \pm \infty
$$

<H2 id="derivatives"> Derivatives </H2>

<H3 id="definition-of-a-derivative"><u>Definition of a Derivative</u></H3>

The derivative of a function at a point is defined as the limit of the difference quotient:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

<H3 id="mean-value-theorem"><u>Mean Value Theorem</u></H3>

The Mean Value Theorem states that there exists at least one point $c$ in the interval $(a, b)$ such that:

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$

<H3 id="power-rule"><u>Power Rule</u></H3>

The power rule is used to differentiate functions of the form $f(x) = x^n$, where $n$ is any real number:

$$
\frac{d}{dx} x^n = n x^{n-1}
$$

<H3 id="constant-rule"><u>Constant Rule</u></H3>

The derivative of a constant is always zero:

$$
\frac{d}{dx} c = 0
$$

<H3 id="sum-and-difference-rules"><u>Sum and Difference Rules</u></H3>

1. **Sum Rule**: The derivative of the sum of two functions is the sum of the derivatives:

$$
\frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x)
$$

2. **Difference Rule**: The derivative of the difference of two functions is the difference of the derivatives:

$$
\frac{d}{dx} [f(x) - g(x)] = f'(x) - g'(x)
$$

<H3 id="product-rule"><u>Product Rule</u></H3>

The derivative of the product of two functions is given by the product rule:

$$
\frac{d}{dx} [f(x) g(x)] = f'(x) g(x) + f(x) g'(x)
$$

<H3 id="quotient-rule"><u>Quotient Rule</u></H3>

The derivative of a quotient of two functions is given by the quotient rule:

$$
\frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}
$$

<H3 id="chain-rule"><u>Chain Rule</u></H3>

The chain rule is used to differentiate composite functions:

$$
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
$$

<H3 id="derivatives-of-trigonometric-functions"><u>Derivatives of Trigonometric Functions</u></H3>

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

<H2 id="applications-of-derivatives"> Applications of Derivatives </H2>

<H3 id="critical-points-and-extrema"><u>Critical Points and Extrema</u></H3>

Critical points occur where the derivative is zero or undefined. These points are used to find local maxima and minima, which can be determined using:

- The **First Derivative Test**: Analyze the sign of the derivative before and after the critical point.
- The **Second Derivative Test**: If $f''(x) > 0$, the function is concave up, and if $f''(x) < 0$, the function is concave down at the critical point.

<H3 id="related-rates"><u>Related Rates</u></H3>

Related rates problems involve determining how the rate of change of one quantity is related to the rates of change of other quantities. These problems typically require implicit differentiation with respect to time.

The general approach for solving related rates problems:

1. Identify all variables and their rates of change
2. Find an equation that relates the variables
3. Implicitly differentiate the entire equation with respect to time
4. Substitute known values and solve for the unknown rate

For example, if we have a relationship between variables $x$ and $y$ such as:

$$
x^2 + y^2 = 25
$$

To find how $y$ changes when $x$ changes at a certain rate, we implicitly differentiate with respect to time $t$:

$$
\frac{d}{dt}(x^2 + y^2) = \frac{d}{dt}(25)
$$

$$
2x \cdot \frac{dx}{dt} + 2y \cdot \frac{dy}{dt} = 0
$$

Solving for $\frac{dy}{dt}$:

$$
\frac{dy}{dt} = -\frac{x}{y} \cdot \frac{dx}{dt}
$$

Another common example involves related rates with volume and radius:

$$
V = \frac{4}{3}\pi r^3
$$

Differentiating with respect to time:

$$
\frac{dV}{dt} = 4\pi r^2 \cdot \frac{dr}{dt}
$$

This shows that if we know how quickly the radius is changing ($\frac{dr}{dt}$), we can find how quickly the volume is changing ($\frac{dV}{dt}$), and vice versa.

<H3 id="implicit-differentiation"><u>Implicit Differentiation</u></H3>

Implicit differentiation is a technique used to find the derivative of a function that is not explicitly solved for one variable. Instead of having $y = f(x)$, we have an equation relating $x$ and $y$, such as $F(x,y) = 0$.

To perform implicit differentiation:

1. Take the derivative of each term with respect to $x$
2. Remember that when differentiating terms containing $y$, you must apply the chain rule by multiplying by $\frac{dy}{dx}$
3. Solve for $\frac{dy}{dx}$

**Example 1: Circle Equation**

For a circle with equation:

$$
x^2 + y^2 = 25
$$

Differentiate both sides with respect to $x$:

$$
\frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25)
$$

$$
2x + 2y \cdot \frac{dy}{dx} = 0
$$

Solving for $\frac{dy}{dx}$:

$$
\frac{dy}{dx} = -\frac{x}{y}
$$

This gives us the slope of the tangent line at any point $(x,y)$ on the circle.

**Example 2: Ellipse Equation**

For an ellipse with equation:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
$$

Differentiate both sides with respect to $x$:

$$
\frac{d}{dx}\left(\frac{x^2}{a^2} + \frac{y^2}{b^2}\right) = \frac{d}{dx}(1)
$$

$$
\frac{2x}{a^2} + \frac{2y}{b^2} \cdot \frac{dy}{dx} = 0
$$

Solving for $\frac{dy}{dx}$:

$$
\frac{dy}{dx} = -\frac{b^2 \cdot x}{a^2 \cdot y}
$$

**Example 3: General Power Relationship**

Consider the equation:

$$
x^3 + y^3 = 6xy
$$

Differentiate both sides with respect to $x$:

$$
\frac{d}{dx}(x^3 + y^3) = \frac{d}{dx}(6xy)
$$

$$
3x^2 + 3y^2 \cdot \frac{dy}{dx} = 6y + 6x \cdot \frac{dy}{dx}
$$

Rearranging to solve for $\frac{dy}{dx}$:

$$
3y^2 \cdot \frac{dy}{dx} - 6x \cdot \frac{dy}{dx} = 6y - 3x^2
$$

$$
\frac{dy}{dx}(3y^2 - 6x) = 6y - 3x^2
$$

$$
\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x}
$$

**Example 4: Logarithmic Relationship**

For the equation:

$$
xy + \ln(y) = e^x
$$

Differentiate both sides with respect to $x$:

$$
\frac{d}{dx}(xy + \ln(y)) = \frac{d}{dx}(e^x)
$$

$$
y + x \cdot \frac{dy}{dx} + \frac{1}{y} \cdot \frac{dy}{dx} = e^x
$$

Rearranging to solve for $\frac{dy}{dx}$:

$$
x \cdot \frac{dy}{dx} + \frac{1}{y} \cdot \frac{dy}{dx} = e^x - y
$$

$$
\frac{dy}{dx}\left(x + \frac{1}{y}\right) = e^x - y
$$

$$
\frac{dy}{dx} = \frac{e^x - y}{x + \frac{1}{y}}
$$

Implicit differentiation is particularly useful for complicated relationships between variables and for curves that cannot be easily expressed as explicit functions.

<br>

<!-- Link to Table of Contents -->
<a href="#table-of-contents" style="display: inline-block; text-align: center; margin-top: 20px; font-size: 16px; padding: 10px; text-decoration: none; background-color: #007bff; color: white; border-radius: 5px;">
  Go to Table of Contents
</a>
