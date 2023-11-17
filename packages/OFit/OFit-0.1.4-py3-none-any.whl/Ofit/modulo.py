import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class KernelFit:

    """
    Esta clase se encarga de realizar el analisis de datos usando un kernel gaussiano, trucube y Epanechnikov
    Input:  
    path: ruta del archivo csv con columnas "NUEVOS_CASOS"

    Output:
    data: plot de los datos y su ajuste

    """

    def __init__(self,h,path):
        self.path = path
        self.data = None
        self.casos= None
        self.fechas= None
        self.h= h
        self.kernelTC = lambda x,N: N*(70/81)*(1-(np.abs(x/self.h))**3)**3 if abs(x/self.h)<=1 else 0
        self.kernelEpa = lambda x,N: N*(3/4)*(1-(np.abs(x/self.h))**2) if abs(x/self.h)<=1 else 0
        self.kernelG = lambda x,N: N*np.exp(-np.abs(x)**2/(2*self.h))


    

    def read_data(self):
        """Lee los datos del archivo csv"""
        try:
            self.data = pd.read_csv(self.path)
            self.casos = self.data["NUEVOS_CASOS"]
            self.Fecha = pd.to_datetime(self.data["FECHA_ACTUALIZACION"]) #Se usa para hacer el plot
            self.fechas = np.arange(0,len(self.casos),1) #Se usa para hacer los cálculos
        
        except:
            print("Error al leer el archivo")
        return True
    
    def calcularpunto(self,kernel,xi,N):
        """x: arreglo 
            xi: punto a evaluar
        """
        try:
            x_xi = self.fechas-xi #Resta de arreglos
            
            K = np.zeros(len(x_xi))
            for i in range(len(x_xi)):
                K[i] = kernel(x_xi[i],self.casos[i]) #Evaluacion del kernel
        except:
            print("Error al calcular el kernel")
        return sum(K)
    
    def fit(self,kernel):
        """Calcula el suavizado de los datos
        """
        try:
            y = []
            for i in range(len(self.fechas)):#Recorre todos los puntos
                y.append(self.calcularpunto(kernel,self.fechas[i],self.casos[i]))
        except:
            print("Error al calcular el suavizado")
        return np.array(y)
    
    def dataplot(self):
        """Retorna los datos y el suavizado
        """
        x = self.fechas
        y_data = self.casos
        y_fit = self.fit()
        return x,y_data,y_fit*max(y_data)/max(y_fit)
    
    def plot_kernel_Gauss(self):
        self.read_data()
        """Grafica los datos y el suavizado"""
        x = self.Fecha
        yd = self.casos
        yf = self.fit(self.kernelG)
        yf = yf*max(yd)/max(yf)
        plt.figure(figsize=(8,6))
        plt.plot(x,yd,label="Datos",color = "darkblue")
        plt.plot(x,yf,label="Suavizado",color = "darkred")
        plt.xlabel("Dias")
        plt.ylabel("Casos")
        plt.xticks(rotation=45)
        plt.title("Fit Kernel Gauss")
        plt.legend()
        plt.savefig("Gauss.png")
        print("Terminado")
        return True
    
    def plot_kernel_Tricube(self):
        self.read_data()
        """Grafica los datos y el suavizado"""
        x = self.Fecha
        yd = self.casos
        yf = self.fit(self.kernelTC)
        yf = yf*max(yd)/max(yf)
        plt.figure(figsize=(8,6))
        plt.plot(x,yd,label="Datos",color = "darkblue")
        plt.plot(x,yf,label="Suavizado",color = "darkred")
        plt.xlabel("Dias")
        plt.ylabel("Casos")
        plt.xticks(rotation=45)
        plt.title("Fit Kernel Tricube")
        plt.legend()
        plt.savefig("Tricube.png")
        print("Terminado")
        return True
    

    def plot_kernel_Epanechnikov(self):
        self.read_data()
        """Grafica los datos y el suavizado"""
        x = self.Fecha
        yd = self.casos
        yf = self.fit(self.kernelEpa)
        yf = yf*max(yd)/max(yf)
        plt.figure(figsize=(8,6))
        plt.plot(x,yd,label="Datos",color = "darkblue")
        plt.plot(x,yf,label="Suavizado",color = "darkred")
        plt.xlabel("Dias")
        plt.ylabel("Casos")
        plt.xticks(rotation=45)
        plt.title("Fit Kernel Epanechnikov")
        plt.legend()
        plt.savefig("Epanechnikov.png")
        print("Terminado")
        return True
    
    def run(self):
        """Ejecuta el analisis"""
        self.read_data()    
        self.plot()
        return True
