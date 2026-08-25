import uuid
from tools.fakers import get_random_email
from pydantic import BaseModel, Field, EmailStr, ValidationError, constr


class UserSchema(BaseModel):
    """
    Описание структуры модели данных пользователя.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры модели данных пользователя в запросе на создание пользователя.
    """
    email: EmailStr = get_random_email()
    password: constr(min_length=8)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры модели данных пользователя в ответе с данными созданного пользователя.
    """
    user: UserSchema


try:
    user = CreateUserRequestSchema(
        # email="user@example.com",
        password="Pass1234",
        lastName="Doe",
        firstName="John",
        middleName="Doe"
    )
    print(user)
except ValidationError as error:
    print(error)
