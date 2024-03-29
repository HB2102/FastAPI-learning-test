from sqlalchemy.orm.session import Session
from schemas import UserBase
from database.models import DbUser
from database.hash import Hash
from exeptions import EmailNotValid


def create_user(db: Session, request: UserBase):
    if '@' not in request.email:
        raise EmailNotValid('Email Not Valid')

    user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(DbUser).all()



def get_user(id,db: Session):
    return db.query(DbUser).filter(DbUser.id == id).first()


def get_user_username(username,db: Session):
    return db.query(DbUser).filter(DbUser.username == username).first()


def delete_user(id, db: Session):
    user = get_user(id, db)
    db.delete(user)
    db.commit()
    return 'User deleted'

def update_user(id, db:Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password),
    })
    db.commit()

    return "User updated"

