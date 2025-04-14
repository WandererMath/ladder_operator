# About the Project 

Illustrate ladder operator for 1D harmonic quantum oscillators.

``` math
\hat{H}\psi=E\psi
```

With natural units and the potential strength $\omega=1$,
``` math
\hat{p}=-i\frac{d}{dx}
```

``` math
\hat{H}=-\frac{\hat{p}^2}{2}+\frac{x^2}{2}
```

Define creation operator:
``` math
a_{+}=x-i\hat{p}
```

# Install requirements
``` bash
pip install -r requirements.txt
```

# Usage
To create a quantum harmonic oscillator of the n-th lowest energy state:
``` python
oscillator= HarmonicOscillator(n)
```

To view its analytic formula:
``` python
print(oscillator)
```

To plot probability density vs. postioin:
``` python
oscillator.plot_pdf("filename.pdf")
```

To calculate the energy by 
```math
E=\frac{\int_{-\infty}^{\infty} \hat{H}\psi~ dx}{\int_{-\infty}^{\infty} \psi ~dx}, 
```
as a verification:
``` python
E=oscillator.E()
```
