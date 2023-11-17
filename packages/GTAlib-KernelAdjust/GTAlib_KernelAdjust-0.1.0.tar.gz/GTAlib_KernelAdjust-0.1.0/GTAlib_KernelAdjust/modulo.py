import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Kernels_DataAdjust:
    """
    Clase para el ajuste de datos utilizando el método del kernel Gaussiano.

        Args:

          - csv_file (str): Ruta al archivo CSV con las columnas 'nuevos_casos' y 'fecha_actualizacion'.
          - sigma (float, opcional): Valor de la desviación estándar para el cálculo de las gaussianas. 
            Por defecto, es 1.
        
        Methods:

          - _load_data(): Carga y normaliza los datos del archivo CSV.
          - _calculate_kernel(): Calcula el kernel usando el método del kernel Gaussiano.
          - plot_smooth_curve(): Grafica la curva suavizada de nuevos casos.
          - plot_derivative(): Grafica la derivada de la curva suavizada.
        
        Returns:

          Retorna la gráfica comparativa entre los datos suavizados y los reales.
          Además retorna la grafica de la respectiva derivada
    
    """
    def __init__(self, csv_file, sigma=1):
        """
        Inicializa la instancia de DataAdjust.

          Attributes:

            - csv_file (str): Ruta al archivo CSV con las columnas 'nuevos_casos' y 'fecha_actualizacion'.
            - sigma (float, opcional): Valor de la desviación estándar para el cálculo de las gaussianas. Por defecto es 1.
            - df (pd.DataFrame): DataFrame que contiene los datos cargados.
            - days_passed (np.ndarray): Array que representa los días transcurridos desde el primer caso.
            - x (np.ndarray): Array que representa los días transcurridos como valores.
            - y (np.ndarray): Array que representa los datos normalizados de nuevos casos.
            - smooth_curve (np.ndarray): Array que representa la curva suavizada de nuevos casos.
        """
        self.csv_file = csv_file
        self.sigma = sigma
        self.df = None
        self.days_passed = None
        self.x = None
        self.y = None

        self._load_data()

    def _load_data(self):
        """
        Carga y normaliza los datos del archivo CSV.

        """
        try:
            self.df = pd.read_csv(self.csv_file)
            self.df['FECHA_ACTUALIZACION'] = pd.to_datetime(self.df['FECHA_ACTUALIZACION'], format='%Y/%m/%d %H:%M:%S%z')
            self.df['NUEVOS_CASOS'] = self.df['NUEVOS_CASOS'] / self.df['NUEVOS_CASOS'].max()
            self.days_passed = (self.df['FECHA_ACTUALIZACION'] - self.df['FECHA_ACTUALIZACION'].min()).dt.days
            self.x = self.days_passed.values
            self.y = self.df['NUEVOS_CASOS'].values
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {self.csv_file}")
        except Exception as e:
            raise Exception(f"Error al cargar y normalizar datos: {e}")


    def Scaled_diff(self):
        self.scaled_differences = abs((self.x[:, np.newaxis] - self.x) / self.sigma)

    def Gauss_kernel(self):
        """
        Calcula el kernel usando el método de gaussianas de forma vectorizada.
        """
        try:
          kernels = np.exp(-0.5 * self.scaled_differences ** 2)
          self.Gauss_smooth_curve = np.sum(kernels * self.y, axis=1) / np.sum(kernels, axis=1)
        except Exception as e:
            raise Exception(f"Error al calcular el kernel: {e}")



    def Tricube_kernel(self):
        """
        Calcula el kernel usando el método de Tricube de forma vectorizada.
        """
        try:
            kernels = ((70/81)*(1-(self.scaled_differences*(self.scaled_differences<=1))**3)**3)*(self.scaled_differences<=1)
            
            self.Tricube_smooth_curve = np.sum(kernels * self.y , axis=1)/ np.sum(kernels, axis = 1)
        except Exception as e:
            raise Exception(f"Error al calcular el kernel: {e}")
        
    def Epanechnikov_kernel(self):
        """
        Calcula el kernel usando el método de Epanechnikov de forma vectorizada.
        """
        try:
            kernels = ((3/4)*(1-(self.scaled_differences*(self.scaled_differences<=1))**2))*(self.scaled_differences<=1)
            
            self.Epanechnikov_smooth_curve = np.sum(kernels * self.y , axis=1)/ np.sum(kernels, axis = 1)
        except Exception as e:
            raise Exception(f"Error al calcular el kernel: {e}")

    def plot_smooth_curves(self):
        """
        Grafica la curva suavizada de nuevos casos.
        """
        try:    
            self.Scaled_diff()
            self.Gauss_kernel()
            self.Tricube_kernel()
            self.Epanechnikov_kernel()
            Smooth_Curves = {'Gauss': self.Gauss_smooth_curve,'Tricube': self.Tricube_smooth_curve,'Epanechnikov':self.Epanechnikov_smooth_curve }
            
            for kernel_name, curve in Smooth_Curves.items():
                plt.plot(self.days_passed, self.y, label='Datos Reales', color='blue', alpha=0.5)
                plt.plot(self.days_passed, curve, color='red', label = kernel_name)
                plt.xlabel('Días transcurridos')
                plt.ylabel('Casos Nuevos (Normalizado)')
                plt.legend()
                plt.title('Casos diarios de Covid-19 en Colombia')
                plt.show()
        except Exception as e:
            raise Exception(f"Error al graficar la curva suavizada: {e}")

    

    def comparison(self):
        self.Scaled_diff()
        self.Gauss_kernel()
        self.Tricube_kernel()
        self.Epanechnikov_kernel()
        Smooth_Curves = {'Gauss': self.Gauss_smooth_curve,'Tricube': self.Tricube_smooth_curve,'Epanechnikov':self.Epanechnikov_smooth_curve }
        for kernel_name, curve in Smooth_Curves.items():
            plt.plot(self.days_passed, curve, label = kernel_name)
            plt.xlabel('Días transcurridos')
            plt.ylabel('Casos Nuevos (Normalizado)')
            plt.legend()
            plt.title('Grafica comparativa de kernels')
        plt.show()