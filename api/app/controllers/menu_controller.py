from fastapi import APIRouter, HttpStatus
from fastapi.responses import JSONResponse

from api.app.models.menu import Menu
from api.app.schemas.menu_schema import MenuCreateSchema, MenuUpdateSchema
#from api.app.schemas.menu_schema import MenuCreateSchema, MenuUpdateSchema

router = APIRouter()


@router.get("/menu")
async def get_menu_items():
    menu_items = await Menu.all()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"menu": menu_items},
    )


@router.post("/menu")
async def create_menu_item(menu_item: MenuCreateSchema):
    menu_item = await Menu.create(**menu_item.dict(exclude_unset=True))
    return JSONResponse(
        status_code=HttpStatus.CREATED,
        content={"menu_item": menu_item},
    )


@router.patch("/menu/{id}")
async def update_menu_item(id: int, menu_item: MenuUpdateSchema):
    menu_item_orm = await Menu.get_or_none(id=id)
    if not menu_item_orm:
        return JSONResponse(
            status_code=HttpStatus.NOT_FOUND,
            content={"detail": f"Menu item with id {id} not found"},
        )

    await menu_item_orm.update(**menu_item.dict(exclude_unset=True)).apply()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"menu_item": menu_item_orm},
    )


@router.delete("/menu/{id}")
async def delete_menu_item(id: int):
    menu_item_orm = await Menu.get_or_none(id=id)
    if not menu_item_orm:
        return JSONResponse(
            status_code=HttpStatus.NOT_FOUND,
            content={"detail": f"Menu item with id {id} not found"},
        )

    await menu_item_orm.delete()
    return JSONResponse(
        status_code=HttpStatus.OK,
        content={"deleted_id": id},
    )