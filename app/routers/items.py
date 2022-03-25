from fastapi import APIRouter, Depends, HTTPException



router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_items():
    return "fake_items_db"


@router.get("/{item_id}")
async def read_item(item_id: str):
    return item_id