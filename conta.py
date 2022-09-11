#coding utf-8

class Conta():
    num = 1011
    def __init__(self):
        self.__numero = Conta.num
        Conta.num += 1
        self.__saldo = 0

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo

    def sacar(self, valor:float):
        if valor > 0 and valor >= self.__saldo:
            print('Valor indisponível')
        
        elif valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            
        else:
            print('Entrada não reconhecida!')
    
    def depositar(self, valor:float):
        if valor > 0:
            self.__saldo += valor
        
        elif valor <= 0:
            print('Erro\nO valor inserido é inválido!')
        
        else:
            print('Entrada não reconhecida!') 