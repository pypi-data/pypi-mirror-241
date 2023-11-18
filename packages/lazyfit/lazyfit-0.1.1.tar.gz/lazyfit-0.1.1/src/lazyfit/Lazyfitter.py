from scipy.interpolate import RBFInterpolator
import numpy as np
from distutils import errors
from lazyfit.Rbf import Rbf
from scipy.optimize import minimize_scalar

class LazyFitter:
    def __init__(self, coordinates, function_values, epsilon = 1):
        self.coordinates = np.asarray(coordinates)
        self.function_values = np.asarray(function_values)

        self.min_error = []
        self.epsilon = epsilon
        self.errors = []
        LazyFitter.Fit(self)
        self.interpolator = Rbf(self.coordinates, self.function_values, kernel = self.min_error[0], epsilon=self.epsilon)
    
    def Fit(self):
        kernels = ["linear", "cubic", "thin_plate_spline", "quintic", "gaussian", "multiquadric", "inverse_quadric"]
        for kernel in kernels:
            LazyFitter.TestKernel(self, kernel)
        min = self.errors[0]
        for error_pack in self.errors:
            if error_pack[1] < min[1]:
                min = error_pack
        self.min_error = min

    def OptimizeShape(self):
        self.interpolator = Rbf(self.coordinates, self.function_values, kernel = self.min_error[0])
        best_epsilon = minimize_scalar(self.interpolator.ShapeOpitmizer, bounds = (0.000001, self.interpolator.MinBoundingNBallFromOrigin()))
        print(best_epsilon.success)
        self.epsilon = best_epsilon.x
        self.interpolator = Rbf(self.coordinates, self.function_values, kernel = self.min_error[0], epsilon=best_epsilon.x)
        self.min_error[1] = self.interpolator.average_error

    def TestKernel(self, kernel):
        interp = Rbf(self.coordinates, self.function_values, kernel)
        self.errors.append([kernel, interp.average_error])
    
    def Interpolate(self, x):
        return self.interpolator.Interpolate(x)