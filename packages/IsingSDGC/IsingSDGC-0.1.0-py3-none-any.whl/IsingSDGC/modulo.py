import numpy as np
import matplotlib.pyplot as plt

class IsingCal5:
    def __init__(self, NumIter, NumIterTemp, Ancho, Alto, Tempfinal, Campo=False):
        """ 
        NumIter         : Numero de iteraciones de MC para estimacion de funcion de particion
        NumIterTemp     : Numero de valores intermedios a evaluar la temperatura
        Ancho           : Ancho de la red
        Alto            : Alto de la red
        Tempfinal       : Temperatura maxima a la cual se evalua el sistema
        Campo           : Opcionalmente se toma en cuenta un campo externo
        """
        self.N  = NumIter
        self.TN = NumIterTemp
        self.w  = Ancho
        self.h  = Alto
        self.T  = Tempfinal
        self.t  = np.linspace(1, self.T, self.TN)
        self.kb = 1 # 0.001987204
        self.J  = 1                                                           # Cste para material ferromagnetico
        self.Red = np.random.choice([-1, 1], size=(self.h, self.w))           # Inicializa la red de spins en el lattice
        #self.Red = np.ones((self.h, self.w))

        if Campo:                                                             # Permite la presencia de un campo uniforme sobre el lattice
            self.B = Campo
        else:
            self.B = 0
            
        try:
            1/self.T
        except ZeroDivisionError:
            print("Temperatura no puede ser cero, no tendra resultados significativos")

    def IniRed(self):                                                                                                       # Siempre da la red inicial
        """ 
        Inicializa la red igual siempre 
        """
        np.random.seed(42)
        self.Red = np.random.choice([-1,1],size=(self.h, self.w))
        #self.Red = np.ones((self.h, self.w))

    def Mostro(self):
        """ 
        Itera por temperatura, por microestados, y las dos dimensiones de la red para calcular todas las caracteristicas deseadas
        """
        econfig = 0
        deconfig = 0
        self.CV    = np.zeros(self.TN)
        self.Eprom = np.zeros(self.TN)
        self.Mag   = np.zeros(self.TN)
        for s in range(self.TN):                                                                         # Mueve por temperaturas
            self.IniRed()                                                                                # Reinicia la red al estado original
            beta = 1/(self.kb * self.t[s])
            E2prom    = np.zeros(self.N)
            Eprom2    = np.zeros(self.N)
            Mag       = np.zeros(self.N) 
            for k in range(self.N):                                                                      # Mueve por microestados
                n, m = np.random.randint(self.h), np.random.randint(self.w)
                econfig = 0
                deconfig = 0                                                  
                for i in range(self.h):                                                                  # Mueve por alto
                    for j in range(self.w):                                                              # Mueve por ancho
                        vecinos = self.Red[(i+1)%self.h, j] + self.Red[(i-1)%self.h, j] + self.Red[i, (j+1)%self.w] + self.Red[i, (j-1)%self.w]
                        econfig += (-self.J * self.Red[i,j] * vecinos)/2 - self.B * self.Red[i,j]        # Contando cada interaccion 1 vez
                        if i==n and j==m:
                            e = -self.J * self.Red[n,m] * vecinos                                                
                E2prom[k]    = econfig**2                                                                # Calcula E2prom del microestado
                Eprom2[k]    = -econfig                                                                  # Calcula Eprom del microestado
                Mag[k]       = np.sum(self.Red)                                                          # Calcula la magnetizacion del microestado

                deconfig = 2 * e                                                                         # Diferencia de energia al cambiar de microestado
                if deconfig < 0 or np.random.rand() < np.exp(-beta*deconfig):                            # Condicion de aceptacion de config
                    self.Red[n,m] *= -1
            E2promCompleta    = np.mean(E2prom)                                                          # Para la temperatura calcula E2promedio
            Eprom2Completa    = np.mean(Eprom2)**2                                                       # Para la temperatura calcula Epromedio**2
            self.CV[s]        = E2promCompleta - Eprom2Completa                                          # Calor específico en temperatura s
            self.Eprom[s]     = np.mean(Eprom2)                                                          # Calcula energia promedio a la temperatura s
            self.Mag[s]       = np.mean(Mag)                                                             # Calcula magnetizacion promedio a la temperatura s

    def Calcular(self):
        self.Mostro()

    def GraphCV(self):
        """ 
        Grafica la capacidad calorifica contra la temperatura
        """
        plt.scatter(self.t, self.CV, marker = '.')
        plt.title('T vs Cv')
        plt.xlabel('Temperatura')
        plt.ylabel('Cv')
        plt.show()

    def GraphE(self):
        """ 
        Grafica la capacidad calorifica contra la temperatura
        """
        plt.scatter(self.t, self.Eprom, marker = '.')
        plt.title('T vs Eprom')
        plt.xlabel('Temperatura')
        plt.ylabel('Eprom')
        plt.show()

    def GraphM(self):
        """ 
        Grafica la capacidad calorifica contra la temperatura
        """
        plt.scatter(self.t, self.Mag, marker = '.')
        plt.title('T vs M')
        plt.xlabel('Temperatura')
        plt.ylabel('Magnetizacion')
        plt.show()