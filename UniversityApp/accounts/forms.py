from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from UniversityApp.accounts.models import Profile
from UniversityApp.mixins import PlaceholderMixin, DisabledFieldsMixin

User = get_user_model()     # get User model


class UserRegisterForm(PlaceholderMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')


class UserEditForm(UserChangeForm):     # for admin
    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user", "course", "is_lector",)
        labels = {
            'first_name': '',
            'last_name': '',
            'personal_image': '',
            'biography': '',
            'age': '',
        }


class ProfileCreateOrEditForm(PlaceholderMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        help_texts = {
            'first_name': 'This field is required!',
            'age': 'Age must be at least 5.',
        }


class ProfileDeleteForm(DisabledFieldsMixin, forms.ModelForm):
    disabled_fields_set = ('first_name', 'last_name',)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',)
