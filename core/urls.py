from django.urls import path, include
from .views import ProceduresView, CommunityView, CleziView, ProfileView
from rest_framework.routers import DefaultRouter
from .views import TagViewSet

# Create your urls here
app_name = 'core'
router = DefaultRouter()
router.register('tags', TagViewSet)

urlpatterns = [
    path('', ProceduresView.as_view(), name='procedures'),
    path('community/', CommunityView.as_view(), name='community'),
    path('clezi/', CleziView.as_view(), name='clezi'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/', include(router.urls))
]
