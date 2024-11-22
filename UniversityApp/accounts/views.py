from UniversityApp.accounts.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy


class UserRegisterPage(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('home')


class UserLoginPage(LoginView):
    template_name = 'users/login.html'


class UserEditPage(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')


class ProfileDetailsPage(generic.DetailView):
    pass


class ProfileDeletePage(generic.DeleteView):
    pass
