import arquivo
import tarefas
import menu
import os
from rich import print
from rich.panel import Panel

# retorna a string concatenada no molde de diretório "data/dados.json" (linux) ou "data\dados.json" (windows)
caminho_arquivo = os.path.join("data", "dados.json") 
# cria o diretório "data/" caso ela já não exista; # exist_ok=True garante isso
os.makedirs("data", exist_ok=True)
# lê os arquivos json e carrega os dados na memória
lista_de_tarefas = arquivo.carregar_tarefas(caminho_arquivo)

while True:
    op = menu.exibir_menu()
    
    if op == 1:
        tarefa_descricao = input("Digite a descrição da tarefa: ")
        if tarefa_descricao == "":
            print("Impossível adicionar tarefa sem descrição.")
        else:
            tarefas.adicionar_tarefa(lista_de_tarefas, tarefa_descricao)
            print("Tarefa adicionada.")
    elif op == 2:
        tarefas.listar_tarefas(lista_de_tarefas)
    elif op == 3:
        tarefa_id = input("Digite o ID da tarefa que deseja concluir: ")
        try:
            tarefa_id = int(tarefa_id)
            tarefas.concluir_tarefa(lista_de_tarefas, tarefa_id)
        except ValueError:
            print("Id inválido.")
    elif op == 4:
        tarefa_id = input("Digite o ID da tarefa que deseja editar: ")
        try:
            tarefa_id = int(tarefa_id)
            tarefa_descricao = input("Digite a nova descrição: ")
            tarefas.editar_tarefa(lista_de_tarefas, tarefa_id, tarefa_descricao)
        except ValueError:
            print("Id inválido.")
    elif op == 5:
        tarefa_id = input("Digite o ID da tarefa que deseja remover: ")
        try:
            tarefa_id = int(tarefa_id)
            tarefas.remover_tarefa(lista_de_tarefas, tarefa_id)
        except ValueError:
            print("Id inválido.")
    elif op == 6:
        arquivo.salvar_tarefas(lista_de_tarefas, caminho_arquivo)
        print("[bold red]Saindo do sistema...[/bold red]")
        break
    else:
        print("Opção inválida.")
        continue
    # salva o arquivo
    arquivo.salvar_tarefas(lista_de_tarefas, caminho_arquivo)