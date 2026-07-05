from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse


''' Описываем параметры валидации для полей  '''


class ProductBase(BaseModel):
    name: str = Field( ..., min_length=1, max_length=200,
                      description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field( ..., gt=0,
                          description="Product price(must be greater than zero)")
    category_id: int = Field( ..., description='Category ID')
    image_url: Optional[str] = Field(None, description='Product image URL')


class ProductCreate(ProductBase):
    pass


class ProductResponse(BaseModel): # определяет то, как мы будем видеть получаемую из API информацию
    id: int = Field( ..., description="Unique product ID")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field( ..., description="Product category details")

    class Config:
        form_attributes = True


class ProductListResponse(BaseModel): # тут определяем поля, выводимые в общем списке товаров
    products: list[ProductResponse]
    total: int = Field( ..., description='total number of products')