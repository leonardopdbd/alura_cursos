import os
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print("""

        
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
  
    """)

def exibir_opcoes():
    ''' Exibe as opções de menu para o usuário.

    Esta função imprime um menu de opções no console, permitindo ao usuário
    escolher entre diferentes ações disponíveis no sistema, como cadastrar
    restaurantes, listar restaurantes, alternar o estado de um restaurante
    ou sair do programa.

    Não há argumentos de entrada nem valores de retorno, pois a função
    apenas exibe as opções diretamente no console.'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():

    '''Finaliza a execução do aplicativo.

    Esta função exibe uma mensagem indicando que o aplicativo está sendo 
    finalizado, utilizando a função `exibir_subtitulo` para apresentar a 
    mensagem no formato de subtítulo.

    Não há argumentos de entrada nem valores de retorno, pois a função 
    apenas executa uma ação de exibição de mensagem.'''
    exibir_subtitulo('Finalizando o app\n')
    

def voltar_ao_menu_principal():

    '''Retorna ao menu principal do aplicativo.

    Esta função aguarda que o usuário pressione qualquer tecla para 
    continuar, e em seguida, chama a função `main()` para retornar ao 
    menu principal do aplicativo.

    Não há argumentos de entrada nem valores de retorno, pois a função 
    simplesmente pausa a execução até que o usuário interaja e, 
    posteriormente, chama a função `main()`.'''


    input('\nDigite uma tecla para voltar ao menu:')
    main()

def opcao_invalida():

    '''Informa ao usuário que a opção selecionada é inválida e retorna ao menu principal.

    Esta função exibe uma mensagem de erro indicando que a opção escolhida 
    pelo usuário não é válida. Após a exibição da mensagem, a função chama 
    `voltar_ao_menu_principal()` para permitir que o usuário retorne ao menu 
    principal do aplicativo.

    Não há argumentos de entrada nem valores de retorno, pois a função apenas 
    exibe uma mensagem e redireciona o fluxo para o menu principal.'''


    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):

    '''Exibe um subtítulo formatado no console.

    Esta função exibe o texto fornecido pelo usuário como um subtítulo, 
    formatado com uma borda de asteriscos acima e abaixo do texto. 
    A função também limpa a tela do console antes de exibir o subtítulo.

    Argumentos:
        texto (str): O texto a ser exibido como subtítulo. 

    Não há valor de retorno, pois a função apenas imprime o subtítulo 
    formatado diretamente no console.'''


    os.system('cls')
    linha = '*' * (len(texto)+ 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um  novo restauante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:

    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')



    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():

    '''Alterna o estado de atividade de um restaurante.

    Esta função permite ao usuário alterar o estado de um restaurante 
    específico, ativando-o ou desativando-o. O estado é invertido com base 
    no valor atual. Se o restaurante for encontrado, o novo estado é exibido 
    como uma mensagem de sucesso. Caso contrário, uma mensagem de erro é 
    exibida informando que o restaurante não foi encontrado.

    Não há argumentos de entrada na função, mas ela solicita ao usuário que 
    insira o nome do restaurante via `input`.

    A função não retorna nenhum valor, pois ela interage diretamente com o 
    usuário e modifica o estado de um restaurante na lista `restaurantes`. 
    Após a operação, o usuário é redirecionado ao menu principal.'''


    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()



    




def listar_restaurantes():

    '''Exibe uma lista de todos os restaurantes cadastrados.

    Esta função exibe no console uma tabela com os restaurantes cadastrados, 
    incluindo o nome, a categoria e o estado atual (ativado ou desativado) de 
    cada restaurante. A função formata a saída para que os dados sejam 
    apresentados de forma organizada, com colunas para o nome do restaurante, 
    a categoria e o status.

    Não há argumentos de entrada na função, pois ela utiliza a lista global 
    `restaurantes` para obter os dados a serem exibidos.

    A função não retorna nenhum valor, pois imprime diretamente a lista de 
    restaurantes no console. Após a exibição, o usuário é redirecionado ao 
    menu principal.'''



    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')


    voltar_ao_menu_principal()





def escolher_opcao():

    ''' Processa a opção escolhida pelo usuário e executa a ação correspondente.

    Esta função solicita ao usuário que escolha uma opção do menu, capturando 
    a entrada como um número inteiro. Dependendo da opção escolhida, a função 
    chama a função apropriada para executar a ação desejada, como cadastrar 
    um novo restaurante, listar restaurantes, alternar o estado de um 
    restaurante, ou finalizar o aplicativo.

    Se o usuário escolher uma opção inválida ou se houver algum erro ao 
    processar a entrada, a função `opcao_invalida()` é chamada, exibindo uma 
    mensagem de erro e retornando ao menu principal.

    Não há argumentos de entrada na função, mas ela solicita a entrada do 
    usuário via `input`. A função não retorna nenhum valor, pois o fluxo 
    continua com a execução da função correspondente à opção escolhida.'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:          
             alternar_estado_restaurante()            
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
        
        '''Função principal do aplicativo.

    Esta função é responsável por iniciar o aplicativo, limpando a tela do 
    console, exibindo o nome do programa, apresentando as opções disponíveis 
    para o usuário e processando a escolha do usuário.

    Passos realizados:
    1. Limpa a tela do console usando `os.system('cls')`.
    2. Exibe o nome do programa com a função `exibir_nome_do_programa()`.
    3. Exibe as opções de menu com a função `exibir_opcoes()`.
    4. Processa a escolha do usuário chamando a função `escolher_opcao()`.

    Não há argumentos de entrada nem valores de retorno. A função é executada 
    quando o módulo é executado diretamente, conforme indicado pela condição 
    `if __name__ == '__main__':`.'''


        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()
if __name__ == '__main__':
    main()
