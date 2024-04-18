def gravar_receita():
    nome = input("Escreva o Titulo das receita:")
    ingredientes = []
    while True:
        ingrediente = input("Digite os ingredientes (ou 'fim' para parar):")
        if ingrediente.lower() == 'fim':
            break
        ingredientes.append(ingrediente)


    modo_de_preparo = input("Digite o modo de preparo:")


    with open("receitas.txt","a") as arquivo:
        arquivo.write("Nome da receita:", nome + "\n" "\n")

        arquivo.write("Ingredientes: \n")
        for i in range(0,len(ingredientes)):
            arquivo.write(ingredientes[i] + "\n""\n")

        arquivo.write("Modo de preparo: \n")
        arquivo.write(modo_de_preparo + "\n")


def Achar_receita(nome):
    with open("receitas.txt", "r") as arquivo:
        encontrada = False
        for linha in arquivo:

            if linha.strip() == nome:
                encontrada = True
                print(linha.strip())  
                print("Ingredientes:")

                for linha in arquivo:
                    if linha.strip() == "Modo de preparo:":
                        break
                    print("-", linha.strip())  
                print("\nModo de preparo:")

                for linha in arquivo:
                    if linha.strip() == "":
                        break
                    print(linha.strip())  

                break
        if not encontrada:
            print("Receita não encontrada.")



def Listar_Receita():
    with open("receitas.txt", "r") as arquivo:
        print(arquivo.read())

def Limpar_Receitas():
    with open("receitas.txt", "w") as arquivo:
        arquivo.write('')






while True:
    opcao = input("Menu:\n1. Criar receita\n2. Listar receitas\n3. Consultar receita\n4. Limpar Arquivo\n5. sair \n.")
    if opcao == "1":
        gravar_receita()
    elif opcao == "2":
        Listar_Receita()
    elif opcao == "3":
        nome = input("Digite o nome da receita que deseja encontrar: ")
        Achar_receita(nome)
    elif opcao == "4":
        Limpar_Receitas()
    elif opcao == "5":
        print("Programa finalizado, obrigado! - Murilo Schittino 3 periodo UniAcademia")
        break
    else:
        print("Opcao invalida. Tente novamente.")