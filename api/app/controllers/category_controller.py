from fastapi import APIRouter, HttpStatus
from fastapi.responses import JSONResponse

from app.models.category import Category
from app.schemas.category_schema import CategoryCreateSchema, CategoryUpdateSchema


router = APIRouter()


@router.get("/category")
async def get_categories():
    categories = await Category.all()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"categories": categories},
    )


@router.post("/category")
async def create_category(category: CategoryCreateSchema):
    category_orm = await Category.create(**category.dict(exclude_unset=True))
    return JSONResponse(
        status_code=HttpStatus.CREATED,
        content={"category": category_orm},
    )


@router.patch("/category/{id}")
async def update_category(id: int, category: CategoryUpdateSchema):
    category_orm = await Category.get_or_none(id=id)
    if not category_orm:
        return JSONResponse(
            status_code=HttpStatus.NOT_FOUND,
            content={"detail": f"Category with id {id} not found"},
        )

    await category_orm.update(**category.dict(exclude_unset=True)).apply()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"category": category_orm},
    )


@router.delete("/category/{id}")
async def delete_category(id: int):
    category_orm = await Category.get_or_none(id=id)
    if not category_orm:
        return JSONResponse(
            status_code=HttpStatus.NOT_FOUND,
            content={"detail": f"Category with id {id} not found"},
        )

    await category_orm.delete()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"deleted_id": id},
    )