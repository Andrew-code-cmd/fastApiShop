# FastAPI Shop 

Учебный pet-проект интернет-магазина с каталогом товаров, фильтрами и корзиной

---

<img width="1957" height="1355" alt="Screenshot From 2026-07-12 16-03-35" src="https://github.com/user-attachments/assets/6e73848b-b8fb-4172-ba11-f9f594e2b344" />
<img width="1732" height="1112" alt="Screenshot From 2026-07-12 16-04-15" src="https://github.com/user-attachments/assets/b098e267-6a3c-466b-a3db-c8413735e787" />
<img width="1732" height="1112" alt="Screenshot From 2026-07-12 16-04-41" src="https://github.com/user-attachments/assets/457a8893-14f0-4b33-aaee-8eebb88762cf" />


##  Возможности

- Каталог товаров с пагинацией
- Фильтрация товаров по категориям
- Корзина товаров
- Быстрый отзывчивый интерфейс на Vue 3 + TailwindCSS

---

## Стек

| Слой              | Технологии                              |
|-------------------|------------------------------------------|
| Backend           | FastAPI, Pydantic, SQLAlchemy            |
| Frontend          | Vue 3, Vite, Pinia, Vue Router |
| Стили             | TailwindCSS                              |
| База данных       | SQLite

---

## Запуск

**Backend:**

```bash
cd backend
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

## Основные эндпоинты API

| Метод | Путь                     | Описание                          |
|-------|--------------------------|------------------------------------|
| GET   | `/api/products`          | Список товаров          |
| GET   | `/api/products/category/{category_id}`     | Получить продукты по категории     |
| GET   | `/api/categories`        | Список категорий                   |
| GET   | `/api/cart`              | Получить содержимое корзины        |
| POST  | `/api/cart/add`        | Добавить товар в корзину           |
| PUT | `/api/cart/update`   | Изменить количество товара         |
| DELETE| `/api/cart/remove/{product_id}`   | Удалить товар из корзины           |

Полная интерактивная документация доступна по адресу `/api/docs` (Swagger UI) после запуска backend.

---

## Фронтенд

- **Vue 3 Composition API** — вся логика компонентов вынесена в `<script setup>`
- **Pinia** — хранение состояния корзины и списка товаров
- **Vue Router** — навигация между страницами каталога, карточкой товара и корзиной
- **TailwindCSS** — утилитарные классы для быстрой и адаптивной вёрстки
