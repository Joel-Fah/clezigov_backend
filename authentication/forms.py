from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.core.validators import EmailValidator


# Create your forms here
class UserLoginForm(AuthenticationForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'credential',
                'name': 'credential',
                'placeholder': 'name@clezigov.com or clezi_gov',
                'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 border-slate-600 placeholder-slate-400 '
                         'text-white focus:ring-primaryColor focus:border-primaryColor',
            },
        ),
        label='Email address or username',
        help_text='Please enter your registered username or email address.',
        error_messages={
            'required': 'Please enter your username or email address',
            'invalid_login': "Please enter a correct email/username and password."
        },
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Password',
                'class': 'rounded-xl block w-full ps-10 p-2.5 bg-slate-700 border-slate-600 placeholder-slate-400 '
                         'text-white focus:ring-primaryColor focus:border-primaryColor',
            },
        ),
        label='Password',
        help_text='Enter your password.',
        error_messages={
            'required': 'Please enter your password',
        },
        required=True,
    )

    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'id': 'remember',
                'name': 'remember',
                'class': 'w-4 h-4 border rounded-md focus:ring-3 bg-slate-700 border-slate-600 '
                         'focus:ring-primaryColor ring-offset-slate-800 focus:ring-offset-slate-800',
            },
        ),
        label='Remember Me?',
        help_text='Whether you want to keep your session active or not.',
        required=False,
    )

    # make is_Active field not required
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['remember_me'].required = False
        self.fields['remember_me'].default = True
        self.fields['username'].required = False

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
            'remember_me',
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password.")
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class RegisterForm(ModelForm):
    pass
