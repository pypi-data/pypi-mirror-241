
import numpy as np
class operacion:
    """ 
    Clase operacion 
    """

    def __init__(self, a, b):
        """
        Constructor de la clase operacion
        """
        self.a = a
        self.b = b
    
    def suma(self):
        """
        Metodo que suma dos numeros
        """
        return self.a + self.b

class prueba:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b
    

class dados:
    """Clase dados"""
    def __init__(self,N_dados,suma,n):
        self.N_dados = N_dados
        self.suma = suma
        self.n = n

    def lanzar_dados(self):
        """
        Metodo que simula el lanzamiento de N_dados
        """
        lanzamiento = np.random.randint(1,7,(self.n,self.N_dados))
        return lanzamiento
    

    def prob_dados(self):
        """
        Metodo que calcula la probabilidad de que la suma de los dados sea igual a suma
        """

        if self.suma < self.N_dados or self.suma > self.N_dados*6:
            return print("EL valor a evaluar debe ser mayor a la suma de los dados y menor a 6 veces la suma de los dados")
        lanzamiento = self.lanzar_dados()
        suma = np.sum(lanzamiento, axis=1)
        casos = np.sum(suma == self.suma)/self.n
        return casos
    

    # if suma < n_dados or suma > n_dados*6:
    #     return print("EL valor a evaluar debe ser mayor a la suma de los dados y menor a 6 veces la suma de los dados")
    # for i in range(n_dados):
    #     d  = np.random.randint(1,7,(n,n_dados))
    #     d = np.sum(d, axis=1)
    #     casos = np.sum(d == suma)/n
    #     return casos
    