import json
import os

#-------------------------AÇÕES----------------------------#

def add_task(lista, tarefa): 
    tarefa = tarefa.strip()

    if not tarefa:
        return False
    
    lista.append(tarefa)
    return True

       
def list_tasks(lista):

    if not lista:
        return False
    
    return [f'{i} - {item}'for i,item in enumerate(lista, start = 1)]
        

def remove_task(lista, opcao_validada): 
    
    if opcao_validada:
        lista.pop(opcao_validada - 1) # pop remove o índice da lista
        return True

    return False

#---------------------PERSISTÊNCIA----------------------#
    
def read_tasks():
    try:
        with open('tarefas.json','r', encoding = 'utf-8') as t:
            return json.load(t)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


   
def save_tasks(tarefas):
    with open('tarefas.json', 'w', encoding = 'utf-8') as t:
        json.dump(tarefas, t,indent = 4 ,ensure_ascii = False)

#---------------------VALIDAÇÃO-------------------------#

def validate_choice(opcoes, opcao):
    try: 
        opcao = int(opcao)
        if 1 <= opcao <= len(opcoes):
            return opcoes[opcao - 1]
        
    except (ValueError,TypeError):
        pass
    
    return None
    

def validate_index(lista,indice):
    try: 
        indice = int(indice)
        if 1 <= indice <= len(lista):
            return indice
        
    except (ValueError,TypeError):
        pass 
    
    return None



def confirm_action(entrada): 
    entrada = entrada.strip().upper()
    if entrada == 'N':
        return False
    
    if entrada == 'S':
        return True
    
    return None

#--------------------INTERFACE--------------------#
      
def pause():
    entrada = input('\nPressione ENTER para continuar...')

        


def title(texto):
    print('='*50)
    print(texto.center(50))
    print('='*50)
    print()


def clear():
    os.system('cls' if os.name =='nt' else 'clear')
