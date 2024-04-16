import os

restaurantes = [{'nome':'restaurante','categoria':'alimento','ativo':False},
                {'nome':'Santa','categoria':'carne','ativo':True},
                {'nome';'CWB','categoria':'Sushi','ativo':False}]

def exibir_nome_do_programa():
 print("""Sabor MDA(melhores da atualidade)
""")
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')

def finaliza_app():
   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
      input('\n Digite a tecla "Enter" para voltar ao menu principal')
      main()

def opcao_invalida():
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear') #os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro do novo restaurante:')
   nome_do_restaurante = input('Digite o nome do novo restaurante')
   categoria = input(f'Digite a categoria do resturante {nome_do_restaurante}:')
   dado_do_restarante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restarante)
   print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurante:
        nome_restaurante = restaurante['nome']
        categoria =  restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
def escolher_opcao():
 try:
   opcao_escolhida = int(input('Escolha uma opção: '))

   if opcao_escolhida == 1:
     print('Cadastrar restaurante')
   elif opcao_escolhida == 2:
     print('Listar restaurantes')
   elif opcao_escolhida == 3:
     print('Ativar restaurantes')
   elif opcao_escolhida == 4:
      finaliza_app()
   else:
       opcao_invalida()
 except:
       opcao_invalida()

def main():
       os.system('clear')
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcao()

       if __name__ == '__main__':
           main()