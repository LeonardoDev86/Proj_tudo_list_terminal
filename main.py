from todo_list.funcoes import (
    validar_escolha, adicionar_tarefa,remover_tarefa,listar_tarefa,
    pausar,titulo,ler_tarefa,salvar_tarefa,limpar,confirmar_acao,validar_indice
)

def main():
    tarefas = ler_tarefa()
    opcoes = ['adicionar','listar','remover','sair']

    while True:
        limpar()
        titulo('GERENCIADOR DE TAREFAS')

        print('Selecione uma das opções:\n1 - Adicionar\n2 - Listar\n3 - Remover\n4 - Sair')

        opcao = input('\nDigite uma opção: ')
        escolha = validar_escolha(opcoes,opcao)

        if escolha is None:
            print(f'[ERRO]: Selecione opções entre 1 e {len(opcoes)}')
            pausar()
            continue

        if escolha == 'sair':
            print('Obrigado por utilizar nosso sistema.')
            print('Sessão encerrada!\n')
            break
        
        if escolha == 'adicionar':
            while True:
                limpar()
                titulo('ADICIONAR TAREFA\n')
                nova_tarefa = input('Digite a tarefa: ').strip()
                
                if adicionar_tarefa(tarefas,nova_tarefa):
                    salvar_tarefa(tarefas)
                    print('\nTarefa adicionada com sucesso!')   
                else:
                    print('\nERRO: Nenhuma tarefa digitada.')

                while True:    
                    resposta = input('\nDeseja adicionar mais tarefas? S/N: ').upper().strip()

                    confirma = confirmar_acao(resposta)
                    if confirma is not None:
                        break

                    print('\nPor favor digite "S" ou "N".')

                if not confirma:
                    break    
                

        elif escolha == 'remover':
            while True:
                limpar()
                titulo('REMOVER TAREFA')
                itens = listar_tarefa(tarefas)

                if not itens:
                    print('\nNenhuma tarefa à remover')
                    pausar()
                    break

                # Exibe a lista para o usuário se situar
                for item in itens:
                    print(item)
 
                indice = input('\nDigite o número da tarefa à remover ou "V" para voltar: ').strip().upper()
                if indice == 'V':
                    break

                ind = validar_indice(tarefas,indice)
                if ind is None:
                    print(f'\nERRO: Digite apenas números entre 1 e {len(tarefas)}') 
                    pausar()
                    continue  

                #------- Validação antes de remover a tarefa-------#
                limpar()
                print(f'\nTem certeza que deseja remover a tarefa "{tarefas[ind - 1]}"?')
                resposta = input('S/N: ').strip().upper()
                confirma = confirmar_acao(resposta)

                if confirma:
                    remover_tarefa(tarefas,ind)
                    salvar_tarefa(tarefas)
                    print('\nTarefa removida com sucesso!')
                    pausar()
                    break

                if confirma is False:
                    print('\nRemoção cancelada.')
                    pausar()
                    break
                else:
                    print('\nOpção inválida.')
                    pausar()   
                
        elif escolha == 'listar':
            limpar()
            titulo('LISTA DE TAREFAS')
            itens = listar_tarefa(tarefas)
            if itens:
                for item in itens:
                    print(item)
            else:
                print('\nNenhuma tarefa para listar')
            
            pausar()

if __name__ == '__main__':
    main()
