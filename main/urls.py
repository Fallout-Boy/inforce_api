from django.urls import path

from .views import EmployeeRegistrationView, RestaurantCRUDView, RestaurantMenuView, GetTodayMenuView, MenuVoteView, today_results

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', EmployeeRegistrationView.as_view(), name='register'),
    path('restaurants/', RestaurantCRUDView.as_view(), name='create-restaurant'),
    path('menus/', RestaurantMenuView.as_view(), name='create-menu'),
    path('today-menus/', GetTodayMenuView.as_view(), name='today-menus'),
    path('vote/', MenuVoteView.as_view(), name='vote'),
    path('results/', today_results, name='results'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
