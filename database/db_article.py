from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from database.models import DbArticle
from fastapi.exceptions import HTTPException
from fastapi import status



def create_article(db:Session, request:ArticleBase):
    article = DbArticle(title = request.title,
                        content = request.content,
                        published = request.published,
                        user_id = request.creator_id,
                        )

    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(id:int, db:Session):
    artilce = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not artilce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"article with id {id} not found !")

    return artilce
