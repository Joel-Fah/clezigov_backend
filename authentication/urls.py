from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView

# Create your urls here
urlpatterns = [
    # path('accounts/login/', UserLoginView.as_view(), name='account_login'),
    # path('accounts/logout/', UserLogoutView.as_view(), name='account_logout'),
    # path('accounts/register/', UserRegisterView.as_view(), name='account_signup'),
]
