from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=50)
    curso = forms.CharField(max_length=50)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label ="Email")
    first_name = forms.CharField(label ="Nombre")
    last_name = forms.CharField(label ="Apellido")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']
        help_texts = {k: "" for k in fields }

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder':'Username'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Last Name'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password'}))
    
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password']
        help_texts = {k: "" for k in fields }

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Old password'}))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'New password'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'New password confirmation'}))
    
    class Meta:
        model = User
        fields =['old_password','new_password1','new_password2']
        help_texts = {k: "" for k in fields }
    