from django.contrib.auth import get_user_model
from UniversityApp.accounts.forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from UniversityApp.accounts.models import Profile


class UserRegisterPage(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')


class UserLoginPage(LoginView):
    template_name = 'registration/login.html'


class ProfileDetailsPage(generic.DetailView):
    model = get_user_model()
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileEditPage(generic.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'
    # success_url = reverse_lazy('profile-details')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    # def get_queryset(self):
    #     queryset = self.get_queryset()
    #     print(queryset)
    #     return queryset

    # def get_object(self, queryset=None):
    #     return self.request.user


class ProfileDeletePage(generic.DeleteView):
    pass
