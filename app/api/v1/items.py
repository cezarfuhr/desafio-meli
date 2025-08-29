import logging
from fastapi import APIRouter, Depends, status

from app.models.item import Item, ItemCreateModel
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


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(
    item_data: ItemCreateModel,
    item_service: ItemService = Depends(get_item_service)
) -> Item:
    """
    Cria um novo item.
    
    Args:
        item_data: Dados do novo item a ser criado
        item_service: Servico injetado para logica de negocio
        
    Returns:
        Item criado com ID gerado
    """
    logger.info(f"POST /items requested - title: {item_data.title}")
    return item_service.create_item(item_data)