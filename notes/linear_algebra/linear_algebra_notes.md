---
layout: default
title: Linear Algebra
permalink: /notes/linear_algebra/linear-algebra/
description:
---

# Linear Algebra Notes

[Home](../../../) >> [Notes](../../) >> Linear Algebra

# Table of Contents

- [Unit I: Ax = b and the Four Subspaces](#unit-1)
  - [Matrix Multiplication](#matrix-multiplication)
  - [Overview of Key Ideas](#overview-of-key-ideas)
  - [Elimination and Permutation Matrix](#elimination-permutation)
  - [Inverses](#inverses)

<br>

<H2 id="unit-1"><a href="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/" target="_blank">Unit I: Ax = b and the Four Subspaces</a></H2>

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
= \;  \boldsymbol{?}
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

**Row times column multiplication:**

If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, then $C$ is an $m \times p$ matrix. We use $c_{ij}$ to denote the entry row $i$ and column $j$ of matrix $C$:

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}
$$

**Column times row multiplication:**

$$
AB = \sum_{k=1}^{n}
\begin{bmatrix}
a_{1k} \\
\vdots \\
a_{mk}
\end{bmatrix}
\begin{bmatrix}
b_{k1} & \cdots & b_{kn}
\end{bmatrix}
$$

<br>

<H3 id="overview-of-key-ideas"><a href="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/an-overview-of-key-ideas/" target="_blank"><u>Overview of Key Ideas</u></a></H3>
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
\;
\vec{v} =
\begin{bmatrix}
0 \\
1 \\
-1
\end{bmatrix},
\;
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

We can also write vectors as:

$$
\vec{u}=\langle 1, -1, 0 \rangle, \;  \vec{v}=\langle 0, 1, -1 \rangle, \;  \vec{w}=\langle 0, 0, 1 \rangle
$$

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
\end{bmatrix}
$$

$$
= \begin{bmatrix}
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

equals the sum $x_1\mathbf{u} + x_2\mathbf{v} + x_3\mathbf{w} = \mathbf{b}$. The product of a matrix and a vector is a combination of the columns of the matrix. Note this particular matrix $A$ is a _difference matrix_ because the components of $A\mathbf{x}$ are differences of the components of that vector.

A deeper question is to start with a vector $\vec{b}$ and ask "_for what vectors $\vec{x}$ does $A\mathbf{x} = b$?_" In our example, this means solving three equations in three unknowns. Solving:

$$
\begin{bmatrix}
\begin{array}{r}
x_1 \\
x_2 - x_1 \\
x_3 - x_2
\end{array}
\end{bmatrix} =
\begin{bmatrix}
b_1 \\
b_2 \\
b_3
\end{bmatrix}
$$

Since we see that $x_1 = b_1$, then:

$$
\begin{bmatrix}
\begin{array}{r}
x_1 \\
x_2 - x_1 \\
x_3 - x_2
\end{array}
\end{bmatrix} =
\begin{bmatrix}
b_1 \\
b_2 \\
b_3
\end{bmatrix} =
\begin{pmatrix}
\begin{bmatrix}
b_1 \\
0 \\
0
\end{bmatrix} +
\begin{bmatrix}
0 \\
b_2 \\
0
\end{bmatrix} +
\begin{bmatrix}
0 \\
0 \\
b_3
\end{bmatrix}
\end{pmatrix}
$$

and in vector form:

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}=
\begin{bmatrix}
\begin{array}{r}
b_1 \\
b_1 + b_2 \\
b_1 + b_2 + b_3
\end{array}
\end{bmatrix}
$$

Note that:

- $x_1$ is just $b_1$, so the first row of the matrix will have a 1 in the first column, and 0's elsewhere. This reflects that only $b_1$ contributes to $x_1$.
- $x_2$ is $b_1 + b_2$, so the second row will have a 1 in the first and second columns, reflecting the contributions of both $b_1$ and $b_2$ to $x_2$.
- $x_3$ is $b_1 + b_2 + b_3$, so the third row will have a 1 in the first, second, and third columns, reflecting the contributions of $b_1$, $b_2$, and $b_3$ to $x_3$.

So, rewriting it for $\vec{x}$:

$$
\vec{x} =
\begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
1 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
b_1 \\
b_2 \\
b_3
\end{bmatrix}
$$

$$
\begin{array}{c|c c c}
  & b_1 & b_2 & b_3 \\
\hline
x_1 & 1 & 0 & 0 \\
x_2 & 1 & 1 & 0 \\
x_3 & 1 & 1 & 1
\end{array}
$$

<br>

<H3 id="elimination-permutation"><u>Elimination and Permutation Matrix</u></H3>

**Elimination Matrix:**

Elimination matrix (also called an elementary matrix) is a matrix that represents a single elementary row operation. It's obtained by applying that operation to the identity matrix $I$

$$
I = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Identity matrices are square matrices ($n \times n$) with ones on the diagonal and zeros everywhere else. For example, a $2 \times 2$ identity matrix is just:
$$\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$.

There are three types of elimination matrices, corresponding to the three types of elementary row operations:

1. Row Swap: Exchanges rows
2. Row Scaling: Multiplies a row by a non-zero scalar
3. Row Replacement: Adds a multiple of one row to another

For example, if we want to add -3 times the first row to the second row of some matrix, the corresponding elimination matrix would be:

$$
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Elimination matrix, $E$ are usually multiplied on the left side of the matrix you want to perform the elimination on $A$:

$$
E \times A =
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix}
$$

$$
= \begin{bmatrix}
1 & 2 & 1 \\
(3+(-3*1)) & (8+(-3*2)) & (1+(-3*1)) \\
0 & 4 & 1
\end{bmatrix}
$$

$$
= \begin{bmatrix}
1 & 2 & 1 \\
0 & 2 & -2 \\
0 & 4 & 1
\end{bmatrix}
$$

**Permutation Matrix:**

A permutation matrix is a special type of elimination matrix that only performs row swaps. It's a matrix obtained by rearranging the rows of an identity matrix.

Key properties of permutation matrices:

- They contain exactly one $1$ in each row and column, with all other entries being $0$.
- They are orthogonal matrices $P^T = p^{-1}$
- Multiplying by a permutation matrix on the right reorders _columns_ instead of _rows_. Example:

$$
P = \begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}

\text{This swaps the first and second rows.}
$$

$$
P = \begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}

\text{This reverses the order of rows of matrix } A.
$$

$$
PA =
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
= \begin{bmatrix}
7 & 8 & 9 \\
4 & 5 & 6 \\
1 & 2 & 3
\end{bmatrix}
$$

<br>

<H3 id="inverses"><a href="https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/multiplication-and-inverse-matrices/" target="_blank"><u>Inverses</u></a></H3>

If $A$ is a square matrix, the most important question you can ask about it is whether it has an inverse $A^{-1}$. If it does, then $A^{-1}A = I = AA^{-1}$ and we say that A is _invertible_ or _nonsingular_.

If $A$ is _singular_, that means $A$ does not have an inverse - and its determinant is zero. We can then find some non-zero vector $\vec{x}$ for which $A\mathbf{x} = 0$. For example:

$$
\begin{bmatrix}
1 & 3 \\
2 & 6
\end{bmatrix}
\begin{bmatrix}
3 \\
-1
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

<br>

<!-- Link to Table of Contents -->
<a href="#table-of-contents" style="display: inline-block; text-align: center; margin-top: 20px; font-size: 16px; padding: 10px; text-decoration: none; background-color: #007bff; color: white; border-radius: 5px;">
  Go to Table of Contents
</a>
