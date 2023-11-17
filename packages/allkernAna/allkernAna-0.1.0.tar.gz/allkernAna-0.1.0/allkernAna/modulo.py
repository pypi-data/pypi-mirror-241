import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class suavizado:

    def __init__(self, nombreDocumento, sigma):
        self.df = pd.read_csv(nombreDocumento)
        self.sigma = sigma

    def kerGaus(self, numCasos, sigma):
        def func(x, x_, sigma):
            return np.exp(-(abs(x-x_)) ** 2 / (2*sigma))
        datos_f = np.zeros_like(numCasos)

        for i in range(len(numCasos)):
            pesos = func(np.arange(len(numCasos)), i, sigma)
            datos_f[i] = np.sum(numCasos * pesos)/ np.sum(pesos)

        return datos_f
    
    def triKern(self, numCasos, h):
        def func(x, x_, h):
            L_ = []
            for i in range(len(x)):
                if abs((x[i]-x_)/h) <= 1:
                    L_.append(70/81 * (1 - abs((x[i]-x_)/h)**3)**3)
                else:
                    L_.append(0)
            return L_
        datos_f = np.zeros_like(numCasos)
        
        for i in range(len(numCasos)):
            pesos = func(np.arange(len(numCasos)), i, h)
            datos_f[i] = np.sum(numCasos * pesos)/ np.sum(pesos)

        return datos_f
    
    def Epanechnikov(self, numCasos, h):
        def func(x, x_, h):
            L_ = []
            for i in range(len(x)):
                if abs((x[i]-x_)/h) <= 1:
                    L_.append(3/4 * (1 - abs((x[i]-x_)/h)**2))
                else:
                    L_.append(0)
            return L_
        datos_f = np.zeros_like(numCasos)
        
        for i in range(len(numCasos)):
            pesos = func(np.arange(len(numCasos)), i, h)
            datos_f[i] = np.sum(numCasos * pesos)/ np.sum(pesos)

        return datos_f

    
    def figPlot(self):
        y = self.kerGaus(self.df.NUEVOS_CASOS, self.sigma)

        places = np.linspace(0, len(self.df) - 1, 8)
        ticks = []

        for i in places:
            ticks.append(self.df.FECHA_ACTUALIZACION[int(i)].split(' ')[0])

        y2 = self.triKern(self.df.NUEVOS_CASOS, self.sigma)
        y3 = self.Epanechnikov(self.df.NUEVOS_CASOS, self.sigma)
        plt.plot(self.df.FECHA_ACTUALIZACION, self.df.NUEVOS_CASOS, label= 'Datos')
        plt.plot(self.df.FECHA_ACTUALIZACION, y, label='Kernel gausiano')
        plt.plot(self.df.FECHA_ACTUALIZACION, y2, label='Kernel tricube')
        plt.plot(self.df.FECHA_ACTUALIZACION, y3, label='Kernel Epanechnikov')
        plt.legend()
        plt.xticks(places, ticks, rotation = 45)
        plt.ylabel('Nuevos casos')
        plt.savefig('Nuevos_Casos_Suavizado.png')