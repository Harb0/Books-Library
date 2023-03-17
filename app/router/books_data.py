from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import models
from ..schema import book_data
from typing import List


router = APIRouter(
    # prefix=['/book'],
    tags= ['Create Book']
)

@router.post('/create_new_book', status_code=status.HTTP_201_CREATED, response_model=book_data.BookOut)
def create_new_book(add: book_data.CreateBook, db: Session = Depends(get_db)):

    add_new = models.Library_Book(**add.dict())
    db.add(add_new)
    db.commit()
    db.refresh(add_new)

    return add_new

@router.get('/all_books', status_code=status.HTTP_200_OK, response_model=List[book_data.BookOut])
def all_books(db: Session = Depends(get_db)):

    get_book = db.query(models.Library_Book).all()

    return get_book


@router.get('/book_by{id}', status_code=status.HTTP_200_OK, response_model=book_data.BookOut)
def book_by_id(id: str, db: Session = Depends(get_db)):

    get_book = db.query(models.Library_Book).filter(models.Library_Book.id == id).first()

    return get_book


@router.put('/update_by{id}', status_code=status.HTTP_200_OK)
def update_by_id(id: str, add: book_data.CreateBook, db: Session = Depends(get_db)):

    get_book = db.query(models.Library_Book).filter(models.Library_Book.id == id)

    check = get_book.first()

    if not check:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"Status": False, "message": f"this id is not find{id}"})

    get_book.update(add.dict(), synchronize_session=False)
    db.commit()

    return {"status": True, "message": "Successfully Updated book"}

# Delete a book

@router.put('/delete_by{id}', status_code=status.HTTP_200_OK)
def delete_by_id(id: str, db: Session = Depends(get_db)):

    get_book = db.query(models.Library_Book).filter(models.Library_Book.id == id)

    check = get_book.first()

    if not check:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"Status": False, "message": f"this id is not find{id}"})

    get_book.delete(synchronize_session=False)
    db.commit()

    return {"status": True, "message": "Successfully Deleted book"}