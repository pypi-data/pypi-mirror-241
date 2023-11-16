import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataAdjust:
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
            self.df['fecha_actualizacion'] = pd.to_datetime(self.df['fecha_actualizacion'], format='%Y/%m/%d %H:%M:%S%z')
            self.df['nuevos_casos'] = self.df['nuevos_casos'] / self.df['nuevos_casos'].max()
            self.days_passed = (self.df['fecha_actualizacion'] - self.df['fecha_actualizacion'].min()).dt.days
            self.x = self.days_passed.values
            self.y = self.df['nuevos_casos'].values
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {self.csv_file}")
        except Exception as e:
            raise Exception(f"Error al cargar y normalizar datos: {e}")

    def _calculate_kernel(self):
        """
        Calcula el kernel usando el método de gaussianas de forma vectorizada.
        """
        try:
          scaled_differences = (self.x[:, np.newaxis] - self.x) / self.sigma
          kernels = np.exp(-0.5 * scaled_differences ** 2)
          self.smooth_curve = np.sum(kernels * self.y, axis=1) / np.sum(kernels, axis=1)
        except Exception as e:
            raise Exception(f"Error al calcular el kernel: {e}")

    def plot_smooth_curve(self):
        """
        Grafica la curva suavizada de nuevos casos.
        """
        try:
            self._calculate_kernel()
            plt.plot(self.days_passed, self.y, label='Datos Reales', color='blue', alpha=0.5)
            plt.plot(self.days_passed, self.smooth_curve, color='red')
            plt.xlabel('Días transcurridos')
            plt.ylabel('Casos Nuevos (Normalizado)')
            plt.title('Casos diarios de Covid-19 en Colombia')
            plt.show()
        except Exception as e:
            raise Exception(f"Error al graficar la curva suavizada: {e}")

    def plot_derivative(self):
        """
        Grafica la derivada de la curva suavizada.
        """
        try:
            self._calculate_kernel()
            derivative = np.gradient(self.smooth_curve, self.days_passed)
            plt.plot(self.days_passed, derivative)
            plt.xlabel('Días transcurridos')
            plt.title('Tasa de Cambio de infectados diarios')
            plt.show()
        except Exception as e:
            raise Exception(f"Error al graficar la derivada: {e}")