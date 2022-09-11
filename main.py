#coding utf-8

from conta import Conta
from titular import Titular
from titularpf import titularPF
from titularpj import titularPJ

if __name__ == '__main__':
    
    num = 0
    while num != 7:
        print('-=-='*15)
        print('Olá, seja bem vindo ao banco 644!')
        val = str(input('Deseja fazer o cadastro de uma nova conta(S/N)? ')).lower()
        
        if val == 's' or 'sim':
            ident = str(input('\nSua conta pertence a uma (pessoa), ou a uma (entidade)? \nEscolha uma das duas opções:\n')).lower()
            num2 = 0

            if ident == 'pessoa':
                nome_ = str(input('\nInsira seu nome: \n'))
                idade_ = str(input('Insira sua idade: \n'))
                id_ = str(input('Insira seu CPF: \n'))
                numero_ = str(input('Insira seu número: \n'))

                titular = titularPF(nome_, idade_, id_, numero_)

            elif ident == 'entidade':
                nome_ = str(input('\nInsira sua razão social: \n'))
                idade_ = str(input('Tempo de existência: \n'))
                id_ = str(input('Insira seu CNPJ: \n'))
                numero_ = str(input('Insira seu número: \n'))

                titular = titularPJ(nome_, idade_, id_, numero_)

            else:
                print('Erro, tente novamente.\n')
                num2 = 7

            while num2 != 7:
                print('\nOperações disponívei:')
                num3 = int(input('''
[1] Realizar Depósito
[2] Realizar um Saque
[3] Verificar o Saldo
[4] Realizar Transferência
[5] Solicitar Extrato
[6] Cadastrar nova conta
[7] Sair do Sistema
\n'''))
                if num3 == 1:
                    deposito = float(input('Valor a ser depositado: R$ '))
                    titular.getConta().depositar(deposito)
                    print(f'Seu saldo atualizado é de: \nR${titular.getConta().getSaldo()}')
                    opc = str(input('Deseja realizar mais alguma operação?(S/N)\n')).lower()
                    if opc == 's' or 'sim':
                        pass
                    elif opc == 'n' or 'nao' or 'não':
                        print('Tudo bem, tenha um bom dia! :)')
                        break
                    else:
                        print('Entrada inválida, tente novamente!')
                elif num3 == 2:
                    saque = float(input("Valor a ser sacado: R$"))
                    titular.getConta().sacar(saque)
                    print(f'Seu saldo atualizado é de: \nR${titular.getConta().getSaldo()}')
                    opc = str(input('Deseja realizar mais alguma operação?(S/N)\n')).lower()
                    if opc == 's' or 'sim':
                        pass
                    elif opc == 'n' or 'nao' or 'não':
                        print('Tudo bem, tenha um bom dia! :)')
                        num2 = 7
                        num = 7
                    else:
                        print('Entrada inválida, tente novamente!')
                elif num3 == 3:
                    print(f'Olá {titular.getNome()}')
                    print(f'Seu saldo disponível é de: \nR${titular.getConta().getSaldo()}')
                    opc = str(input('Deseja realizar mais alguma operação?(S/N)\n')).lower()
                    if opc == 's' or 'sim':
                        pass
                    elif opc == 'n' or 'nao' or 'não':
                        print('Tudo bem, tenha um bom dia! :)')
                        num2 = 7
                        num = 7
                    else:
                        print('Entrada inválida, tente novamente!')
                elif num3 == 4:
                    pass
                elif num3 == 5:
                    pass
                elif num3 == 6:
                    pass
                elif num3 == 7:
                    print('Tudo bem, tenha um bom dia! :)')
                    num = 7
                    num2 = num3
                else:
                    print('Erro de entrada, tente novamente!')

        elif val == 'n' or 'nao' or 'não':
            print('Tudo bem, tenha um bom dia! :)')
            num = 7

        else:
            print('Erro de entrada, tente novamente.')
            
        
        
        