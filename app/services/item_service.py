import logging
from typing import Optional

from app.models.item import Item
from app.repository.item_repository import ItemRepository

logger = logging.getLogger(__name__)


class ItemNotFoundException(Exception):
    """
    Excecao lancada quando um item nao e encontrado.
    
    Esta excecao e usada na camada de servico para indicar
    que um item solicitado nao existe no sistema.
    """
    
    def __init__(self, item_id: str):
        self.item_id = item_id
        super().__init__(f"Item with ID '{item_id}' not found")


class ItemService:
    """
    Servico responsavel pela logica de negocio relacionada a itens.
    
    Esta classe atua como intermediaria entre a camada de API
    e a camada de acesso a dados, implementando a logica de negocio.
    """
    
    def __init__(self, item_repository: Optional[ItemRepository] = None):
        """
        Inicializa o servico com um repositorio de itens.
        
        Args:
            item_repository: Repositorio para acesso aos dados dos itens.
                           Se nao fornecido, sera criado um novo.
        """
        self.item_repository = item_repository or ItemRepository()
    
    def get_item_by_id(self, item_id: str) -> Item:
        """
        Busca um item pelo ID.
        
        Args:
            item_id: ID do item a ser buscado
            
        Returns:
            Item encontrado
            
        Raises:
            ItemNotFoundException: Quando o item nao e encontrado
        """
        logger.info(f"Searching for item with ID: {item_id}")
        
        item = self.item_repository.find_by_id(item_id)
        
        if item is None:
            logger.warning(f"Item not found: {item_id}")
            raise ItemNotFoundException(item_id)
        
        logger.info(f"Item found: {item.title} (ID: {item_id})")
        return item