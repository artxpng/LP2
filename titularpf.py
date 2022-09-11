#coding utf-8
from titular import Titular

class titularPF(Titular):
    def __init__(self, nome:str, idade:int, cpf:int, tel:int):
        super().__init__(nome, idade, cpf, tel)
    
    def getCpf(self):
        return self.getDoc()

    def setCpf(self, cpf):
        self.setDoc(cpf) 
 