#coding utf-8
from titular import Titular

class titularPF(Titular):
    def __init__(self, nome:str, idade:int, cnpj:int, tel:int):
        super().__init__(nome, idade, cnpj, tel)
    
    def getCnpj(self):
        return self.getDoc()

    def setCnpj(self, cnpj):
        self.setDoc(cnpj) 