from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from UniversityApp.accounts.models import Profile
from UniversityApp.mixins import PlaceholderMixin

User = get_user_model()     # get User model


class UserRegisterForm(PlaceholderMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

        # widgets = {
        #     'email': forms.EmailInput(attrs={'id': "email",}),
        #     'password1': forms.PasswordInput(attrs={'id': "password1"}),
        #     'password2': forms.PasswordInput(attrs={'id': "password2"}),
        # }
        # labels = {
        #     'username': "Email",
        #     'password1': "Password",
        #     'password2': "Repeat password",
        # }


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)
