from typing import Any
from copy import deepcopy

import sympy
import matplotlib.pyplot as plt
import numpy as np

from utils import timeit

TABLE={}



class HarmonicOscillator:
    psi: Any
    x: Any
    reference_table: dict
    norm: float # Optional

    def __init__(self, n, reference_table=TABLE):
        self.reference_table=reference_table
        self.norm=None

        def psi1():
            psi, x=sympy.symbols("psi x")
            psi=sympy.exp(-x**2/2)
            return psi, x
        
        def ladder(harmonic_o: HarmonicOscillator):
            psi2, x2=sympy.symbols("psi x")
            psi, x=harmonic_o.psi, harmonic_o.x
            psi2=x*psi-sympy.diff(psi, x)
            psi2=psi2.subs(x, x2)
            return psi2, x2

        if n in self.reference_table:
            self=deepcopy(self.reference_table[n])
        elif n==0:
            self.x=sympy.symbols("x")
            self.psi=sympy.Integer(0)
        elif n==1:
            self.psi, self.x= psi1()
        else:
            prev: HarmonicOscillator
            if n-1 in self.reference_table:
                prev=self.reference_table[n-1]
            else:
                prev=HarmonicOscillator(n-1)
            psi2, x2=ladder(prev)
            self.psi=psi2
            self.x=x2
        self.psi=sympy.simplify(self.psi)
        self.reference_table[n]=self
        print(f"Harmonic Oscillator {n} Calculated.")
        
    
    def evaluate(self, x1):
        return self.psi.subs(self.x, x1).evalf()

    @staticmethod
    def _norm(expr, x):
        return sympy.integrate(expr, (x, -sympy.oo, sympy.oo))
    def get_norm(self):
        if self.norm is None:
            self.norm=HarmonicOscillator._norm(self.psi**2, self.x)
        return self.norm
    
    def pdf(self, x1, normalize=True):
        if normalize:
            if self.norm is None:
                self.norm=HarmonicOscillator._norm(self.psi**2, self.x)
            return self.evaluate(x1)**2/self.norm
        else:
            return self.evaluate(x1)**2
    
    @timeit
    def plot_pdf(self, path=None, normalize=True):
        X=np.linspace(-5, 5, 500)
        Y=[self.pdf(x, normalize=normalize) for x in X]
        plt.plot(X, Y)
        if path is None:
            plt.show()
        else:
            plt.savefig(path)
        plt.clf()
    
    def E(self):
        HE=-sympy.diff(sympy.diff(self.psi, self.x), self.x)/2+self.x**2*self.psi/2
        print(HE)
        return HarmonicOscillator._norm(HE, self.x)/HarmonicOscillator._norm(self.psi, self.x)


    
if __name__=='__main__':
    h7= HarmonicOscillator(7)
    print(h7.E())
    h7.plot_pdf('7.pdf')

