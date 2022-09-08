#coding utf-8
from conta import Conta

class titularPF(Conta):
    def __init__(self, tel:int, cnpj:int, nome:str, idade:int):
        super().__init__(tel)
        self.__nome = nome
        self.__idade = idade
        self.__cnpj = cnpj
    
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getCnpj(self):
        return self.__cnpj

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj