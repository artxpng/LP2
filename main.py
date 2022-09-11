#coding utf-8

from conta import Conta
from titular import Titular
from titularpf import titularPF

if __name__ == '__main__':
    
    nome_ = str(input('Insira seu nome: '))
    idade_ = int(input('Insira sua idade: '))
    cpf_ = str(input('Insira seu CPF: '))
    numero_ = str(input('Insira seu número: '))

    titular = titularPF(nome_, idade_, cpf_, numero_)

    print(f'Olá {titular.getNome()}')
    print(f'Seu saldo disponível é de: R${titular.getConta().getSaldo()}')
    
    deposito = float(input('Valor a ser depositado: R$'))
    titular.getConta().depositar(deposito)
    print(f'Seu saldo atualizado é de: R${titular.getConta().getSaldo()}')
    
    saque = float(input("Valor a ser sacado: R$"))
    titular.getConta().sacar(saque)
    print(f'Seu saldo atualizado é de: R${titular.getConta().getSaldo()}')