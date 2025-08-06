# inforce_api

1. ¬становити Docker
2. «апустити проект:


    docker-compose up --build


3. «астосувати м≥грац≥њ:


    docker-compose run --rm web python manage.py makemigrations
    docker-compose run --rm web python manage.py migrate


“ести:

    docker-compose run --rm test



API:
POST /api/register/ Ч реЇстрац≥€
POST /api/token/ Ч лог≥н 
POST /api/restaurants/ Ч додати ресторан
POST /api/menus/ Ч додати меню
GET /api/today-menus/ Ч перегл€д меню на сьогодн≥
POST /api/vote/ Ч голосуванн€
GET /api/results/ - результати голосуванн€
