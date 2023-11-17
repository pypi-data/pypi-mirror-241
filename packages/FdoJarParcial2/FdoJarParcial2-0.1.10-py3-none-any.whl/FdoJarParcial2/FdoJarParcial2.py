from typing import Any
import numpy as np
from typing import List,Callable
import matplotlib.pyplot as plt
import pandas as pd


class SuavKernel:
    """
    Calse para realizar un suavizado de curvas con distintas funciones kernel
    """

    def __init__(self,DataName:str,h:float) -> None:
        """
        Inicializa la clase

        DataName:str
            Nombre del archivo
            Debe contener las columnas 'FECHA_ACTUALIZACION' y  'NUEVOS_CASOS'

        h: float
            valor de h para calcular el kernel

        """
        data = pd.read_csv(DataName)
        data.index = pd.to_datetime(data['FECHA_ACTUALIZACION'], format='%Y/%m/%d %H:%M:%S+00')
        data.index = data.index.date


        self.data = data
        self.h = h

        pass



    def KernelGaussiano(self,Xn:List[float],Xm:float,h:float) -> List[float]:
        """
        Retorna los pesos usando el kernel Gaussiano
        """
        return np.exp(-(Xn-Xm)**2/(2*h))
    
   
    def kernelTriCubico(self,Xn:List[float],Xm:float,h:float) -> List[float]:
        """
        Retorna los pesos usando el kernel Tricube
        """
        N = len(Xn)
        pesos = np.zeros(N)

        for i in range(N):
            A = abs(Xn[i]-Xm)/h

            if A<=1:
                pesos[i] = 70/81*(1-A**3)**3
            elif A>1:
                pesos[i] = 0

        return pesos
    
    
    def KernelEpanechnikov(self,Xn:List[float],Xm:float,h:float) -> List[float]:
        """
        Retorna los pesos usando el kernel Epanechnikov
        """
        N = len(Xn)
        pesos = np.zeros(N)

        for i in range(N):
            A = abs(Xn[i]-Xm)/h
            if A<=1:
                pesos[i] = 3/4*(1-A**2)
            elif A>1:
                pesos[i] = 0
        
        return pesos
    

    def SuavizadoGauss(self) -> None:
        """
        Realiza el suavizado con el kernel Gaussiano
        Genera un gráfica pero no la guarda

        Para guardar la gráfica se debe llamar luego al método GuardarFigura
        """
        DataY = self.data['NUEVOS_CASOS']
        h = self.h
        N = len(DataY)
        sol = np.zeros(N)
        for i in range(N):
            temp = self.KernelGaussiano(np.arange(N),i,h)
            sol[i] = np.sum(DataY*temp)/sum(temp)
        
        plt.plot(self.data.index,sol,label='Gauss')

    
    def SuavizadoTriCube(self) -> None:
        """
        Realiza el suavizado con el kernel TriCube
        Genera un gráfica pero no la guarda

        Para guardar la gráfica se debe llamar luego al método GuardarFigura
        """
        DataY = self.data['NUEVOS_CASOS']
        h = self.h
        N = len(DataY)
        sol = np.zeros(N)
        
        for i in range(N):
            temp = self.kernelTriCubico(np.arange(N),i,h)
            sol[i] = np.sum(DataY*temp)/sum(temp)

        plt.plot(self.data.index,sol,label='TriCube')
    
    def SuavizadoEpanechnikov(self) -> None:
        """
        Realiza el suavizado con el kernel Epanechnikov
        Genera un gráfica pero no la guarda

        Para guardar la gráfica se debe llamar luego al método GuardarFigura
        """
        DataY = self.data['NUEVOS_CASOS']
        h = self.h
        N = len(DataY)
        sol = np.zeros(N)
        for i in range(N):
            temp = self.KernelEpanechnikov(np.arange(N),i,h)
            sol[i] = np.sum(DataY*temp)/sum(temp)

        plt.plot(self.data.index,sol,label='Epanechnikov')
    
    def GuardarFigura(self,Nombre:str):
        """
        Guarda la gráfica llamada Nombre.jpg
        """

        plt.plot(self.data.index,self.data['NUEVOS_CASOS'],'.',label='Datos Originales',color='grey',zorder=0)

        plt.legend()
        plt.xlabel('Fecha')
        plt.ylabel('Nuevos Casos')
        plt.xticks(rotation=45)

        plt.savefig('{}.jpg'.format(Nombre))