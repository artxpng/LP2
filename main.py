#coding utf-8

from titularpf import titularPF

if __name__ == '__main__':
    arthur = titularPF('Arthur', 20, '123456', '(75) 8888-9999')

    saque = float(input("..."))
    arthur.getConta().sacar(saque)