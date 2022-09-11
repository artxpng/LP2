from conta import Conta

class Titular:
    def __init__(self, nome:str, idade:int, doc:str, tel:str):
        self.__nome = nome
        self.__idade = idade
        self.__doc = doc
        self.__tel = tel
        self.__conta = Conta()

    def getConta(self):
        return self.__conta

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getDoc(self):
        return self.__doc
    
    def getTelefone(self):
        return self.__tel

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setDoc(self, doc):
        self.__doc = doc

    def setTelefone(self, telefone):
        self.__tel = telefone 
