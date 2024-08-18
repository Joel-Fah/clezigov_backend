from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserLoginForm
from django.utils.html import format_html


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('core:procedures')
    form_class = UserLoginForm
    authentication_form = UserLoginForm

    def get_success_url(self):
        return self.success_url or self.get_redirect_url()

    def form_valid(self, form):
        """If the form is valid, send a success message and log the user in."""
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30) # 30 days
        else:
            self.request.session.set_expiry(0) # session expires when the browser is closed

        login(self.request, form.get_user())
        message = format_html("You are successfully logged in.<br>Welcome back! ✌🏽")
        messages.success(self.request, message)
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, send an error message."""
        message = format_html("Invalid username or password.<br>Please try again.")
        messages.error(self.request, message)
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('auth:login')

    def dispatch(self, request, *args, **kwargs):
        message = format_html("You are successfully logged out.<br>See you soon! 👋🏽")
        messages.success(request, message)
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(TemplateView):
    template_name = 'auth/register.html'
