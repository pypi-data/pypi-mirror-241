import numpy as np



class Rbf:
    def __init__(self, coordinates, function_values, kernel, epsilon = 1, norm_weights = None):
        self.coordinates = np.asarray(coordinates)
        self.function_values = np.asarray(function_values)

        self.n = len(coordinates)
        self.kernel = kernel
        self.epsilon = epsilon
        self.weights = np.zeros(len(coordinates))

        if norm_weights != None and len(norm_weights) == len(coordinates[0]):
            self.__norm_weights = norm_weights
        elif norm_weights != None and len(norm_weights) != len(coordinates[0]):
            print("Improper norm_weights shape, defaulted to Euclidean norm.")
            self.__norm_weights = np.full((len(self.coordinates[0])), 1)
        else:
            self.__norm_weights = np.full((len(self.coordinates[0])), 1)

        self.coefficient_matrix = np.empty((self.n, self.n))
        self.is_singular = False
        Rbf.__BuildInterpolant(self)
        self.average_error = 0
        self.errors = Rbf.LeaveOneOutError(self)

    def Norm(self, v):
        norm = 0
        for i in range(len(v)):
            norm += (self.__norm_weights[i]*v[i])**2
        return np.sqrt(norm)
    
    def MinBoundingNBallFromOrigin(self):
        max = np.zeros_like(self.coordinates[0])
        
        for coord in self.coordinates:
            for i, x in enumerate(coord):
                if max[i] < np.abs(x):
                    max[i] = np.abs(x)
        return 2*np.linalg.norm(max, 2)

    def __BuildInterpolant(self):
        for i in range(self.n):
            for j in range(i, self.n, 1):
                r = Rbf.Norm(self, self.coordinates[i] - self.coordinates[j])
                self.coefficient_matrix[i][j] = Rbf.__kernel(self, r)
                if i != j:
                    self.coefficient_matrix[j][i] = Rbf.__kernel(self, r)
        try:
            self.weights = np.linalg.solve(self.coefficient_matrix, self.function_values)
        except:
            print("ill-conditioned matrix (coefficient matrix not full rank)")
            self.is_singular = True
            return

    def Interpolate(self, point):
        out = 0
        for i in range(self.n):
            r = Rbf.Norm(self, self.coordinates[i] - point)
            out += Rbf.__kernel(self, r)*self.weights[i]
        return out

    #error is rms error
    def LeaveOneOutError(self):
        if self.is_singular:
            print("cannot compute error, interpolation matrix is singular")
            self.average_error = np.inf
            return
        inverse = np.linalg.inv(self.coefficient_matrix)
        error = [abs(self.weights[i]/inverse[i][i])**2 for i in range(self.n)]
        self.average_error = np.sqrt(abs(np.average(error)))
        return np.asarray(error)
    
    def ShapeOpitmizer(self, epsilon):
        self.epsilon = epsilon
        Rbf.__BuildInterpolant(self)
        error = Rbf.LeaveOneOutError(self)
        return self.average_error

    def __kernel(self, r):
        if self.kernel == "linear":
            return self.epsilon*r
        elif self.kernel == "cubic":
            return self.epsilon*r**3
        elif self.kernel == "thin_plate_spline":
            if r == 0:
                return 0
            else:
                return self.epsilon*r**2 * np.log(r)
        elif self.kernel == "quintic":
            return self.epsilon*r**5
        elif self.kernel == "gaussian":
            return np.exp(-1.0*(self.epsilon*r)**2)
        elif self.kernel == "multiquadric":
            return -1.0*np.sqrt(1 + (self.epsilon*r)**2)
        elif self.kernel == "inverse_quadric":
            return 1/(1 + (self.epsilon*r)**2)
    