from todo_list.funcoes import (
    validate_choice, add_task, remove_task, list_tasks,
    pause, title, read_tasks, save_tasks, clear, confirm_action, validate_index
)

def main():
    tasks = read_tasks()
    # As opções internas ficam em inglês para a lógica do backend
    options = ['add', 'list', 'remove', 'exit']

    while True:
        clear()
        title('GERENCIADOR DE TAREFAS')

        # A interface que o usuário vê continua em português
        print('Selecione uma das opções:\n1 - Adicionar\n2 - Listar\n3 - Remover\n4 - Sair')

        option = input('\nDigite uma opção: ')
        choice = validate_choice(options, option)

        if choice is None:
            print(f'[ERRO]: Selecione opções entre 1 e {len(options)}')
            pause()
            continue

        if choice == 'exit':
            print('Obrigado por utilizar nosso sistema.')
            print('Sessão encerrada!\n')
            break
        
        if choice == 'add':
            while True:
                clear()
                title('ADICIONAR TAREFA\n')
                new_task = input('Digite a tarefa: ').strip()
                
                if add_task(tasks, new_task):
                    save_tasks(tasks)
                    print('\nTarefa adicionada com sucesso!')   
                else:
                    print('\nERRO: Nenhuma tarefa digitada.')

                while True:    
                    resposta = input('\nDeseja adicionar mais tarefas? S/N: ').upper().strip()

                    confirmation = confirm_action(resposta)
                    if confirmation is not None:
                        break

                    print('\nPor favor digite "S" ou "N".')

                if not confirmation:
                    break    
                

        elif choice == 'remove':
            while True:
                clear()
                title('REMOVER TAREFA')
                items = list_tasks(tasks)

                if not items:
                    print('\nNenhuma tarefa para remover.')
                    pause()
                    break

                for item in items:
                    print(item)
 
                index_input = input('\nDigite o número da tarefa para remover ou "V" para voltar: ').strip().upper()
                if index_input == 'V':
                    break

                idx = validate_index(tasks, index_input)
                if idx is None:
                    print(f'\nERRO: Digite apenas números entre 1 e {len(tasks)}') 
                    pause()
                    continue  

                clear()
                print(f'\nTem certeza que deseja remover a tarefa "{tasks[idx - 1]}"?')
                resposta = input('S/N: ').strip().upper()
                confirmation = confirm_action(resposta)

                if confirmation:
                    remove_task(tasks, idx)
                    save_tasks(tasks)
                    print('\nTarefa removida com sucesso!')
                    pause()
                    break

                if confirmation is False:
                    print('\nRemoção cancelada.')
                    pause()
                    break
                else:
                    print('\nOpção inválida.')
                    pause()   
                
        elif choice == 'list':
            clear()
            title('LISTA DE TAREFAS')
            items = list_tasks(tasks)
            if items:
                for item in items:
                    print(item)
            else:
                print('\nNenhuma tarefa para listar.')
            
            pause()

if __name__ == '__main__':
    main()