import os

restaurantes = [{'nome':'restaurante','categoria':'alimento','ativo':False},
                {'nome':'Santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'Sushi','ativo':False}]

def exibir_nome_do_programa():
 '''essa função é responsavel por dar nome ao programa
 '''
 print("""Sabor MDA(melhores da atualidade)
""")
def exibir_opcoes():
 '''essa função é responsavel por cadastrar, listar e ativar os restaurantes, e também sair
 '''
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')

def finaliza_app():
   '''essa função é responsavel por finalizar o aplicativo
   '''
   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
      '''essa função é responavel por voltar ao menu principal
      '''
      input('\n Digite a tecla "Enter" para voltar ao menu principal')
      main()

def opcao_invalida():
      '''essa função é responsavel por invalidar a opção 
      '''
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' essa função é responavel por limpar o programa
    '''
    os.system('clear') #os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   ''' essa função é responsavel por cadastrar um novo restaurante
   -input
   -nomerestaurante
   -categoria
   output:
   -adicionar um novo restaurante a lista de restaurantes
   '''
   exibir_subtitulo('Cadastro do novo restaurante:')
   nome_do_restaurante = input('Digite o nome do novo restaurante')
   categoria = input(f'Digite a categoria do resturante {nome_do_restaurante}:')
   dado_do_restarante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restarante)
   print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
    '''essa função é responavel por listar os restaurantes
    '''
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurante:
        nome_restaurante = restaurante['nome']
        categoria =  restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
def escolher_opcao():
 ''' essa função é responsavel por escolher as opções
 '''
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
       '''esa função é responsavel por ser o menu principal'''
       os.system('clear')
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcao()

       if __name__ == '__main__':
           main()