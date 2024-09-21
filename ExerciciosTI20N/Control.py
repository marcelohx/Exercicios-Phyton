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
            '\n24. Exercicio Vinte'           )

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
            else:
                print('Opção escolhida não é válida!')