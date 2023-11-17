import numpy as np
import matplotlib.pyplot as plt

class IsingCal:
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
    self.J  = 1                                                                         # Cste para material ferromagnetico
    self.Red = np.random.choice([-1, 1], size=(self.h, self.w))                         # Inicializa la red de spins en el lattice

    if Campo:                                                                           # Permite la presencia de un campo uniforme sobre el lattice
      self.B = Campo
    else:
      self.B = 0
            
    try:
      1/self.T
    except ZeroDivisionError:
      print("Temperatura no puede ser cero, no tendra resultados significativos")

  def RedIni(self):
    self.Red = np.random.choice([-1, 1], size=(self.h, self.w))                         # Inicializa la red de spins en el lattice

  def MCRed(self):
    """
    Realiza MC sobre la red para cambiar spines
    """
    for i in range(self.h):
      for j in range(self.w):
        n, m = np.random.randint(self.h), np.random.randint(self.w)
        vecinos = self.Red[(n+1)%self.h, m] + self.Red[(n-1)%self.h, m] + self.Red[n, (m+1)%self.w] + self.Red[n, (m-1)%self.w]
        e = -self.J * self.Red[n,m] * vecinos
        deconfig =  -2 * e                                                              # Diferencia de energia al cambiar de microestado
        if deconfig <= 0 or np.random.rand() < np.exp(-self.beta*deconfig):             # Condicion de aceptacion de config
          self.Red[n,m] *= -1

  def Emicro(self):
    """
    Calcula energia de microestado
    """
    self.MCRed()
    energy = 0
    for i in range(self.h):
      for j in range(self.w):
        vecinos = self.Red[(i+1)%self.h, j] + self.Red[(i-1)%self.h, j] + self.Red[i, (j+1)%self.w] + self.Red[i, (j-1)%self.w]
        energy  += -self.J * self.Red[i,j] * vecinos/4 - self.Red[i,j] * self.B
    return energy

  def Magnetizacion(self):
    """
    Calcula magnetizacion de microestado
    """
    mag = np.sum(self.Red)
    return mag

  def Actualizacion(self):
    """
    Actualiza la red y calcula todo pertinente al micro estado
    """
    a = 1/(self.N*self.w*self.h)                                                        # Normaliza sobre area y MC
    b = 1/(self.N*self.N*self.w*self.h)                                                 # Normaliza sobre area y MC dos veces
    self.Energy  = np.zeros(self.TN)
    self.Energy2 = np.zeros(self.TN)
    self.CV      = np.zeros(self.TN)
    self.Mag     = np.zeros(self.TN)
    for s in range(self.TN):                                                            # Moverse por temperaturas
      self.beta = 1 /(self.kb*self.t[s])                                                # Actualiza beta
      E  = 0
      E2 = 0
      M  = 0
      for n in range(self.N):                                                           # Moverse por microestados
        self.MCRed()
        e = self.Emicro()
        m = self.Magnetizacion()
        E  += e                                                                         # Suma de energia de microestados
        E2 += e*e                                                                       # Suma de cuadrado de energia de microestados
        M  += m                                                                         # Suma de magnetizacion de microestados

      self.Energy[s]  = E * a
      self.Energy2[s] = E2 
      self.CV[s]      = (E2*a  - (E**2)*b) / (self.t[s]**2)
      self.Mag[s]     = M * a
      
  def Run(self):
    """
    Corre lo pesado del codigo
    """
    self.Actualizacion()
    
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
    plt.scatter(self.t, self.Energy, marker = '.')
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