from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from .models import Tag, Procedure
from .serializers import TagSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProceduresView(LoginRequiredMixin, ListView):
    model = Procedure
    template_name = 'core/procedures.html'
    context_object_name = 'procedures'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class CommunityView(LoginRequiredMixin, TemplateView):
    template_name = 'core/community.html'


class CleziView(LoginRequiredMixin, TemplateView):
    template_name = 'core/clezi.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'


# ViewSets
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
