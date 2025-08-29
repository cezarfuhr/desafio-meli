from pydantic import BaseModel


class Item(BaseModel):
    """
    Modelo que representa um item do catalogo.
    
    Attributes:
        id: Identificador unico do item
        title: Titulo/nome do item
        price: Preco do item
        currency_id: Codigo da moeda (ex: 'BRL', 'USD')
        description: Descricao detalhada do item
        condition: Condicao do item ('new', 'used', etc.)
    """
    id: str
    title: str
    price: float
    currency_id: str
    description: str
    condition: str


class ItemCreateModel(BaseModel):
    """
    Modelo para criacao de novos itens.
    
    Contem todos os campos de Item exceto o 'id',
    que sera gerado automaticamente pelo sistema.
    """
    title: str
    price: float
    currency_id: str
    description: str
    condition: str