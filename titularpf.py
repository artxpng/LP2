#coding utf-8
from conta import Conta

class titularPF(Conta):
    def __init__(self, tel:int, cpf:int, nome:str, idade:int):
        super().__init__(tel)
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getCpf(self):
        return self.__cpf

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setCpf(self, cpf):
        self.__cpf = cpf
