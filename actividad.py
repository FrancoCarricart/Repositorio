class Cuenta:
    def __init__(self,titular,saldo=0.0):
        self.titular=titular
        self.__saldo=float(saldo)

    def mostrar(self):
        print( f"La cuenta esta a nombre de {self.titular} y actualmente tiene un saldo de {self.__saldo} pesos")
    
    def ingresar(self,cantidad):
        if type(cantidad)==float or type(cantidad)==int:
            if cantidad>=0:
                print(f"Ingresando {cantidad} pesos a la cuenta")
                self.__saldo+=cantidad
            else:
                print("No se puede agregar una cantidad negativa de plata a la cuenta")
        else:
            print("Debe ingresar una cantidad numerica")

    def retirar(self,cantidad):
        if type(cantidad)==float or type(cantidad)==int:
            if cantidad>=0:
                print(f"Retirando {cantidad} pesos de la cuenta")
                self.__saldo-=cantidad
            else:
                print("No se puede retirar una cantidad negativa de plata de la cuenta")
        else:
            print("Debe ingresar una cantidad numerica")
Franco=Cuenta("Franco Carricart")
Franco.mostrar()
Franco.ingresar("3")
Franco.ingresar(100.87231312)
Franco.retirar(200)
Franco.retirar(400200)
Franco.mostrar()
