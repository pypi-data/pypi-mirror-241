import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class smoother:

    def __init__(self, path : str , par : float):
        """
        path: direccion del archivo csv
        par: factor de suavizado (0<par<1, entre mas cercano a 0, mas suavizado)
        kernel: kernel de suavizado, valores posibles: (gauss,tricube)
        
        Esta clase lee un archivo csv con datos de casos nuevos de covid-19 en Colombia,
        con columnas 'fecha_actualizacion' y 'nuevos_casos', y genera un ajuste 
        suave de los datos
        """

        self.doc = pd.read_csv(path)
        self.sg=par
        self.y=self.doc['nuevos_casos']
        self.fechas=pd.to_datetime(self.doc['fecha_actualizacion'])
        self.x=np.arange(0,len(self.y),1)
        self.ker=None

    def kernelGauss(self):
        self.ker='gaus' 
        return self.plot('Gauss')

    def kernelTricube(self):
        self.ker='tricube'
        return self.plot('Tricube')

    def kernelEpan(self):
        self.ker='epan'
        return self.plot('Epanechnikov')
            

    def kerneli(self, x : float ,xi : float ,y : float):
        """
        x: vector de fechas
        xi: dato a evaluar
        y: vector de casos nuevos

        Este metodo calcula el kernel de la funcion de suavizado
        """
        if self.ker == 'gaus':
            kernel= lambda x,xi,y: y*np.exp(-abs(x-xi)**2/(2*self.sg))
        elif self.ker == 'tricube':
            def kernel(x,xi,y):
                core = abs((xi-x)/self.sg)
                if core <= 1:
                    return y*70/81*(1-core**3)**3
                else:
                    return 0
        elif self.ker=='epan':
            def kernel(x,xi,y):
                core = abs((xi-x)/self.sg)
                if core <= 1:
                    return y*0.75*(1-core**2)
                else:
                    return 0
        else:
            print('Ingrese un kernel válido: gauss, tricube, epan')
            kernel=lambda x,xi,y: y*np.exp(-abs(x-xi)**2/(2*self.sg**-1))
        return kernel(x,xi,y)
    
    def kernelisum(self, X : float):
        """
        X: vector de fechas

        Este metodo calcula la suma de los kernels de la funcion de suavizado,
        dando el valor de la funcion de suavizado en X
        """

        kernelsum=0
        for i in range(len(self.x)):
            ks=self.kerneli(X,self.x[i],self.y[i])
            kernelsum+=ks
        return kernelsum
    
    def arraysum(self):
        """
        Este metodo calcula la funcion de suavizado en todo el rango de fechas
        """

        Y=np.zeros(len(self.x))
        for i in range(len(self.x)):
            Y[i]=self.kernelisum(self.x[i])
        maximo=max(Y)
        return max(self.y)*Y/maximo

    def plot(self, title, name : str = 'plotCovid',safe=True,datos=True):
        """
        Este metodo grafica los datos y el ajuste suave
        """
        if datos==True:
            plt.plot(self.fechas,self.y,label='Datos')
        plt.plot(self.fechas,self.arraysum(),label='Ajuste')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.title(f'Suavizado con kernel de {title}')
        if safe==True:
            plt.savefig(name)
        return f'{name}.png'
    
    def plotComparativo(self):
        self.ker='gaus'
        self.plot('',safe=False,datos=False)

        self.ker='epan'
        self.plot('',safe=False,datos=False)

        self.ker='tricube'
        self.plot('',safe=False,datos=False)

        plt.title('Plot comparativo de los ajustes')
        plt.savefig('plotComparativo')
        plt.close()
