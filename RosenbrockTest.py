# File to test the performance of the Rosenbrock function on the
# classical Newtons method. (Task 5)
import numpy as np
import unittest as ut
#from OptimizationProblem import *
from OptimizationProblem import *

def f(x,y):
    return 100*(y-x**2)**2 + (1 - x)**2

def df_dx(x,y):
    return 400*(x**3) - 400*x*y - 2 + 2*x

def df_dy(x,y):
    return 200*y - 200*(x**2)

def df_dx2(x,y):
    return 1200*(x**2) - 400*y + 2

def df_dxy(x,y):
    return -400*x

def df_dy2(x,y):
    return 200
    
grad = [df_dx,df_dy]

#problem = OptimizationProblem(f,grad)

## Solve the problem with a method here

def manual_hessian(x,y):
    return [[df_dx2(x,y), df_dxy(x,y)],[df_dxy(x,y), df_dy2(x,y)]]

class RosenbrockTestCase(ut.TestCase):
    def setUp(self):
        self.man_gradient = [df_dx(1,2), df_dy(1,2)]
        self.man_hess = manual_hessian(1,2)
    #Test of function without a supplied gradient
    def testCalculatedGradient(self):
        op = OptimizationProblem(f)
        gradient = op.get_gradient_at(1,2)
        np.testing.assert_allclose(gradient, self.man_gradient)
    #Test of function with a supplied gradient:
    def testSuppliedGradient(self):
        op = OptimizationProblem(f, grad)
        gradient = op.get_gradient_at(1,2)
        np.testing.assert_allclose(gradient, self.man_gradient)
    #Testing the hessian without a supplied gradient
    def testHessianFunctionWithoutGradient(self):
        op = OptimizationProblem(f)
        hessian = op.get_hessian(1,2)
        np.testing.assert_allclose(self.man_hess, hessian) #, 0.0001)
    #Testing the hessian with a supplied gradient
    def testHessianFunctionWithGradient(self):
        op = OptimizationProblem(f, grad)
        hessian = op.get_hessian(1,2)
        np.testing.assert_allclose(self.man_hess, hessian) #, 0.0001)

if __name__=='__main__':
    ut.main()