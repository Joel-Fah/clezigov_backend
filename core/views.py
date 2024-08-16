from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer


# Create your views here.
class ProceduresView(TemplateView):
    template_name = 'core/procedures.html'


class CommunityView(TemplateView):
    template_name = 'core/community.html'


class CleziView(TemplateView):
    template_name = 'core/clezi.html'


class ProfileView(TemplateView):
    template_name = 'core/profile.html'


# ViewSets
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
