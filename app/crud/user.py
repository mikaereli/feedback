from app.crud.base import BaseCrud
from app.models.user import User

class UserCrud(BaseCrud):
    model = User
