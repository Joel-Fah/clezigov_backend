from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProceduresView(TemplateView):
    template_name = 'core/procedures.html'


class CommunityView(TemplateView):
    template_name = 'core/community.html'


class CleziView(TemplateView):
    template_name = 'core/clezi.html'


class ProfileView(TemplateView):
    template_name = 'core/profile.html'
