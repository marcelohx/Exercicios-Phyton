from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model() #Instanciando a classe model
        self.opcao = 0

    def mostrarMenu(self):
        print('Escolha uma das opções abaixo' +
             '\n1. Sair'                      +
             '\n2. Trocar'                    +
             '\n3. Tabuada'                   +
             '\n4. Media de Tres'             +
             '\n5. Exercicio Um'              +
            '\n6. Exercicio Dois'             +
            '\n7. Exercicio Tres'             +
            '\n8. Exercicio Quatro '          +
            '\n9. Exercicio Cinco'            +
            '\n10. Exercicio Seis'            +
            '\n11. Exercicio Sete'            +
            '\n12. Exercicio Oito'            +
            '\n13. Exercicio Nove'            +
            '\n14. Exercicio Dez'             +
            '\n15. Exercicio Onze'            +
            '\n16. Exercicio Doze'            +
            '\n17. Exercicio Treze'           +
            '\n18. Exercicio Quatorze'        +
            '\n19. Exercicio Quinze'          +
            '\n20. Exercicio Dezesseis'       +
            '\n21. Exercicio Dezessete'       +
            '\n22. Exercicio Dezoito'         +
            '\n23. Exercicio Dezenove'        +
            '\n24. Exercicio Vinte'           +
            '\n25. Exercicio Vinte Um' +
            '\n26. Exercicio Vinte Dois' +
            '\n27. Exercicio Vinte Tres' +
            '\n28. Exercicio Vinte Quatro' +
            '\n29. Exercicio Vinte Cinco' +
            '\n30. Exercicio Vinte Seis' +
            '\n31. Exercicio Vinte Sete' +
            '\n32. Exercicio Vinte Oito' +
            '\n33. Exercicio Vinte Nove' +
            '\n34. Exercicio Trinta' +
            '\n35. Exercicio Trinta Um' +
            '\n36. Exercicio Trinta Dois' +
            '\n37. Exercicio Trinta Tres' +
            '\n38. Exercicio Trinta Quatro' +
            '\n39. Exercicio Trinta Cinco' +
            '\n40. Exercicio Trinta Seis' +
            '\n41. Exercicio Trinta Sete' +
            '\n42. Exercicio Trinta Oito' +
            '\n43. Exercicio Trinta Nove' )


    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Informe um número: '))
            if self.opcao == 1:
                print('Obrigado!!! :)')
            elif self.opcao == 2:
                valorA = int(input('Informe um valor para A: '))
                valorB = int(input('Informe um valor para B: '))
                print(self.modelo.trocar(valorA,valorB))
            elif self.opcao == 3:
                num = int(input('Informe um número: '))
                print(self.modelo.tabuada(num))
            elif self.opcao == 4:
                nota1 =float(input('Primeira Nota: '))
                while(nota1 < 0 or nota1 > 10):
                    print('Erro, Informe uma nota entre 0 e 10')
                    nota1 = float(input('Primeira Nota: '))

                nota2 = float(input('Segunda Nota: '))
                while (nota2 < 0 or nota2 > 10):
                    print('Erro, Informe uma nota entre 0 e 10')
                    nota2 = float(input('Segunda Nota: '))

                nota3 = float(input('Terceira Nota: '))
                while (nota3 < 0 or nota3 > 10):
                    print('Erro, Informe uma nota entre 0 e 10')
                    nota3 = float(input('Terceira Nota: '))

                print(self.modelo.mediaTres(nota1,nota2,nota3))
            elif self.opcao == 5:
                print(self.modelo.exercicioUm())
            elif self.opcao == 6:
                print(self.modelo.exercicioDois())
            elif self.opcao == 7:
                print(self.modelo.exercicioTres())
            elif self.opcao == 8:
                print(self.modelo.exercicioQuatro())
            elif self.opcao == 9:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioCinco(num))
            elif self.opcao == 10:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioSeis(num))
            elif self.opcao == 11:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioSete(num))
            elif self.opcao == 12:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioOito(num))
            elif self.opcao == 13:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioNove(num))
            elif self.opcao == 14:
                print(self.modelo.exercicioDez())
            elif self.opcao == 15:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioOnze(num))
            elif self.opcao == 16:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDoze(num))
            elif self.opcao == 17:
                print(self.modelo.exercicioTreze())
            elif self.opcao == 18:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioQuatorze(num))
            elif self.opcao == 19:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioQuinze(num))
            elif self.opcao == 20:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDezesseis(num))
            elif self.opcao == 21:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDezessete(num))
            elif self.opcao == 22:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDezoito(num))
            elif self.opcao == 23:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioDezenove(num))
            elif self.opcao == 24:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioVinte(num))
            elif self.opcao == 25:
                valorA = int(input('Informe um valor para A: '))
                valorB = int(input('Informe um valor para B: '))
                print(self.modelo.exercicioVinteUm(valorA, valorB))
            elif self.opcao == 26:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioVinteDois(num))
            elif self.opcao == 27:
                base = int(input('Informe um valor para a base: '))
                altura = int(input('Informe um valor para a altura: '))
                print(self.modelo.exercicioVinteTres(base, altura))
            elif self.opcao == 28:
                dia = int(input('Informe dia : '))
                mes = int(input('Informe mes: '))
                ano = int(input('Informe ano: '))
                print(self.modelo.exercicioVinteQuatro(dia, mes, ano))
            elif self.opcao == 29:
                totalEleitores = int(input('Informe o total de eleitores : '))
                votosBrancos = int(input('Informe o total de votos branco: '))
                votosNulos = int(input('Informe o total de votos nulos: '))
                votosValidos = int(input('Informe o total de votos validos: '))
                print(self.modelo.exercicioVinteCinco(totalEleitores, votosBrancos, votosNulos, votosValidos))
            elif self.opcao == 30:
                salario = int(input('Informe um valor do salario: '))
                perReajuste = int(input('Informe a porcentagem do reajuste: '))
                print(self.modelo.exercicioVinteSeis(salario, perReajuste))
            elif self.opcao == 31:
                custoFabrica = int(input('Informe o custo de fabrica : '))
                print(self.modelo.exercicioVinteSete(custoFabrica))
            elif self.opcao == 32:
                notaUm = int(input('Informe a primeira nota: '))
                notaDois = int(input('Informe a segunda nota: '))
                notaTres = int(input('Informe a terceira nota: '))
                print(self.modelo.exercicioVinteOito(notaUm, notaDois, notaTres))
            elif self.opcao == 33:
                qtdeMaca = int(input('Informe a quantidade de maçã comprada: '))
                print(self.modelo.exercicioVinteNove(qtdeMaca))
            elif self.opcao == 35:
                salarioFixo = int(input('Informe o salario fixo: '))
                vendas = int(input('Informe o valor das vendas: '))
                print(self.modelo.exercicioTrintaUm(salarioFixo, vendas))
            elif self.opcao == 36:
                saldo = float(input('Informe o saldo em conta: '))
                debito = float(input('Informe os debitos: '))
                credito = float(input('Informe os creditos: '))
                print(self.modelo.exercicioTrintaDois(saldo, debito, credito))
            elif self.opcao == 37:
                num = int(input('Informe um número: '))
                print(self.modelo.exercicioTrintaTres(num))
            elif self.opcao == 38:
                print(self.modelo.exercicioTrintaQuatro())
            elif self.opcao == 39:
                print(self.modelo.exercicioTrintaCinco())
            elif self.opcao == 40:
                print(self.modelo.exercicioTrintaSeis())
            elif self.opcao == 41:
                qtde = int(input('Informe a quantidade de numeros: '))
                print(self.modelo.exercicioTrintaSete(qtde))
            elif self.opcao == 42:
                print(self.modelo.exercicioTrintaOito())
            elif self.opcao == 43:
                habitantes = int(input('Informe a quantidade de habitantes: '))
                print(self.modelo.exercicioTrintaNove(habitantes))
            else:
                print('Opção escolhida não é válida!')