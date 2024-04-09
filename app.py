import os

restaurantes = ['pizza','xp']

def exibir_nome_do_programa():
    print("""Sabor MDA (MANTIOCA DO AMOR)
      """)

def exibir_opcoes():
 print("1)cadastrar restaurante")
 print("2)listar restaurante")
 print("3)ativar restaurante")
 print("4)sair")

def finaliza_app():
    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
    input('\n Digite a tecla "enter" para voltar ao menu principal')
    main()

opcao_escolhida = int(input("Escolha uma opção"))

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def escolher_opcao():

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finaliza_app()

def main():        #meu main é o rico
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

    if __name__ == '__main__':
        main()

        
