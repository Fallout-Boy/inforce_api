# inforce_api

1. ���������� Docker
2. ��������� ������:


    docker-compose up --build


3. ����������� �������:


    docker-compose run --rm web python manage.py makemigrations
    docker-compose run --rm web python manage.py migrate


�����:

    docker-compose run --rm test



API:
POST /api/register/ � ���������
POST /api/token/ � ���� 
POST /api/restaurants/ � ������ ��������
POST /api/menus/ � ������ ����
GET /api/today-menus/ � �������� ���� �� �������
POST /api/vote/ � �����������
GET /api/results/ - ���������� �����������
