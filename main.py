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
            
            if ident == 'pessoa':
                nome_ = str(input('\nInsira seu nome: '))
                idade_ = int(input('Insira sua idade: '))
                id_ = str(input('Insira seu CPF: '))
                numero_ = str(input('Insira seu número: '))

                titular = titularPF(nome_, idade_, id_, numero_)

            elif ident == 'entidade':
                nome_ = str(input('\nInsira sua razão social: '))
                idade_ = int(input('Insira seu tempo de existência: '))
                id_ = str(input('Insira seu CNPJ: '))
                numero_ = str(input('Insira seu número: '))

                titular = titularPJ(nome_, idade_, id_, numero_)

            else:
                print('Erro!')
                num = 7
                num2 = 7

            num2 = 0
            while num2 != 7:
                print('\nOperações disponíveis para realizar na conta:')
                num2 = int(input('''[1] Realizar Depósito
[2] Realizar um Saque
[3] Verificar o Saldo
[4] Realizar Transferência
[5] Solicitar Extrato
[6] Cadastrar nova conta
[7] Sair do Sistema\n'''))
                if num2 == 1:
                    deposito = float(input('Valor a ser depositado: R$'))
                    titular.getConta().depositar(deposito)
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
                elif num2 == 2:
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
                elif num2 == 3:
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
                elif num2 == 4:
                    pass
                elif num2 == 5:
                    pass
                elif num2 == 6:
                    pass
                elif num2 == 7:
                    print('Tudo bem, tenha um bom dia! :)')
                    num = 7
                else:
                    print('Erro de entrada, tente novamente!')

        elif val == 'n' or 'nao' or 'não':
            print('Tudo bem, tenha um bom dia! :)')
            num = 7

        else:
            print('Erro de entrada, tente novamente.')
            
        
        
        