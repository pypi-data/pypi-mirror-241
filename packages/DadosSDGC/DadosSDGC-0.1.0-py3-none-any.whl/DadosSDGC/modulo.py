import numpy as np

class Dados:
    def __init__(self, NumeroDados, NumeroIteraciones, suma):
        """
        NumeroDados        : dados a tirar para sumar
        Numero Iteraciones : iteraciones de tirada de dados
        suma               : valor de suma del cual queremos conocer la probabilidad 
        """
        self.d = NumeroDados
        self.n = NumeroIteraciones
        self.s = suma
        if self.s < self.d:
            print('No puedes obtener una suma menor al numero de dados elegidos, el resultado obtenido no tiene sentido')
        if self.s <= 0:
            print('Como vas a querer obtener 0 sin 0 dados, o un valor negativo, no jodas')
        if self.s > self.d * 6:
            print('Los valores posibles a obtener son solamente aquellos menores al numero de dados por el numero de caras')
        
    def Arreglo(self):
        """ 
        Genera un arreglo de las tiradas de dados
        """
        self.A = np.random.randint(1,7,[self.d, self.n])

    def Sumas(self):
        """ 
         Suma cada instancia de tiradas
        """
        self.Arreglo()
        self.S = np.zeros(self.n)
        for i in range(self.n):
            self.S[i]=(self.A[:,i]).sum()
    
    def ValorDeseado(self):
        """
        Proporciona al usuario la probabilidad de sacar el valor deseado
        """
        self.Sumas()
        self.valor = np.count_nonzero(self.S == self.s)
        self.Prob = (self.valor / self.S.size) * 100
        print("La suma {} aparece un {}% de las veces que se suman {} dados".format(self.s, self.Prob, self.d))