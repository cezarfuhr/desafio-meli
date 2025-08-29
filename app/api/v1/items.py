import logging
from fastapi import APIRouter, Depends

from app.models.item import Item
from app.services.item_service import ItemService

logger = logging.getLogger(__name__)

router = APIRouter()


def get_item_service() -> ItemService:
    """
    Dependencia que fornece uma instancia do ItemService.
    
    Returns:
        Instancia configurada do ItemService
    """
    return ItemService()


@router.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(
    item_id: str,
    item_service: ItemService = Depends(get_item_service)
) -> Item:
    """
    Busca um item pelo seu ID.
    
    Args:
        item_id: ID unico do item a ser buscado
        item_service: Servico injetado para logica de negocio
        
    Returns:
        Detalhes do item encontrado
        
    Raises:
        HTTPException: 404 se o item nao for encontrado
    """
    logger.info(f"GET /items/{item_id} requested")
    return item_service.get_item_by_id(item_id)