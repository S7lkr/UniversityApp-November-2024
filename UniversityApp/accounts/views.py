from django.contrib.auth import get_user_model, login
from UniversityApp.accounts.forms import UserRegisterForm, ProfileEditForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from UniversityApp.accounts.models import Profile

User = get_user_model()


class UserRegisterPage(generic.CreateView):     # register
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('profile-edit', kwargs={'pk': self.object.pk})


class UserLoginPage(LoginView):                 # login
    template_name = 'users/login.html'


class ProfileDetailsPage(generic.DetailView):       # profile details
    model = get_user_model()
    template_name = 'profile/profile-details.html'


class ProfileEditPage(generic.UpdateView):          # profile edit
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeletePage(generic.DeleteView):        # profile delete
    pass
