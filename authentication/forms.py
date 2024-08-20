from django.db import transaction
from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import EmailValidator, RegexValidator
from allauth.account.forms import LoginForm, SignupForm

from authentication.models import Profile


# Create your forms here
class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # login field
        self.fields['login'].widget.attrs.update({
            'id': 'credential',
            'name': 'credential',
            'placeholder': 'name@clezigov.com or clezi_gov',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['login'].label = 'Email address or username'
        self.fields['login'].help_text = 'Please enter your registered username or email address.'
        self.fields['login'].error_messages = {
            'required': 'Please enter your username or email address',
            'invalid_login': "Please enter a correct email/username and password."
        }
        self.fields['login'].required = True

        # password field
        self.fields['password'].widget.attrs.update({
            'id': 'password',
            'name': 'password',
            'placeholder': 'Password',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['password'].label = 'Password'
        self.fields['password'].help_text = 'Enter your password.'
        self.fields['password'].error_messages = {
            'required': 'Please enter your password',
        }
        self.fields['password'].required = True


class UserRegisterForm(SignupForm):
    # add first name field
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'name': 'first_name',
                'placeholder': 'How should we call you?',
                'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                         'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                         'transition-all duration-300 ease-in-out',
            }
        ),
        label='Your name(s)',
        help_text='Enter your name.',
        error_messages={'required': 'Please enter your name'},
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # email
        self.fields['email'].widget.attrs.update({
            'id': 'email',
            'name': 'email',
            'placeholder': 'name@clezigov.com',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['email'].label = 'Email address'
        self.fields['email'].help_text = 'Please enter your email address.'
        self.fields['email'].error_messages = {
            'required': 'Please enter your email address',
            'invalid': 'Enter a valid email address.',
            'unique': 'A user with that email already exists.',
        }
        self.fields['email'].required = True

        # username
        self.fields['username'].widget.attrs.update({
            'id': 'username',
            'name': 'username',
            'placeholder': 'user__name',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['username'].label = 'Set a username'
        self.fields['username'].help_text = 'Enter your username.'
        self.fields['username'].error_messages = {
            'required': 'Please enter your username',
            'invalid': 'Enter a valid username with letters, numbers, ".", and "_"',
            'unique': 'A user with that username already exists.',
        }
        self.fields['username'].required = True

        # password1
        self.fields['password1'].widget.attrs.update({
            'id': 'password1',
            'name': 'password1',
            'placeholder': 'Password',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['password1'].label = 'Create a password'
        self.fields['password1'].help_text = 'Enter your password.'
        self.fields['password1'].error_messages = {
            'required': 'Please enter your password',
        }
        self.fields['password1'].required = True

        # password2
        self.fields['password2'].widget.attrs.update({
            'id': 'password2',
            'name': 'password2',
            'placeholder': 'Re-enter password',
            'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 hover:bg-slate-600 border-slate-600 '
                     'placeholder-slate-400 text-white focus:ring-primaryColor focus:border-primaryColor '
                     'transition-all duration-300 ease-in-out',
        })
        self.fields['password2'].label = 'Confirm password'
        self.fields['password2'].help_text = 'Re-enter your password.'
        self.fields['password2'].error_messages = {
            'required': 'Please re-enter your password to confirm',
        }
        self.fields['password2'].required = True

    @transaction.atomic
    def save(self, request):
        user = super(UserRegisterForm, self).save(request)
        Profile.objects.create(user=user)
        return user
