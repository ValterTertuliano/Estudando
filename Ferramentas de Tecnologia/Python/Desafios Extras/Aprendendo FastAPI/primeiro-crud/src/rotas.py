from fastapi import FastAPI
from src.dados import menu
from fastapi import Path
from typing import Optional
from pydantic import BaseModel  # Importa a classe BaseModel para criar a classe Item

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define a classe Item com os campos id, name e price
class Item(BaseModel):
    """
    Classe para representar um item no menu.
    
    Atributos:
    id (int): Identificador único do item.
    name (str): Nome do item.
    price (float): Preço do item.
    """
    id: int
    name: str
    price: float

# Define um endpoint GET para buscar um item pelo seu ID
@app.get("/get-item/{item_id}")
def get_item(
    item_id: int = Path(
        description="Preencha com o ID do item que deseja visualizar"
    ),
):
    """
    Recupera um item do menu pelo seu ID.

    Args:
        item_id (int): O ID do item a ser recuperado.

    Returns:
        dict: Retorna o item encontrado ou uma mensagem de erro.
    """
    # Filtra o menu para encontrar o item com o ID fornecido
    search = list(filter(lambda x: x["id"] == item_id, menu))

    # Se não encontrar o item, retorna um erro
    if search == []:
        return {"Erro": "Item não existe"}

    # Se encontrar o item, retorna o item encontrado
    return {"Item": search[0]}


# Define um endpoint GET para buscar um item pelo nome
@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    """
    Recupera um item do menu pelo seu nome.

    Args:
        name (str, optional): O nome do item a ser recuperado. Caso não seja fornecido, retorna todos os itens.

    Returns:
        dict: Retorna o item encontrado ou uma mensagem de erro.
    """
    # Filtra o menu para encontrar o item com o nome fornecido
    search = list(filter(lambda x: x["name"] == name, menu))

    # Se não encontrar o item, retorna uma mensagem de erro
    if search == []:
        return {"item": "Não existe"}
    
    return {'Item': search[0]}

# Define um endpoint GET para listar todos os itens do menu
@app.get('/list-menu')
def list_menu():
    """
    Recupera todos os itens do menu.

    Returns:
        dict: Retorna a lista de todos os itens no menu.
    """
    return {'Menu': menu}


# Define um endpoint POST para criar um novo item no menu
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    """
    Cria um novo item no menu.

    Args:
        item_id (int): O ID do novo item.
        item (Item): O objeto que contém as informações do novo item.

    Returns:
        dict: Retorna o item criado ou uma mensagem de erro.
    """
    # Filtra o menu para verificar se já existe um item com o ID fornecido
    search = list(filter(lambda x: x["id"] == item_id, menu))

    # Se o item já existir, retorna um erro
    if search != []:
        return {'Erro': 'Item já existe'}

    # Converte o objeto item para um dicionário e adiciona o ID fornecido
    item = item.dict()
    item['id'] = item_id

    # Adiciona o item ao menu
    menu.append(item)
    return item


# Define um endpoint PUT para atualizar um item existente no menu
@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: Item):
    """
    Atualiza um item existente no menu.

    Args:
        item_id (int): O ID do item a ser atualizado.
        item (Item): O objeto com os novos dados para o item.

    Returns:
        dict: Retorna o item atualizado ou uma mensagem de erro.
    """
    # Filtra o menu para verificar se o item existe
    search = list(filter(lambda x: x["id"] == item_id, menu))

    # Se o item não existir, retorna uma mensagem de erro
    if search == []:
        return {'Item': 'Não existe'}

    # Atualiza o nome do item se fornecido
    if item.name is not None:
        search[0]['name'] = item.name

    # Atualiza o preço do item se fornecido
    if item.price is not None:
        search[0]['price'] = item.price

    return search


# Define um endpoint DELETE para excluir um item do menu
@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):
    """
    Exclui um item do menu.

    Args:
        item_id (int): O ID do item a ser excluído.

    Returns:
        dict: Retorna uma mensagem de sucesso ou erro.
    """
    # Filtra o menu para verificar se o item existe
    search = list(filter(lambda x: x["id"] == item_id, menu))

    # Se o item não existir, retorna uma mensagem de erro
    if search == []:
        return {'Item': 'Não existe'}

    # Remove o item do menu
    for i in range(len(menu)):
        if menu[i]['id'] == item_id:
            del menu[i]
            break

    return {'Mensagem': 'Item excluído com sucesso'}
