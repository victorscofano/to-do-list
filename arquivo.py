import json

# json.dump/load   -> arquivos
# json.dumps/loads -> strings

def salvar_tarefas(tarefas:list, caminho_arquivo:str):
    """
    salvar_tarefas serve para salvar a tarefa
    Deve-se considerar a lista de tarefas e o diretório do arquivo

    tarefas:
        lista de tarefas
    
    caminho_arquivo:
        string que contém o diretório do arquivo
    """
    try:
        # Abre o arquivo no modo escrita (w)
        # Se arquivo não existir, ele é criado
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            # json.dump pega a lista 'tarefas' e grava dentro de 'arquivo'
            # indent=4 serve para deixar o arquivo .json organizado e visual
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    # bloco de exceções com os erros
    except PermissionError: # erro de permissão de diretório
        print("Programa sem permissão do sistema para acessar a pasta/arquivo") 
    except OSError as erro: # erro de sistema (qualquer)
        print(f"Erro de sistema: {erro} | Nº {erro.errno} | Mensagem: {erro.strerror}")
    except Exception as erro: # qualquer outro tipo de erro
        print(f"Erro inesperado: {erro}")


def carregar_tarefas(caminho_arquivo: str):
    """
    carregar_tarefas serve para carregar as tarefas.
    Deve-se considerar o diretório do arquivo gerado.

    caminho_arquivo:
        string que contém o diretório do arquivo
    """
    try:
        # Abre o arquivo no modo leitura (r)
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            tarefas_salvas = json.load(arquivo)
        
        return tarefas_salvas
    # bloco de exceções
    except FileNotFoundError: # erro de arquivo inexistente
        print("Aviso: Arquivo não existe.")
        return []
    except json.JSONDecodeError as erro: # erro de conversão para json
        print(f"Falha ao decodificar JSON: {erro.msg}") # mensagem do erro
        print(f"Linha: {erro.lineno}, Coluna: {erro.colno}") # erro.lineno/colno identifica a linha/coluna do erro
        print(f"Posição do caractere: {erro.pos}") # índice exato do caractere problemático
        return []
    except PermissionError: # erro de permissão de diretório
        print("Programa sem permissão do sistema para acessar a pasta/arquivo")
        return []
    except OSError as erro: # erro de sistema (qualquer)
        print(f"Erro de sistema: {erro} | Nº {erro.errno} | Mensagem: {erro.strerror}")
        return []
    except Exception as erro: # qualquer outro tipo de erro
        print(f"Erro inesperado: {erro}")
        return []