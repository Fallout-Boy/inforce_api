# inforce_api

1. Install Docker

2. Run the project:


    docker-compose up --build


3. Apply migrations:


    docker-compose run --rm web python manage.py makemigrations
    docker-compose run --rm web python manage.py migrate


Tests:

    docker-compose run --rm test


API:
- POST /api/register/ — registration
- POST /api/token/ — login
- POST /api/restaurants/ — add a restaurant
- POST /api/menus/ — add a menu
- GET /api/today-menus/ — view today's menus
- POST /api/vote/ — vote
- GET /api/results/ — voting results
