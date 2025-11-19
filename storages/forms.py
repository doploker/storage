from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UploadedFile


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'введите пароль'
            }
        )
    )

    password2 = forms.CharField(
        label='повторный пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'повторите пароль'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'введите имя'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'введите email'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'введите имя'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'введите фамилию'
                }
            )
        }

class LoginUser(forms.Form):
    username = forms.CharField(
        label='имя пользователя',
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class UploadedFileForm(forms.ModelForm):
    class Meta:

        model = UploadedFile
        fields = ('name', 'file')
        widgets = {
            'file' : forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            )
        }