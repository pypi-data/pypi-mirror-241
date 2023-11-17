import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Kernels(object):
    """
    Esta clase implementa el kernel gaussiano para suavizar una serie de tiempo.
    
    Parámetros:
    -----------
    data: str
        Ruta del archivo csv con los datos de la serie de tiempo.
    sigma: float
        Parámetro de suavizado.
        
    Métodos:
    --------
    PlotGaussianKernel()
        Grafica la serie de tiempo original y la suavizada.
    """
    
    
    def __init__(self,data,h):
        """
        Inicializa la clase KernelGaussiano.
        
        Parámetros:
        -----------
        data: str
            Ruta del archivo csv con los datos de la serie de tiempo.
            
        sigma: float
            Parámetro de suavizado.
        """
        self.h = h
        
        if not data.endswith('.csv'):
            raise ValueError("Data must be a .csv file")
        
        self.data  = pd.read_csv(data)
        
        if not isinstance(self.data,pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        if not isinstance(self.h,(int,float)):
            raise TypeError("Sigma must be a number")
        if self.h <= 0:
            raise ValueError("Sigma must be positive")
        if 'nuevos_casos' not in self.data.columns.str.lower():
            raise ValueError("Data must have 'nuevos_casos' column")
        if 'fecha_actualizacion' not in self.data.columns.str.lower():
            raise ValueError("Data must have 'fecha_actualizacion' column")
        
    def Tricube_Kernel(self,data):
        """
        Este método calcula el kernel tricúbico.
        
        Parámetros:
        -----------
        data : array
            Serie de tiempo.
            
        Retorna:
        --------
        Kernel tricúbico.
        """
        h = self.h
        
        def Kernel(x,x_,h):
            kernel = []
            for i in x:
                if abs(x_ - i)/h <= 1:
                    kernel.append((70/81)*(1-np.abs((x_ - i)/h)**3)**3)
                else:
                    kernel.append(0)   
            return np.array(kernel)
            
        smoothed_data = np.zeros_like(data)
        
        for i in range(len(data)):
            pesos = Kernel(np.arange(len(data)), i, h)
            smoothed_data[i] = np.sum(data * pesos)/np.sum(pesos)    
    
        return smoothed_data  
         
         
    def Gaussian_Kernel(self,data):
        """
        Este método calcula el kernel gaussiano.
        
        Parámetros:
        -----------
        data : array
            Serie de tiempo.
            
        Retorna:
        --------
        Kernel gaussiano.
        """
        sigma = self.h
        gaussKernel = lambda x,x_,sigma: np.exp(-(abs(x-x_))**2/(2*sigma)) 
        smoothed_data = np.zeros_like(data)
            
        for i in range(len(data)):
            pesos = gaussKernel(np.arange(len(data)), i, sigma)
            smoothed_data[i] = np.sum(data * pesos)/np.sum(pesos)
                
        return smoothed_data      
    
    def Epanechnikov_Kernel(self,data):
        """
        Este método calcula el kernel Epanechnikov.
        
        Parámetros:
        -----------
        data : array
            Serie de tiempo.
            
        Retorna:
        --------
        Kernel Epanechnikov.
        """
        
        h = self.h
        
        def Kernel(x,x_,h):
            kernel = []
            for i in x:
                if abs(x_ - i)/h <= 1:
                    kernel.append((3/4)*(1-(abs((x_ - i)/h))**2))
                else:
                    kernel.append(0)   
            return np.array(kernel)
        
        smoothed_data = np.zeros_like(data)
        
        for i in range(len(data)):
            pesos = Kernel(np.arange(len(data)), i, h)
            smoothed_data[i] = np.sum(data * pesos)/np.sum(pesos)
        
        return smoothed_data
    
    
    def Data(self):
        """ 
        Esta función retorna los datos de la serie de tiempo.
        
        Retorna:
        --------
        data: array
            Serie de tiempo.
        """
        
        #cargar datos
        df = self.data.copy()
        #convertimos columnas en minuscula
        df.columns = df.columns.str.lower()
        #transformamos a formato de fecha
        df['fecha_actualizacion'] = pd.to_datetime(df['fecha_actualizacion'])
        #separamos la fecha de la hora
        df['fecha_actualizacion'] = df['fecha_actualizacion'].dt.date
        
        #sacamos la columna de nuevos casos
        data = df['nuevos_casos'].to_numpy()
        
        return data
    
    def PlotGaussianKernel(self):
        """
        Este método grafica la serie de tiempo original y la suavizada con el kernel gaussiano.
        
        Retorna:
        --------
        Gráfica de la serie de tiempo original y la suavizada.
        """
        
        #cargamos los datos de la serie de tiempo
        data = self.Data()
        
        #creamos una nueva columna con los datos suavizados
        smoothed_data = self.Gaussian_Kernel(data)
        
        #graficamos
        _, ax = plt.subplots(figsize=(25,10))
        ax.plot(data, 'ko', label='Data')
        ax.plot(smoothed_data, 'r-', linewidth=3, label='Kernel_gaussiano')
        ax.legend(fontsize=20)
        ax.tick_params(axis='both', labelsize=20)
        plt.xticks(rotation=90)
        ax.set_xlabel('Fecha', fontsize=20)
        ax.set_ylabel('Número de nuevos casos', fontsize=20)
        ax.set_title('Número de nuevos casos de COVID-19', fontsize=20)
        plt.show()
        
    def PlotTricubeKernel(self):
        """
        Este método grafica la serie de tiempo original y la suavizada con el kernel tricúbico.
        
        Retorna:
        --------
        Gráfica de la serie de tiempo original y la suavizada.
        """
        
        #cargamos los datos de la serie de tiempo
        data = self.Data()
        
        #creamos una nueva columna con los datos suavizados
        smoothed_data = self.Tricube_Kernel(data)
        
        #graficamos
        _, ax = plt.subplots(figsize=(25,10))
        ax.plot(data, 'ko', label='Data')
        ax.plot(smoothed_data, 'r-', linewidth=3, label='Kernel_tricubico')
        ax.legend(fontsize=20)
        ax.tick_params(axis='both', labelsize=20)
        plt.xticks(rotation=90)
        ax.set_xlabel('Fecha', fontsize=20)
        ax.set_ylabel('Número de nuevos casos', fontsize=20)
        ax.set_title('Número de nuevos casos de COVID-19', fontsize=20)
        plt.show()
        
    def PlotEpanechnikovKernel(self):
        """
        Este metodo grafica la serie de tiempo original y la suavizada con el kernel Epanechnikov.
        
        Retorna:
        --------
        Gráfica de la serie de tiempo original y la suavizada.
        """
        
        #cargamos los datos de la serie de tiempo
        data = self.Data()
        
        #creamos una nueva columna con los datos suavizados
        smoothed_data = self.Epanechnikov_Kernel(data)
        
        #graficamos
        _, ax = plt.subplots(figsize=(25,10))
        ax.plot(data, 'ko', label='Data')
        ax.plot(smoothed_data, 'r-', linewidth=3, label='Kernel_Epanechnikov')
        ax.legend(fontsize=20)
        ax.tick_params(axis='both', labelsize=20)
        plt.xticks(rotation=90)
        ax.set_xlabel('Fecha', fontsize=20)
        ax.set_ylabel('Número de nuevos casos', fontsize=20)
        ax.set_title('Número de nuevos casos de COVID-19', fontsize=20)
        plt.show()
        
    def PlotAllKernels(self):
        """
        Este método grafica la serie de tiempo original y la suavizada con los Kernel Gaussianos, Tricúbico y Epanechnikov.
        
        Retorna:
        --------
        Gráfica de la serie de tiempo original y la suavizada con los Kernel Gaussianos, Tricúbico y Epanechnikov.
        """
        
        #cargamos los datos de la serie de tiempo
        data = self.Data()
        
        #creamos una nueva columna con los datos suavizados
        smoothed_data1 = self.Gaussian_Kernel(data)
        smoothed_data2 = self.Tricube_Kernel(data)
        smoothed_data3 = self.Epanechnikov_Kernel(data)
        
        #graficamos
        _, ax = plt.subplots(figsize=(25,10))
        ax.plot(data, 'ko', label='Data')
        ax.plot(smoothed_data1, 'r-', linewidth=3, label='Kernel_gaussiano')
        ax.plot(smoothed_data2, 'b-', linewidth=3, label='Kernel_tricubico')
        ax.plot(smoothed_data3, 'g-', linewidth=3, label='Kernel_Epanechnikov')
        ax.legend(fontsize=20)
        ax.tick_params(axis='both', labelsize=20)
        plt.xticks(rotation=90)
        ax.set_xlabel('Fecha', fontsize=20)
        ax.set_ylabel('Número de nuevos casos', fontsize=20)
        ax.set_title('Número de nuevos casos de COVID-19', fontsize=20)
        plt.show()

# if __name__ == "__main__":
#     data = "/home/luciano/FC120232/Bono 2/Colombia_COVID19_Coronavirus_casos_diarios.csv"
#     h= 18/2
#     kernel = Kernels(data,h)
    
#     kernel.PlotGaussianKernel()
#     kernel.PlotTricubeKernel()
#     kernel.PlotEpanechnikovKernel()
    
#     kernel.PlotAllKernels()
