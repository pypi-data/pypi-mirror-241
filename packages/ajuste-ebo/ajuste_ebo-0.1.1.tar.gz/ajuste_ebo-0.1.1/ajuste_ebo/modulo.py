import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tqdm


class ajuste_curva:

    """
    
    Clase que nos va a permitir por medio de un kernel gaussiano
    suavisar la curva de unos datos, en este caso, datos realacionados
    con los nuevos casos de COVID-19 por días.
    
    """

    def __init__(self, path):
        
        """
        Constructor de la clase.
        Recibe la dirección del archivo csv con los datos.
        ¡¡ El csv debe tener las siguientes columnas!! 
        -- 'fecha_actualizacion' : fecha de actualización de los datos
        -- 'nuevos_casos'  : número de casos nuevos en el día
        """

        self.path = path
        usecols = ['FECHA_ACTUALIZACION', 'NUEVOS_CASOS']
        try:
            self.data = pd.read_csv(self.path, sep=',', header=0, usecols=usecols)
        except Exception as e:
            print(f'Error al leer el archivo, revise la dirección y/o estructura del archivo{e}') 
            self.data = None
        self.x = np.arange(0, len(self.data['FECHA_ACTUALIZACION']),1)
        self.y = self.data['NUEVOS_CASOS'].to_numpy()

    def kernel_tricube(self, x_a, x, r):
            
        """
        Método que nos permite calcular el kernel tricube.
        Recibe:
        -> x_a: punto al que se quiere evaluar
        -> x: punto en el que se encuentra
        -> r: valor de h

        """    
        try:
            factor = (x-x_a)/r
            if np.abs(factor) <= 1:
                k = (70/81) * (1 - np.abs(factor)**3 )**3
            else:
                k = 0
                
        except Exception as e:
            print(f'Error al calcular el kernel tricube{e}')
        else:
            return k
        

    def kernel_gauss(self, x_a, x, r):
            
        """
        Método que nos permite calcular el kernel gaussiano.
        Recibe:
        -> x_a: punto al que se quiere evaluar
        -> x: punto en el que se encuentra
        -> r: valor de h 

        """    
        try:
            sigma = 1/r
            w = 1 # Factor de normalización
            k = w * np.exp(-np.abs(x_a-x)**2/(2*sigma))
        except Exception as e:
            print(f'Error al calcular el kernel gaussiano{e}')
        else:
            return k
        
    def kernel_epanechnikov(self, x_a, x, r):

        """
        Método que nos permite calcular el kernel Epanechnikov.
        Recibe:
        -> x_a: punto al que se quiere evaluar
        -> x: punto en el que se encuentra
        -> r: valor de h 

        """    
        try:
            factor = (x-x_a)/r
            if np.abs(factor) <= 1:
                k = (3/4) * (1 - np.abs(factor)**2 )
            else:
                k = 0
                
        except Exception as e:
            print(f'Error al calcular el kernel Epanechnikov {e}')
        else:
            return k
       
        


    def curva(self,x,y,r,tipo):
        """
        Método que nos permite calcular la curva suavizada.
        Recibe:
        
        -> x: datos en x (días)
        -> y: datos en y (nuevos casos)
        -> r: valor de h 
        -> tipo: tipo de kernel a usar (gaussiano, tricube o epanechnikov)
                tipo str  

        return: curva suavizada
        """

        try:
            kernel = {'gaussiano':self.kernel_gauss,'tricube':self.kernel_tricube , 'epanechnikov':self.kernel_epanechnikov}
            y = np.zeros(len(self.x))
            for j in tqdm.tqdm(range(len(self.x))):
                y_i= []
                for i in range(len(self.x)):
                    y_i.append(kernel[tipo](self.x[j],self.x[i],r)*self.y[i])
                    # print(y_i[i])
                y[j] = np.sum(y_i)

            return (self.y.max()*y)/y.max()
                    
        except Exception as e:
            print(f"Error al calcular la curva suavizada{e}")




    def plot(self,r,tipo):
        
        """
        Método que nos permite graficar los datos vs la curva suavizada.

        Se debe ingresar el valor de r para determinar sigma.

        """

        try:
            y = self.curva(self.x,self.y,r,tipo)
            plt.title(f'Curva suavizada con kernel {tipo} y h = {r} ')
            plt.plot(self.x, self.y,label='Datos')
            plt.plot(self.x, y,label='Curva suavizada')
            plt.legend()
        except Exception as e:
            print(f"Error al graficar los datos{e}")
        else:
            plt.savefig(f'data_{tipo}.png')  
            plt.close()
            

    def curva_gauss(self,h):

        """
        Método para devolver el plot del ajuste de curva con el kernel Gaussiano.
        Recibe:
        -> h: valor de h para el kernel
        """

        try:
            self.plot(h,'gaussiano')
            
            
        except Exception as e:
            print(f"Error al graficar los datos{e}")
        

    def curva_tricube(self,h):

        """
        Método para devolver el plot del ajuste de curva con el kernel Tricube.
        Recibe:
        -> h: valor de h para el kernel
        """

        try:
            self.plot(h,'tricube')
            
        except Exception as e:
            print(f"Error al graficar los datos{e}")
        
            

    def curva_epanechnikov(self,h):
            
            """
            Método para devolver el plot del ajuste de curva con el kernel Epanechnikov.
            Recibe:
            -> h: valor de h para el kernel
            """
    
            try:
                self.plot(h,'epanechnikov')
                
                
            except Exception as e:
                print(f"Error al graficar los datos{e}")

    def plot_comparar(self,h):
        """
        Método para devolver el plot de los tres ajustes de curva.
        Recibe:
        -> h: valor de h para el kernel
        """

        try:
            y_gauss = self.curva(self.x,self.y,h,'gaussiano')
            y_tricube = self.curva(self.x,self.y,h,'tricube')
            y_epanechnikov = self.curva(self.x,self.y,h,'epanechnikov')
            plt.plot(self.x, self.y, label='Datos')
            plt.plot(self.x, y_gauss,label='Gauss')
            plt.plot(self.x, y_tricube,label='Tricube')
            plt.plot(self.x, y_epanechnikov,label='Epanechnikov')
            plt.title('Comparación de curvas suavizadas')
            plt.legend()
        except Exception as e:
            print(f"Error al graficar los datos{e}")
        else:
            plt.savefig(f'comparacion.png')  
            plt.close()
            