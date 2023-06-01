import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
sym.init_printing() # esto se usa para que las expresiones matemmaticas se impriman de una mmanera vistosa

t = sym.symbols('t', real=True)
k = sym.symbols('k', integer=True)


def ideal_sampling(x, k, w_s):
    """
        muestreo ideal de una señal continua
        x = señal continua 
        w_s = frecuencia de muestreo 
        kappa = variable de tiempo discreta utilizada en el muestreo.

    """ 
    kappa = sym.symbols('kappa')
    xs = sym.lambdify(kappa, x.subs(t, kappa * 2 * sym.pi / w_s))  #muestreo 
    return [xs(kappa) for kappa in k] #resultante del muestreo 


def ideal_reconstruction(xs, k, w_s):
    T = 2*sym.pi/w_s
    return sum(xs[n] * sym.sinc(sym.pi / T * (t - k[n] * T)) for n in range(len(k)))


def plot_signals(xs, y, w_s, k):
    plt.stem(k*2*np.pi/w_s, xs) # genera un grafica = señal muestreada
    plt.xlabel('$t$ in s')
    plt.ylabel('$x_s[k] = x_s(kT)$') 
    plt.axis([0, 5, -1.2, 1.2])

    sym.plot(y, (t, 0, 5), xlabel='$t$', ylabel='$y(t)$', ylim=(-1.2, 1.2)) #gráfico de la señal continua

#senal
w_0 = 50
w_1 = 30
x = sym.cos(w_0 * t)*sym.cos(w_1 * t)

k = np.arange(-100, 100)

w_s = 200    # frecuencia de muestro
xs = ideal_sampling(x, k, w_s)
y = ideal_reconstruction(xs, k, w_s)

plot_signals(xs, y, w_s, k)







