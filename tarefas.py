from datetime import datetime
from rich import print
from rich.panel import Panel

def adicionar_tarefa(tarefas:list, descricao):
    """
    adicionar_tarefa serve para adicionar uma tarefa nova à TO-DO LIST.
    Deve-se considerar a lista de tarefas e a descrição da mesma.

    tarefas:
        lista de tarefas
    
    descricao:
        string que captura a descrição da tarefa

    """

    proximo_id = max([u["id"] for u in tarefas], default=0) + 1
    hoje = datetime.now()
    # %Y = ano(4 dígitos), %m = mês, %d = dia
    # %H = hora, %M = minuto, %S = segundo
    hoje = hoje.strftime("%Y-%m-%d %H:%M:%S")

    # cria a tarefa (dict)
    nova_tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "status": False,
        "data_criacao": hoje
    }

    # adiciona a tarefa à lista de tarefas
    tarefas.append(nova_tarefa)

    return tarefas

def listar_tarefas(tarefas:list):
    """
    listar_tarefas serve para listar as tarefas existentes na TO-DO LIST.
    Deve-se considerar a lista de tarefas.

    tarefas:
        lista de tarefas

    Verifica se existe tarefa dentro da lista. 
        - Caso positivo: percorre a lista de tarefas e exibe para o usuário
        - Caso negativo: exibe mensagem informando ao usuário
    """
    # verifica se existe alguma tarefa cadastrada
    if not tarefas:
        print("[red]\nNenhuma tarefa cadastrada![/red]")
    else:
        # percorre a lista de tarefas e verifica o status de cada uma
        for tarefa in tarefas:
            if tarefa['status']:
                # concluido -> variável auxiliar para fazer o print customizável
                # com a bibli rich é passado [cor] texto [/cor]
                concluido = "[bold green]Status => Tarefa concluída[/bold green]"
            else:
                concluido = "[bold red]Status => Tarefa pendente[/bold red]"
            # também utiliza a bibli rich para customizar o print
            print(Panel.fit(f"Tarefa {tarefa['id']} => {tarefa['descricao']} | {concluido}"))

def concluir_tarefa(tarefas: list, id_tarefa):
    """
    concluir_tarefa serve para concluir uma tarefa da TO-DO LIST.
    Deve-se considerar a lista de tarefas e o id correspondente.

    tarefas:
        lista de tarefas

    id_tarefa:
        variável de controle do input do id da tarefa e é comparada com o campo 'id' contido na tarefa
    """
    # variável auxiliar que verifica se aquela tarefa foi encontrada
    # inicia como False e torna True após o loop encontrar o id da tarefa
    encontrado = False
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            encontrado = True
            tarefa['status'] = True # altera o status para True
            print(f"[bold green]Tarefa {tarefa['id']} => {tarefa['descricao']} => Concluída com sucesso![/bold green]")
            break

    if not encontrado:
        print("[bold yellow]id não encontrado.[/bold yellow]")

    return tarefas

def editar_tarefa(tarefas:list, id_tarefa, nova_descricao):
    """
    editar_tarefa serve para editar uma tarefa da TO-DO LIST.
    Deve-se considerar a lista de tarefas, o id e a nova descrição.

    tarefas:
        lista de tarefas
    
    id_tarefa:
        variável de controle do input do id da tarefa e é comparada com o campo 'id' contido na tarefa
    
    nova_descricao:
        variável que recebe o input da nova descrição digitada pelo usuário
    """

    encontrado = False
    # verifica se o usuário deixou a descrição vazia ou em branco
    if not nova_descricao:
        print("[red]impossível adicionar uma tarefa com descrição vazia.[red]")
        return tarefas

    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            encontrado = True
            tarefa['descricao'] = nova_descricao # a nova descrição substitui a antiga dentro da tarefa
            print(f"[blue]Tarefa {tarefa['id']} => Nova descrição: {tarefa['descricao']}[/blue]")
            break
    
    if not encontrado:
        print("[bold yellow]id não encontrado.[/bold yellow]")

    return tarefas

def remover_tarefa(tarefas:list, id_tarefa):
    """
    remover_tarefa serve para remover uma tarefa da TO-DO LIST.
    Deve-se considerar a lista de tarefas e o id correspondente.

    tarefas:
        lista de tarefas

    id_tarefa:
        variável de controle do input do id da tarefa e é comparada com o campo 'id' contido na tarefa.
        
    """
    encontrado = False

    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            encontrado = True
            print(f"[bright_yellow]Tarefa {id_tarefa} removida com sucesso.[/bright_yellow]")
            break
    
    if encontrado:
        tarefas.remove(tarefa)
    
    if not encontrado:
        print("[bold yellow]id não encontrado.[/bold yellow]")

    return tarefas