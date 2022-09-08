#coding utf-8

class Conta():
    num = 1011
    def __init__(self, tel):
        self.__numero = Conta.num
        self.__numero += 1
        self.__saldo = 0
        self.__tel = tel

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo

    def getTel(self):
        return self.__tel
    
    def setTel(self, tel):
        self.__tel = tel

    def sacar(self, valor:int):
        self.valor = int(input('Digite o valor: \n'))
    
    def sacar(self, valor:int):
        self.valor = int(input('Digite o valor: \n'))