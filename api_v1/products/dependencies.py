from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from . import crud

from fastapi import Depends

from core.models import db_helper, Product


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ) -> Product:
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")