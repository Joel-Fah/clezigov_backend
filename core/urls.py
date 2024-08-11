from django.urls import path
from .views import ProceduresView, CommunityView, CleziView, ProfileView

# Create your urls here
app_name = 'core'

urlpatterns = [
    path('', ProceduresView.as_view(), name='procedures'),
    path('community/', CommunityView.as_view(), name='community'),
    path('clezi/', CleziView.as_view(), name='clezi'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
