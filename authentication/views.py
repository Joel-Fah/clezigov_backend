from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from allauth.account.views import LoginView, LogoutView, SignupView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegisterForm
from django.utils.html import format_html
from core.models import Category


# Create your views here.
class UserLoginView(LoginView):
    def form_valid(self, form):
        """If the form is valid, send a success message and log the user in."""
        response = super().form_valid(form)
        remember_me = form.cleaned_data['remember_me']
        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
        else:
            self.request.session.set_expiry(0)  # session expires when the browser is closed
        message = format_html("You are successfully logged in.<br>Welcome back! ✌🏽")
        messages.success(self.request, message)
        return response

    def form_invalid(self, form):
        """If the form is invalid, send an error message."""
        response = super().form_invalid(form)
        message = format_html("Invalid username or password.<br>Please try again.")
        messages.error(self.request, message)
        return response


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        message = format_html("You are successfully logged out.<br>See you soon! 👋🏽")
        messages.success(request, message)
        return response


class UserRegisterView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            format_html(
                'Welcome, <strong>{}</strong>! Your account has been created successfully.<br><a href="{}" '
                'class="font-bold underline">Go to your profile</a>',
                self.object.username,
                reverse_lazy('core:profile')
            )
        )
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request,
            format_html(
                'An error occurred while creating your account.<br>Please try again.'
            )
        )
        return response
