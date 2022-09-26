#coding utf-8

from conta import Conta
from titular import Titular
from titularpf import titularPF
from titularpj import titularPJ
import json
import jsonpickle

if __name__ == '__main__':
    lista = []

    arquivo = open('bg.json', 'r')
    entrada = json.load(arquivo)
    arquivo.close()
    lista = jsonpickle.decode(entrada)

#    for item in entrada:
#        obj = jsonpickle.decode(item)
#        lista.append(obj)

    print('-=-='*25)
    print('Olá, seja bem vindo ao banco 644!')
    
    #criação de conta
    while True:    
        opcao = input('Deseja Cadastrar uma nova conta? [S/N]').lower()
        
        if opcao == 'n':
            break
        
        elif opcao == 's':
            variavel = input('Titular: Pessoa jurídica ou física? [PF/PJ]').lower()
        
        else:
            print('Entrada inválida! Tente novamente')
        
        if variavel == 'pf':
            nome = input('Nome: ').capitalize()
            idade = int(input("Idade: "))
            doc = int(input("CPF: "))
            tel = int(input("Telefone: "))
        
        elif variavel == 'pj':
            nome = input("Razão Social: ").capitalize()
            idade = int(input("Tempo de Criação: "))
            doc = int(input("CNPJ: "))
            tel = int(input("Telefone: "))

        titular = Titular(nome, idade, doc, tel)
        lista.append(titular)
    
    print('-=-='*25)
    while True:
        print('''
Menu Bancário
[1] Realizar Depósito
[2] Realizar um Saque
[3] Verificar o Saldo
[4] Realizar Transferência
[5] Solicitar Extrato
[6] Sair do Sistema\n
        ''')
        opc = int(input('Sua opção: '))
        print('-=-='*25)
        if opc == 6:
            saida = jsonpickle.encode(lista)
            arquivo = open('bg.json', 'w')
            json.dump(saida,arquivo)
            arquivo.close()

            break	

        if opc == 1:
            destino = int(input('Qual o documento da conta para depósito? '))
            busca = True
            for pessoa in lista:
                if pessoa.getDoc() == destino:
                    busca = False
                    valor = float(input('Qual valor a depositar? R$ '))
                    pessoa.getConta().depositar(valor)
            if busca:
                print('Conta não encontrada. Tente novamente!')

        if opc == 2:
            saque = int(input('Qual o documento da conta para saque? '))
            busca = True
            for pessoa in lista:
                if pessoa.getDoc() == saque:
                    busca = False
                    print(f'Seu saldo atual é: R$ {pessoa.getConta().getSaldo()}')
                    valor = float(input('Qual valor a sacar? '))
                    pessoa.getConta().sacar(valor)
            if busca:
                print('Conta não encontrada. Tente novamente!')

        if opc == 3:
            destino = int(input('Qual o documento da conta? '))
            busca = True
            for pessoa in lista:
                if pessoa.getDoc() == destino:
                    busca = False
                    print(f"Saldo: R$ {pessoa.getConta().getSaldo()}")

                if busca:
                    print('Conta não encontrada. Tente novamente!')

        if opc == 4:
            origem = int(input('Qual o documento da conta de origem? '))
            destino = int(input('Qual o documento da conta para transferir? '))
            busca = True
            valor = float(input('Qual valor a transferir? R$ '))
            for pessoa_orig in lista:
                if pessoa_orig.getDoc() == origem:
                    busca = False
                    print(f'Seu saldo atual é: R$ {pessoa_orig.getConta().getSaldo()}')
                    break
                    
            for pessoa_dest in lista:
                if pessoa_dest.getDoc() == destino:
                    busca = False
                    break
            if busca:
                print('Conta não encontrada. Tente novamente!')

            else:
                if pessoa_orig.getConta().getSaldo() >= valor:
                    pessoa_orig.getConta().sacar(valor)
                    pessoa_dest.getConta().depositar(valor)
                    print(f'Foi transferido para a conta do titular {pessoa_dest.getNome()} o valor de R$ {valor} reais.')
                
                else:
                    print('Transferência não sucedida! ')
#            print('Área de transferências em manutenção, sentimos muito pelo inconveniente!\n')
#            print('-=-='*25)

        if opc == 5:
            print("Extrato!")
            ext = int(input("Qual o documento da Conta: "))
            busca = True
            for pessoa in lista:
                if pessoa.getDoc() == ext:
                    busca = False
                    print(f"Saldo: R$ {pessoa.getConta().getSaldo()}")
                    print("Esse é seu Histórico: ")
                    if len(pessoa.getConta().getExtrato()) == 0:
                            print("     ----------------------")
                    else:
                        for n in pessoa.getConta().getExtrato():
                            if n[0] == "Depósito":
                                print(f"- \tDepósito de R$ {n[1]}")
                            elif n[0] == "Saque":
                                print(f"- \tSaque de R$ {n[1]}")
            if busca:
                print("Conta destino não encontrada. Tente novamente!")
    
for pessoa in lista:
    print(f'Nº da conta: {pessoa.getConta().getNumero()}\tDoc: {pessoa.getDoc()}\tCliente: {pessoa.getNome()}\t\tTelefone: {pessoa.getTelefone()}\t\t Saldo:{pessoa.getConta().getSaldo()}')
#
#    #pergunta qual cliente deseja ver na lista, apartir do doc
#    documento = int(input('Qual o documento do cliente que deseja buscar? '))
#
#    for pessoa in lista:
#        if pessoa.getDoc() == documento:
#            print(f'Cliente: {pessoa.getNome()}')
#        else:
#            print('Documento não encontrado!')

    
