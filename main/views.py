from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from django.utils.timezone import now

from .models import Restaurant, Menu, Vote
from .serializers import EmployeeSerializer, RestaurantSerializer, MenuSerializer, VoteSerializer


class EmployeeRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]


class RestaurantCRUDView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestaurantMenuView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetTodayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = now().date()
        return Menu.objects.filter(day=today)


class MenuVoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        employee = request.user
        menu_id = request.data.get("menu_id")

        if not menu_id:
            return Response({"error": "menu_id is required"}, status=400)

        try:
            menu = Menu.objects.get(id=menu_id)
        except Menu.DoesNotExist:
            return Response({"error": "Menu not found"}, status=404)

        if Vote.objects.filter(employee=employee, menu=menu).exists():
            return Response({"error": "Already voted for this menu"}, status=400)

        vote = Vote.objects.create(employee=employee, menu=menu)
        return Response({"message": "Voted"}, status=201)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def today_results(request):
    today = now().date()
    menus = Menu.objects.filter(day=today)
    result = {}

    for menu in menus:
        count = Vote.objects.filter(menu=menu).count()
        result[str(menu)] = count

    return Response(result)
