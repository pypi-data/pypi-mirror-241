<!---
Best read with a KaTex equiped markdown renderer.
In vs-code Markdown Preview Enhanced is a good extension.
-->

 # Lazyfit
This is the lazy fit python package. This package provides classes and methods that may be used to build radial basis function interpolants and optimize their behaviors.

Rbf interpolation is a mesh-free interpolation technique in which a set of  radial basis function are used as the basis for a Haar space. The interpolant takes the form:

$$
L(p) = \sum_{i = 0}^n \lambda_i \varphi(||p - p_i ||)
$$

It is governed by the interpolation condition:

$$
F_j = \sum_{i = 0}^n \lambda_i \varphi(||p_i - p_j||)
$$

Where $p_i$ and $p_j$ are points in the input data and $F_j$ is the known  function value associated with $p_j$.

# Classes
## LazyFitter
The lazyfitter is the primary class of the package. It aims to provide a simple interface that builds and optimizes the interpolation behind the scene.
### Constructor
LazyFitter(coordinates, function_values, epsilon  =  1)
Parameters:
- coordinates: array_like
	>An array_like that contains the coordinates to build the interpolant. For m data points in $\mathbb{R^n}$ the shape is (m, n), this includes data on $\mathbb{R}$ which has shape (m, 1) not just (m).
- function_values: array_like
	>An array_like that contains the function values associated with the coordinates index aligned. For m data points, the shape is (m).
- epsilon: float
	> The shape parameter of the interpolant, default is 1.

### Member Variables:
- coordinates: array_like
	>An array_like that contains the coordinates to build the interpolant. For m data points in $\mathbb{R^n}$ the shape is (m, n), this includes data on $\mathbb{R}$ which has shape (m, 1) not just (m).
- function_values: array_like
	>An array_like that contains the function values associated with the coordinates index aligned. For m data points, the shape is (m).

- epsilon: float
	> Same as the epsilon in object creation, may change with optimization.
- min_error: list
	>Two entries, the first is the name of the minimum error basis function and the second is the RMS leave-one-out cross-validation error of that interpolant.
		
### Member Functions:
- OptimizeShape()
	> Optimizes the current basis function interpolant by shape parameter. Uses a bounded Brent's algorithm for the optimization the error estimator as a function of shape parameter.
- Interpolate(x): array_like
	> returns the evaluation of the interpolant at the point x.

## Rbf
 
### Constructor
Rbf(coordinates, function_values, kernel, epsilon  =  1, norm_weights = None)
- coordinates: array_like
	>An array_like that contains the coordinates to build the interpolant. For m data points in $\mathbb{R^n}$ the shape is (m, n), this includes data on $\mathbb{R}$ which has shape (m, 1) not just (m).
- function_values: array_like
	>An array_like that contains the function values associated with the coordinates index aligned. For m data points, the shape is (m).
- kernel
	- One of:
		- "linear" : $\varphi(r) = r$
		- "thin_plate_spline" : $\varphi(r) = r^2 log(r)$
		- "cubic" : $\varphi(r) = r^3$
		- "quintic" : $\varphi(r) = r^5$
		- "gaussian" : $\varphi(r) = e^{-(\epsilon r)^2}$
		- "multiquadric" : $\varphi(r) = -\sqrt{1 + (\epsilon r)^2}$
		- "inverse_quadric" : $\varphi(r) = \frac{1}{1 + (\epsilon r)^2}$
- epsilon: float
	> The shape parameter of the interpolant, default is 1.
- norm_weights: array_like
	> An array of the weights to be given to the various dimensions to the standard Euclidean norm. This produces an augmented Euclidean norm that is "equivalent" in the mathematical sense regarding normed spaces. Here norm_weights represents $a_i$ in the norm equation $||p_i - p_j|| = \sqrt{\sum_{k = 0}^n a_i (p_{i, k} - p_{j, k})^2}$ for $p_i, p_j$ on $\mathbb{R}^n$. If that were a standard Euclidean norm then $a_i$ would be all 1's.
	### Member Variables:
- coordinates: array_like
	>An array_like that contains the coordinates to build the interpolant. For m data points in $\mathbb{R^n}$ the shape is (m, n), this includes data on $\mathbb{R}$ which has shape (m, 1) not just (m).
- function_values: array_like
	>An array_like that contains the function values associated with the coordinates index aligned. For m data points, the shape is (m).
- n : int
	>The number of cooridnates/function_values given on construction.
- kernel
	- One of:
		- "linear" : $\varphi(r) = r$
		- "thin_plate_spline" : $\varphi(r) = r^2 log(r)$
		- "cubic" : $\varphi(r) = r^3$
		- "quintic" : $\varphi(r) = r^5$
		- "gaussian" : $\varphi(r) = e^{-(\epsilon r)^2}$
		- "multiquadric" : $\varphi(r) = -\sqrt{1 + (\epsilon r)^2}$
		- "inverse_quadric" : $\varphi(r) = \frac{1}{1 + (\epsilon r)^2}$
- epsilon: float
	> The shape parameter of the interpolant, default is 1. Changing this after construction will not rebuild the interpolant.
- weights : array
	>The coefficients of the interpolant's basis functions.
- is_singular: boolean
	> describes whether or not the basis function matrix $\Phi_{ij} = \varphi(||p_i - p_j||)$ is singular.
- average_error:
	>The RMS leave-one-out error of the interpolant, calculated on construction of the object. Calculation runs in $O(n^3)$ time.

### Member Functions:
- Interpolate(point):
	>Evaluates the interpolant at point.

# Dependancies
This Library has both scipy and numpy dependancies:
- numpy: 1.23.5
- scipy: 1.10.1