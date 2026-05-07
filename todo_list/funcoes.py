import json
import os

#-------------------------AÇÕES----------------------------#

def adicionar_tarefa(lista, tarefa): 
    tarefa = tarefa.strip()

    if not tarefa:
        return False
    
    lista.append(tarefa)
    return True

       
def listar_tarefa(lista):

    if not lista:
        return False
    
    return [f'{i} - {item}'for i,item in enumerate(lista, start = 1)]
        

def remover_tarefa(lista, opcao_validada): 
    
    if opcao_validada:
        lista.pop(opcao_validada - 1) # pop remove o índice da lista
        return True

    return False

#---------------------PERSISTÊNCIA----------------------#
    
def ler_tarefa():
    try:
        with open('tarefas.json','r', encoding = 'utf-8') as t:
            return json.load(t)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


   
def salvar_tarefa(tarefas):
    with open('tarefas.json', 'w', encoding = 'utf-8') as t:
        json.dump(tarefas, t,indent = 4 ,ensure_ascii = False)

#---------------------VALIDAÇÃO-------------------------#

def validar_escolha(opcoes, opcao):
    try: 
        opcao = int(opcao)
        if 1 <= opcao <= len(opcoes):
            return opcoes[opcao - 1]
        
    except (ValueError,TypeError):
        pass
    
    return None
    

def validar_indice(lista,indice):
    try: 
        indice = int(indice)
        if 1 <= indice <= len(lista):
            return indice
        
    except (ValueError,TypeError):
        pass 
    
    return None



def confirmar_acao(entrada): 
    entrada = entrada.strip().upper()
    if entrada == 'N':
        return False
    
    if entrada == 'S':
        return True
    
    return None

#--------------------INTERFACE--------------------#
      
def pausar():
    entrada = input('\nPressione ENTER para continuar...')

        


def titulo(texto):
    print('='*50)
    print(texto.center(50))
    print('='*50)
    print()


def limpar():
    os.system('cls' if os.name =='nt' else 'clear')
