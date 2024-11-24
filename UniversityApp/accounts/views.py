from UniversityApp.accounts.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy


class UserRegisterPage(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')


class UserLoginPage(LoginView):
    template_name = 'registration/login.html'


class ProfileDetailsPage(generic.DetailView):
    pass


class ProfileEditPage(generic.UpdateView):
    pass


class ProfileDeletePage(generic.DeleteView):
    pass
