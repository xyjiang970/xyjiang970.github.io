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
  - [Derivatives of Inverse Functions](#derivatives-of-inverse-functions)
  - [Derivatives of Trigonometric Functions](#derivatives-of-trigonometric-functions)
  - [Other Derivatives to Remember](#other-derivatives-to-remember)
- [Applications of Derivatives](#applications-of-derivatives)
  - [Critical Points and Extrema](#critical-points-and-extrema)
    - [Tests for Classifying Critical Points](#tests-for-classifying-critical-points)
  - [Implicit Differentiation](#implicit-differentiation)
  - [Related Rates](#related-rates)
  - [Optimization in Machine Learning](#optimization-in-machine-learning)

<br>

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
<ul>
<li>
<b>Sum Rule:</b> The limit of a sum is the sum of the limits:

$$
\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)
$$

</li>

<li>
<b>Difference Rule:</b> The limit of a difference is the difference of the limits:

$$
\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)
$$

</li>

<li>
<b>Product Rule:</b> The limit of a product is the product of the limits:

$$
\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)
$$

</li>

<li>
<b>Quotient Rule:</b> The limit of a quotient is the quotient of the limits, as long as the denominator does not approach zero:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if } \lim_{x \to a} g(x) \neq 0
$$

</li>

</ul>

<H3 id="special-limits"><u>Special Limits</u></H3>
<ul>
<li>
<b>Sine Limit</b>: One of the most important special limits is:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

</li>

<li>
<b>Exponential Limit:</b> Another crucial limit is:

$$
\lim_{x \to 0} (1 + x)^{1/x} = e
$$

</li>
</ul>

<H3 id="lhôpitals-rule"><u>L'Hôpital's Rule</u></H3>

L'Hôpital's Rule is used to evaluate indeterminate limits of the form $\frac{0}{0}$ or $\frac{\pm \infty}{\pm \infty}$:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{if } \lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \text{ or } \pm \infty
$$

<br>

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
<ul>
<li>
<b>Sum Rule</b>: The derivative of the sum of two functions is the sum of the derivatives:

$$
\frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x)
$$

</li>

<li>
<b>Difference Rule</b>: The derivative of the difference of two functions is the difference of the derivatives:

$$
\frac{d}{dx} [f(x) - g(x)] = f'(x) - g'(x)
$$

</li>
</ul>

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

<H3 id="derivatives-of-inverse-functions"><u>Derivatives of Inverse Functions</u></H3>

$$
(f^-1)'(x) = \frac{1}{f'(f^-1(x))}
$$

The formula tells us that the derivative of the inverse function at a point is the reciprocal of the derivative of the original function at the corresponding point.

If $y = f^{-1}(x)$, then $f(y) = x$, and differentiating both sides implicitly gives:

$$
f'(y) \cdot \frac{dy}{dx} = 1
$$

Solving for $\frac{dy}{dx}$, we obtain:

$$
\frac{dy}{dx} = \frac{1}{f'(y)}
$$

Since $y = f^{-1}(x)$, we rewrite it as:

$$
\left( f^{-1} \right)' (x) = \frac{1}{f'(f^{-1}(x))}
$$

### **Example 1: Inverse of $f(x) = x^3 + 2$**

Find $\left( f^{-1} \right)' (9)$ if $f(x) = x^3 + 2$.

1. **Step 1: Solve for $f^{-1}(9)$**  
   We need to find $x$ such that:

   $$
   x^3 + 2 = 9
   $$

   $$
   x^3 = 7 \quad \Rightarrow \quad x = \sqrt[3]{7}
   $$

   So, $f^{-1}(9) = \sqrt[3]{7}$.

2. **Step 2: Compute $f'(x)$**

   $$
   f'(x) = 3x^2
   $$

   Evaluating at $x = \sqrt[3]{7}$:

   $$
   f'(\sqrt[3]{7}) = 3(\sqrt[3]{7})^2
   $$

3. **Step 3: Use the Formula**

   $$
   \left( f^{-1} \right)' (9) = \frac{1}{f'(\sqrt[3]{7})} = \frac{1}{3(\sqrt[3]{7})^2}
   $$

### **Example 2: Inverse of $f(x) = e^x$**

Find $\left( f^{-1} \right)' (3)$ if $f(x) = e^x$.

1. The inverse function is $f^{-1}(x) = \ln(x)$, so we need:

   $$
   \left( \ln x \right)' = \frac{1}{x}
   $$

2. Since $f^{-1}(3) = \ln 3$, we apply the formula:

   $$
   \left( f^{-1} \right)' (3) = \frac{1}{e^{\ln 3}} = \frac{1}{3}
   $$

### **Example 3: Inverse of $f(x) = \sin x$**

Find $\frac{d}{dx} \left[ \sin^{-1} (x) \right]$.

1. Since $y = \sin^{-1} (x)$, we have:

   $$
   \sin y = x
   $$

2. Differentiating both sides implicitly:

   $$
   \cos y \cdot \frac{dy}{dx} = 1
   $$

3. Solving for $\frac{dy}{dx}$:

   $$
   \frac{dy}{dx} = \frac{1}{\cos y}
   $$

4. Using $cos y = \sqrt{1 - x^2}$ (from the Pythagorean identity),

   $$
   \frac{d}{dx} \left( \sin^{-1} x \right) = \frac{1}{\sqrt{1 - x^2}}
   $$

Similarly,

$$
\frac{d}{dx} \left( \cos^{-1} x \right) = -\frac{1}{\sqrt{1 - x^2}}
$$

$$
\frac{d}{dx} \left( \tan^{-1} x \right) = \frac{1}{1 + x^2}
$$

<H3 id="derivatives-of-trigonometric-functions"><u>Derivatives of Trigonometric Functions</u></H3>

$$
\frac{d}{dx} \sin(x) = \cos(x)
$$

$$
\frac{d}{dx} \cos(x) = -\sin(x)
$$

$$
\frac{d}{dx} \tan(x) = \sec^2(x), \quad \text{Note that: }tan(x) = \frac{sin(x)}{cos(x)}
$$

Cosecant ($csc(x) = \frac{1}{sin(x)}$):

$$
\frac{d}{dx} \csc(x) = -\csc(x) \cot(x)
$$

Secant ($sec(x) = \frac{1}{cos(x)}$):

$$
\frac{d}{dx} \sec(x) = \sec(x) \tan(x)
$$

Cotangent ($cot(x) = \frac{1}{tan(x)} = \frac{cos(x)}{sin(x)}$):

$$
\frac{d}{dx} \cot(x) = -\csc^2(x)
$$

Additionally, here are the derivatives of **inverse** trigonometric functions:

$$
\frac{d}{dx} \arcsin(x) = \frac{1}{\sqrt{1 - x^2}}
$$

$$
\frac{d}{dx} \arccos(x) = -\frac{1}{\sqrt{1 - x^2}}
$$

$$
\frac{d}{dx} \arctan(x) = \frac{1}{1 + x^2}
$$

Arc cosecant (arccsc):
Where $csc(x) = \frac{1}{sin(x)}$

$$
\frac{d}{dx} \csc^{-1}(x) = -\frac{1}{|x|\sqrt{x^2 - 1}}
$$

Arc secant (arcsec):
Where $sec(x) = \frac{1}{cos(x)}$

$$
\frac{d}{dx} \sec^{-1}(x) = \frac{1}{|x|\sqrt{x^2 - 1}}
$$

Arc cotangent (arccot):
Where $cot(x) = \frac{1}{tan(x)} = \frac{cos(x)}{sin(x)}$

$$
\frac{d}{dx} \cot^{-1}(x) = -\frac{1}{1 + x^2}
$$

<H3 id="other-derivatives-to-remember"><u>Other Derivatives to Remember</u></H3>

#### Derivatives of Exponential Functions:

$$
\frac{d}{dx}e^x = e^x
$$

$$
\frac{d}{dx} a^x = a^x \ln(a), \; \text{where } a \text{ is a constant > 0}
$$

#### Derivatives of Logarithmic Functions:

$$
\frac{d}{dx}ln(x) = \frac{1}{x}
$$

$$
\frac{d}{dx}\log_a x = \frac{1}{x \ln(a)}
$$

<br>

<H2 id="applications-of-derivatives"> Applications of Derivatives </H2>

<H3 id="critical-points-and-extrema"><u>Critical Points and Extrema</u></H3>

Critical points occur where the derivative is zero **or** undefined.

A critical point of a function $f(x)$ occurs at $x = c$ if either:

- $f'(c) = 0$ (the derivative equals zero), or
- $f'(c)$ is undefined (the derivative doesn't exist at that point)

Critical points are crucial because they are candidates for **local** extrema (maxima and minima) of the function.

Types of Critical Points:

- Local Maximum: A point where $f(c) ≥ f(x)$ for all $x$ in some open interval containing $c$.
- Local Minimum: A point where $f(c) ≤ f(x)$ for all $x$ in some open interval containing $c$.
- Inflection Point: A point where the concavity of the function changes (though not all inflection points are critical points).
- Saddle Point: A critical point that is neither a local maximum nor a local minimum.

<!-- #### Tests for Classifying Critical Points: -->
<H4 id="tests-for-classifying-critical-points"><u>Tests for Classifying Critical Points:</u></H4>

- The <u>First Derivative Test</u>:

  1. Find all critical points by solving $f'(x) = 0$ or identifying where $f'(x)$ is undefined.
  2. Examine the sign of $f'(x)$ on intervals before and after each critical point.
  3. Classify each critical point based on the sign changes:
     - If $f'(x)$ changes from positive to negative at $x = c$, then $f(c)$ is a local maximum.
     - If $f'(x)$ changes from negative to positive at $x = c$, then $f(c)$ is a local minimum.
     - If $f'(x)$ doesn't change sign at $x = c$ (e.g., positive on both sides or negative on both sides), then $x = c$ is not an extremum (possibly a saddle point).

  Example: For $f(x) = x^3 - 3x + 1$, we have $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$. Critical points appear at $x=-1$ and $x=1$.

  - For $x < -1$: $f'(x) < 0$ (derivative is negative)
  - For $-1 < x < 1$: $f'(x) > 0$ (derivative is positive)
  - For $x > 1$: $f'(x) < 0$ (derivative is negative)

  Therefore:

  - $x = -1$ is a local minimum (derivative changes from negative to positive)
  - $x = 1$ is a local maximum (derivative changes from positive to negative)

<br>

- The <u>Second Derivative Test</u>: The Second Derivative Test is often more convenient when the second derivative is easy to compute.

  1. Find critical points where $f'(c) = 0$.
  2. Evaluate the second derivative $f″(c)$ at each critical point:

  - If $f″(c) > 0$, then $f(c)$ is a local minimum (function is concave up).
  - If $f″(c) < 0$, then $f(c)$ is a local maximum (function is concave down).
  - If $f″(c) = 0$, the test is inconclusive (use the First Derivative Test instead).

  Example: For $f(x) = x^3 - 3x + 1$, we have:

  - $f'(x) = 3x^2 - 3$
  - $f″(x) = 6x$

  At the critical points:

  - At $x = -1$: $f″(-1) = 6(-1) = -6 < 0$, so this is a local maximum.
  - At $x = 1$: $f″(1) = 6(1) = 6 > 0$, so this is a local minimum.

**Inflection Points:**
An inflection point occurs where the concavity of the function changes:

- Concave up: $f″(x) > 0$
- Concave down: $f″(x) < 0$

To find inflection points:

1. Compute $f″(x)$
2. Find the values of $x$ where $f″(x) = 0$ or $f″(x)$ is undefined
3. Check if the sign of $f″(x)$ changes at these points

Example:
For $f(x) = x^3$, we have:

- $f'(x) = 3x^2$
- $f″(x) = 6x$

Setting $f″(x) = 0$, we get $x = 0$.
Checking the sign of $f″(x)$:

- For $x < 0$: $f″(x) < 0$ (concave down)
- For $x > 0$: $f″(x) > 0$ (concave up)

Therefore, $(0, 0)$ is an inflection point where the concavity changes.

**Global Extrema on Closed Intervals:**
To find the absolute (global) maximum and minimum values of a continuous function $f(x)$ on a closed interval $[a, b]$:

1. Find all critical points of $f(x)$ within the interval $(a, b)$.
2. Evaluate $f(x)$ at each critical point and at the endpoints $a$ and $b$.
3. The largest of these values is the absolute maximum, and the smallest is the absolute minimum.

Example: Fine the global extrema of $f(x) = x^3 - 3x + 1$ on $[-2, 2]$.
Critical points: $x = -1$ and $x = 1$.

Evaluate:

- $f(-2) = (-2)^3 - 3(-2) + 1 = -8 + 6 + 1 = -1$
- $f(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3$
- $f(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$
- $f(2) = (2)^3 - 3(2) + 1 = 8 - 6 + 1 = 3$

Therefore:

- Global maximum: $f(-1) = f(2) = 3$ (occurs at two points)
- Global minimum: $f(1) = f(-2) = -1$ (occurs at two points)

<H3 id="implicit-differentiation"><u>Implicit Differentiation</u></H3>

Implicit differentiation is a technique used to find the derivative of a function that is not explicitly solved for one variable. Instead of having $y = f(x)$, we have an equation relating $x$ and $y$, such as $F(x,y) = 0$.

Implicit differentiation is particularly useful for complicated relationships between variables and for curves that cannot be easily expressed as explicit functions.

Sometimes, solving explicitly for one variable is impossible of very difficult. Implicit differentiation lets us find derivatives **without solving explicitly**.

For example, consider the equation: $x^3 + y^3 = 6xy$. Solving explicitly for $y$ in terms of $x$ is complicated. Instead we can differentiate both sides to get $\frac{dy}{dx}$ directly.

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

**Key Takeaway:**

- Explicit formulas are useful for direct calculations, evaluations, and visualization.
- **When Do we WANT an Explicit Formula:**

  - Direct Computation:
    - If we have $z=f(x,y)$, we can directly compute derivatives like $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$.
    - Example: If $z=\sqrt{1 - x^2 - y^2}$, we can easily differentiate it without needing implicit differentiation.
  - Plugging into Other Equations:
    - An explicit formula makes it easier to substitute and analyze function values.
  - Graphing & Visualization:
    - If we explicitly express a variable, we can plot it as a function of others.
  - Solving for Specific Values: - If we want to evaluate a function at a specific point, having an explicit equation makes it easier.

<br>

- Implicit differentiation is a powerful alternative when explicit solutions are too hard or unnecessary.
- **When Do we NOT Need an Explicit Formula:**
  - When Working with Level Curves or Surfaces
    - If we only care about relationships (like gradients or tangent planes), we don't need an explicit formula.
  - In Multi-variable Calculus
    - When defining constraints (e.g. $x^2 + y^2 + z^2 = 1$), explicit formulas are often unnecessary.
  - In Optimization (Lagrange Multipliers)
    - We use constraints implicitly instead of solving for one variable explicitly.

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

<H3 id="optimization-in-machine-learning"><u>Optimization in Machine Learning</u></H3>
Machine learning is a practical application of optimization techniques. While advanced machine learning involves complex mathematics, the core principles connect directly to the calculus concepts we've already covered.

**The Basic Idea**
In machine learning, we try to find the "best" model that explains our data. This involves:

1. Defining a cost function (or "loss function") that measures how wrong our model is
2. Finding the model parameters that minimize this cost function

This is fundamentally an optimization problem!

**Simple Example: Linear Regression**
Consider a simple linear model: $y = mx + b$, where we want to find the values of $m$ and $b$ that best fit our data points.

1. We define our cost function as the sum of squared errors:

   $$
   J(m,b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - (mx_i + b))^2
   $$

2. To find the optimal $m$ and $b$, we take partial derivatives and set them to zero:

   $$
   \frac{\partial J}{\partial m} = 0
   $$

   $$
   \frac{\partial J}{\partial b} = 0
   $$

3. These equations can be solved directly to find the optimal line.

**Gradient Descent: When Direct Solutions Aren't Practical**

For more complex models, we can't always solve directly for the optimum. Instead, we use an iterative approach called gradient descent:

1. Start with an initial guess for the parameters.
2. Calculate the gradient (direction of steepest increase).
3. Take a small step in the opposite direction of the gradient.
4. Repeat until we reach a minimum.

The gradient (derivative of the loss function) tells you the direction to move in order to reduce the loss. The critical points in machine learning correspond to the **global minimum** (best solution) or **local minima** of the loss function. The gradient is essentially the slope of the function at a point, guiding how much the parameters need to be adjusted.

Mathematically, we update parameters using:
$$\theta_{new} = \theta_{old} - \alpha \frac{\partial J}{\partial \theta}$$

Where $\alpha$ is a small number called the "learning rate."

The above describes the update rule for gradient descent (where $J$ is the loss function).

1. Parameters ($\theta$):

   - $\theta_{old}$: represents the current values of the model parameters (weights or coefficients) before the update.
   - $\theta_{new}$: updated value of the parameters after one step of gradient descent.
   - In the context of ML, these parameters could be the weights in a neural network or the coefficients in a regression model.)

2. Gradient of the Loss Function ($\frac{\partial J}{\partial \theta}$):

   - $\frac{\partial J}{\partial \theta}$ is the gradient of the loss function $J(\theta)$ with respect to the parameters $\theta$.
   - This gradient tells you the direction in which the loss function increases the most (direction of steepest ascent).
   - To minimize the loss, we want to move in the **opposite** direction of the gradient (steepest descent).

3. Learning Rate ($\alpha$):

   - $\alpha$: small positive number called the learning rate.
   - Determines the step size we take in the direction opposite to the gradient.
   - If $\alpha$ is too large, we might overshoot the optimal values and miss the minimum.
   - If $\alpha$ is too small, the optimization process can become very slow.

**Convexity vs. Non-Convexity**

In most machine learning algorithms, the goal is to find a convex function (like a convex loss function) because convex functions guarantee that the critical point we find is a global minimum, not just a local one.

- For convex loss functions, gradient descent is likely to converge to the global minimum.
- For non-convex loss functions (like neural networks), we may end up stuck in a local minima or saddle points, and optimization becomes more challenging.

**Constraints in Optimization (Lagrange Multipliers)**

In certain optimization problems, we have constraints. For example, you might want to minimize a cost function subject to a constraint on one or more variables. The method for this in calculus is often done using Lagrange multipliers, which introduce additional variables to incorporate the constraints into the optimization process.

- In ML, regularization methods like L1 (Lasso) and L2 (Ridge) regularization are examples of optimization with constraints. The regularization terms prevent overfitting by penalizing the size of the coefficients (weights) of the model.
- Support Vector Machines (SVM) also use constraints in optimization, where the goal is to find the hyperplane that maximizes the margin between classes, subject to the constrains of correctly classifying the data points.

<u>Connection to Calculus Concepts</u>

Machine learning optimization connects to calculus in several ways:

- **Derivatives** tell us the direction to adjust our parameters
- **Critical points** are potential solutions to our optimization problems
- **Local vs. global minima** affect whether we find the best possible model
- **Multivariable calculus** extends these ideas to functions with many parameters

Even the most advanced machine learning algorithms (like neural networks) rely on these fundamental calculus principles, just applied to functions with thousands or millions of parameters instead of just one or two.

<br>

<!-- Link to Table of Contents -->
<a href="#table-of-contents" style="display: inline-block; text-align: center; margin-top: 20px; font-size: 16px; padding: 10px; text-decoration: none; background-color: #007bff; color: white; border-radius: 5px;">
  Go to Table of Contents
</a>
