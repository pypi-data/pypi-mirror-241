import numpy as np
import matplotlib.pyplot as plt

class dados:
    def __init__(self,N,cantdidadDados,numeroDeseado=7):
        self.N=N
        self.NN=numeroDeseado
        self.d=cantdidadDados

    def suma(self):
        numeros=np.random.randint(1,7,(self.d,self.N))
        return np.sum(numeros,0)
    
    def plot(self):
        x,y=self.histo()
        plt.hist(self.suma(),len(x),density=True)
        plt.savefig('plot')
        return 'plot.png'
    
    def probSuma(self):
        if self.NN < self.d or self.NN > self.d*6:
            return "El valor de la suma no es posible"
        for i in range(self.d):
            d=self.suma()
            casos = np.sum(d == self.NN)/self.N
            return casos
        
        return casos