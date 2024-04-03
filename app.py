import os

print("""Sabor MDA (MANTIOCA DO AMOR)
      """)

print("1)cadastrar restaurante")
print("2)listar restaurante")
print("3)ativar restaurante")
print("4)sair")

opcao_escolhida = int(input("Escolha uma opção"))

def finaliza_app():
    os.system('clear')
    print("encerrando o programa\n")

if opcao_escolhida == 1:
    print('cadastrar retaurante')
elif opcao_escolhida == 2:
    print('listar restaurantes') 
elif opcao_escolhida == 3:
    print('Ativar restaurantes')
else:
    finaliza_app()


