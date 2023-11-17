import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as datetime

class Kernels:
    def __init__(self, url, param):
        self.u = url
        self.h = param
        try:
            1/self.h
        except ZeroDivisionError:
            print('Parametro no puede ser 0')

    def Dataframe(self):
        """ 
        Formatea y extrae información de un archivo .csv con columnas Nuevos_casos y Fecha_actualizacion 
        """
        self.df = pd.read_csv(self.u) 
        self.df.columns = self.df.columns.str.lower()
        self.y = self.df['nuevos_casos']                    
        self.y = (self.y)/(self.y).max()                                                                               # Normalizando
        self.df['fecha_actualizacion'] = pd.to_datetime(self.df['fecha_actualizacion'], format='%Y/%m/%d %H:%M:%S%z')  # Cambiando a formato datetime
        self.x = self.df['fecha_actualizacion']                                                                        # Fecha en formato necesario

        self.C = abs(self.x[0]-self.x)                                                                                 # Para gráficos
        for i in range(len(self.C)):
            self.C[i]=self.C[i].days                                                                                   # arreglo de dias

    def Tricube(self):
        """ 
        Se actualizan los datos para las gráficas, es un método interno para otros métodos
        """
        self.Dataframe()

        self.A = np.zeros((len(self.x),len(self.x)))
        self.T = np.zeros(len(self.x)) 
        self.T1=[]

        for j in range(len(self.x)):
            for i in range(len(self.x)):
                if np.abs((self.x[j]-self.x[i]).days/self.h) <= 1:
                    self.A[j,i] = 1 - (np.abs((self.x[j]-self.x[i]).days/self.h))**3                    # .days Arreglo 2d con las diferencias de fechas al cuadrado
                else:
                    self.A[j,i] = 0
            self.T1.append(self.y * (70/81) * (self.A[j])**3)
            self.T[j]=self.T1[j].sum()/((70/81) * (self.A[j])**3).sum()  

    def Epane(self):
        """ 
        Se actualizan los datos para las gráficas, es un método interno para otros métodos
        """
        self.Dataframe()

        self.B = np.zeros((len(self.x),len(self.x)))
        self.E = np.zeros(len(self.x)) 
        self.E1=[]

        for j in range(len(self.x)):
            for i in range(len(self.x)):
                if np.abs((self.x[j]-self.x[i]).days/self.h) <= 1:
                    self.B[j,i] = 1 - (np.abs((self.x[j]-self.x[i]).days/self.h))**2                   
                else:
                    self.B[j,i] = 0
            self.E1.append(self.y * (3/4) * (self.B[j]))
            self.E[j]=self.E1[j].sum()/((3/4) * (self.B[j])).sum()  

    def Gaussiano(self):
        """ 
        Se actualizan los datos para las gráficas, es un método interno para otros métodos
        """
        self.Dataframe()

        self.G2 = np.zeros((len(self.x),len(self.x)))
        self.G = np.zeros(len(self.x)) 
        self.G1=[]

        for j in range(len(self.x)):
            for i in range(len(self.x)):
                self.G2[j,i] = np.abs((self.x[j]-self.x[i]).days)**2           # .days Arreglo 2d con las diferencias de fechas al cuadrado
            self.G1.append( self.y *  np.exp(-(self.G2[j])/(2*self.h)))
            self.G[j]=self.G1[j].sum() / np.exp(-(self.G2[j])/(2*self.h)).sum()

    def GraphTri(self):
        self.Tricube()
        plt.plot(self.C, self.T)
        plt.xlabel('Días transcurridos desde primer caso')
        plt.ylabel('# Casos Nuevos / # Máximo de casos')
        plt.title('Covid 19 en Colombia')
        plt.show()

    def GraphEpane(self):
        self.Epane()
        plt.plot(self.C, self.E)
        plt.xlabel('Días transcurridos desde primer caso')
        plt.ylabel('# Casos Nuevos / # Máximo de casos')
        plt.title('Covid 19 en Colombia')
        plt.show()
    
    def GraphGauss(self):
        self.Gaussiano()
        plt.plot(self.C, self.G)
        plt.xlabel('Días transcurridos desde primer caso')
        plt.ylabel('# Casos Nuevos / # Máximo de casos')
        plt.title('Covid 19 en Colombia')
        plt.show()

    def GraphAll(self):
        self.Tricube()
        self.Epane()
        self.Gaussiano()
        #plt.plot(self.C, self.y, label='Original')
        plt.plot(self.C, self.T, label='Tricube', color='black')
        plt.plot(self.C, self.E, label='Epanechnikov', alpha = 0.7, color='red')
        plt.plot(self.C, self.G, label='Gaussiano', alpha = 0.5, color='blue')
        plt.legend()
        plt.xlabel('Días transcurridos desde primer caso')
        plt.ylabel('# Casos Nuevos / # Máximo de casos')
        plt.title('Comparacion Kernels')
        plt.show()
        