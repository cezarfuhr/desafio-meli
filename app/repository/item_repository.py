import json
import logging
from typing import Optional
from pathlib import Path

from app.models.item import Item

logger = logging.getLogger(__name__)


class ItemRepository:
    """
    Repositorio para acesso aos dados de itens.
    
    Esta classe e responsavel por carregar e buscar itens
    a partir do arquivo JSON que simula um banco de dados.
    """
    
    def __init__(self, data_file_path: str = "data/items.json"):
        """
        Inicializa o repositorio carregando os dados do arquivo JSON.
        
        Args:
            data_file_path: Caminho para o arquivo JSON com os dados dos itens
        """
        self.data_file_path = data_file_path
        self._items: dict[str, Item] = {}
        self._load_items()
    
    def _load_items(self) -> None:
        """
        Carrega os itens do arquivo JSON para memoria.
        """
        try:
            file_path = Path(self.data_file_path)
            
            if not file_path.exists():
                logger.warning(f"Data file not found: {self.data_file_path}")
                return
            
            with open(file_path, "r", encoding="utf-8") as file:
                items_data = json.load(file)
            
            self._items = {
                item_data["id"]: Item(**item_data) 
                for item_data in items_data
            }
            
            logger.info(f"Loaded {len(self._items)} items from {self.data_file_path}")
            
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.error(f"Error loading items from {self.data_file_path}: {e}")
            self._items = {}
    
    def find_by_id(self, item_id: str) -> Optional[Item]:
        """
        Busca um item pelo seu ID.
        
        Args:
            item_id: ID do item a ser buscado
            
        Returns:
            Item encontrado ou None se nao existir
        """
        logger.debug(f"Searching for item with ID: {item_id}")
        item = self._items.get(item_id)
        
        if item:
            logger.debug(f"Item found: {item.title}")
        else:
            logger.debug(f"Item not found for ID: {item_id}")
            
        return item