---
layout: default
title: Linear Algebra
permalink: /notes/linear_algebra/linear-algebra/
description:
---

# Linear Algebra Notes

[Home](../../../) >> [Notes](../../) >> Linear Algebra

# Table of Contents

- [Scalars, Vectors, Matrices](#scalars-vectors-matrices)
  - [Matrix Multiplication](#matrix-multiplication)
- [Overview of Key Ideas](#overview-of-key-ideas)

<br>

<H2 id="scalars-vectors-matrices"><a href="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/" target="_blank">Scalars, Vectors, Matrices</a></H2>
<a href="https://www.youtube.com/watch?v=My5w4MXWBew" target="_blank">Geometry of Linear Algebra Recitation Video</a>

The fundamental problem of linear algebra is to solve $n$ linear equations in $n$ unknowns; for example:

$$
2x - y = 0
$$

$$
-x + 2y = 3
$$

The system above is two dimensional ($n = 2$). By adding a third variable $z$ we could expand it into three dimensions.

**Column Picture:**

In the column picture we rewrite the system of linear equations as a single equation by turning the coefficients in the columns of the systems into vectors:

$$
x
\begin{bmatrix}
2 \\
-1
\end{bmatrix}
+
y
\begin{bmatrix}
-1 \\
2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

Given two vectors $\vec{c}$ and $\vec{d}$ and scalars $x$ and $y$, the sum $x\vec{c} + y\vec{d}$ is called a _linear combination_. Geometrically, we want to find numbers $x$ and $y$ so that $x$ copies of vector $$\begin{bmatrix} 2 \\ -1 \end{bmatrix}$$ added to $y$ copies of vector $$\begin{bmatrix} -1 \\ 2 \end{bmatrix}$$ equal vector $$\begin{bmatrix} 0 \\ 3 \end{bmatrix}$$.

**Matrix Picture:**

We write the system of equations:

$$
2x - y = 0
$$

$$
-x + 2y = 3
$$

as a single equation by using matrices and vectors:

$$
\begin{bmatrix}
2 & -1 \\
-1 & -2
\end{bmatrix}
+
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

The matrix $$A=\begin{bmatrix}2 & -1 \\ -1 & -2 \end{bmatrix}$$ is called the _coefficient matrix_. The vector $$\vec{x}=\begin{bmatrix} x \\ y \end{bmatrix}$$ is the vector of unknowns. The values on the right hand side of the equation form the vector $\vec{b}$:

$$
A\mathbf{x} = \mathbf{b}
$$

<H3 id="matrix-multiplication"><u>Matrix Multiplication</u></H3>
How do we multiply a matrix $A$ by a vector $\vec{x}$?

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2
\end{bmatrix}
= \boldsymbol{?}
$$

One method is to think of the entries of $\vec{x}$ as the coefficients of a linear combination of the column vectors of the matrix:

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2
\end{bmatrix}
=
1
\begin{bmatrix}
2 \\
1
\end{bmatrix}
+
2
\begin{bmatrix}
5 \\
3
\end{bmatrix}
=
\begin{bmatrix}
12 \\
7
\end{bmatrix}
$$

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2
\end{bmatrix}
=
\begin{bmatrix}
2 \\
1
\end{bmatrix}
+
\begin{bmatrix}
5 \\
3
\end{bmatrix}
+
\begin{bmatrix}
5 \\
3
\end{bmatrix}
=
\begin{bmatrix}
12 \\
7
\end{bmatrix}
$$

This technique shows that $A\vec{x}$ is a linear combination of the columns of $A$. You may also calculate the product $A\vec{x}$ by taking the dot product of each row of $A$ with the vector $\vec{x}$:

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2
\end{bmatrix}
=
\begin{bmatrix}
2 \cdot 1 + 5 \cdot 2 \\
1 \cdot 1 + 3 \cdot 2
\end{bmatrix}
=
\begin{bmatrix}
12 \\
7
\end{bmatrix}
$$

<br>

<H2 id="overview-of-key-ideas"><a href="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/an-overview-of-key-ideas/" target="_blank">Overview of Key Ideas</a></H2>
Linear algebra progresses from vectors to matrices to subspaces.

**Vectors:**

Given vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ we can form the linear combination $x_1\mathbf{u} + x_2\mathbf{v} + x_3\mathbf{w} = \mathbf{b}$. An example in $\mathbb{R}^3$ ($\mathbb{R}^3$ refers to 3-dimensional Euclidean space, which is the set of all ordered triples of real numbers commonly represented by three coordinates $(x, y, z)$, with each $x$, $y$, and $z$ being real numbers) would be:

$$
\vec{u} =
\begin{bmatrix}
1 \\
-1 \\
0
\end{bmatrix},
\vec{v} =
\begin{bmatrix}
0 \\
1 \\
-1
\end{bmatrix},
\vec{w} =
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$

Meaning any vector $\vec{b}$ in $\mathbb{R}^3$ can be formed using a linear combination of $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ must satisfy:

$$
x_1
\begin{bmatrix}
1 \\
-1 \\
0
\end{bmatrix}
+
x_2
\begin{bmatrix}
0 \\
1 \\
-1
\end{bmatrix}
+
x_3
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\
b_2 \\
b_3
\end{bmatrix}
$$

The collection of all multiples of $\mathbf{u}$ forms a line through the origin. The collection of all multiples of $\mathbf{v}$ forms another line. The collection of all combinations of $\mathbf{u}$ and $\mathbf{v}$ forms a plane. Taking all combinations of some vectors creates a _subspace_. We could continue like this, or we can use a matrix to add in all multiples of $\mathbf{w}$.

**Matrices:**

Create a matrix $A$ with vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ in its columns:

$$
A =
\begin{bmatrix}
1 & 0 & 0 \\
-1 & 1 & 0 \\
0 & -1 & 1
\end{bmatrix}
$$

The product:

$$
A\mathbf{x} =
\begin{bmatrix}
1 & 0 & 0 \\
-1 & 1 & 0 \\
0 & -1 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix} =
\begin{bmatrix}
(1 \cdot x_1) + (0 \cdot x_2) + (0 \cdot x_3) \\
(-1 \cdot x_1) + (1 \cdot x_2) + (0 \cdot x_3) \\
(0 \cdot x_3) + (-1 \cdot x_2) + (1 \cdot x_3)
\end{bmatrix}
$$

$$
= \begin{bmatrix}
\begin{array}{r}
x_1 \\
-x_1 + x_2 \\
-x_2 + x_3
\end{array}
\end{bmatrix} =
\begin{bmatrix}
\begin{array}{r}
x_1 \\
x_2 - x_1 \\
x_3 - x_2
\end{array}
\end{bmatrix}
$$

equals the sum $x_1\mathbf{u} + x_2\mathbf{v} + x_3\mathbf{w} = \mathbf{b}$. The product of a matrix and a vector is a combination of the columns of the matrix.

<br>

<!-- Link to Table of Contents -->
<a href="#table-of-contents" style="display: inline-block; text-align: center; margin-top: 20px; font-size: 16px; padding: 10px; text-decoration: none; background-color: #007bff; color: white; border-radius: 5px;">
  Go to Table of Contents
</a>
