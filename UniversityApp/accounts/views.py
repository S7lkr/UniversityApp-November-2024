from django.contrib.auth import get_user_model, login
from UniversityApp.accounts.forms import UserRegisterForm, ProfileCreateOrEditForm, ProfileDeleteForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from UniversityApp.accounts.models import Profile, CustomUser
from UniversityApp.courses.models import Course

UserModel = get_user_model()


class UserRegisterPage(generic.CreateView):     # register
    model = UserModel
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
    success_url = reverse_lazy('home')
    redirect_authenticated_user = reverse_lazy('home')


class ProfileDetailsPage(generic.DetailView):       # profile details
    model = UserModel
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object().profile
        image = profile.personal_image
        bio = profile.bio
        age = profile.age
        course_id = profile.course_id

        context['user_type'] = "Lector" if profile.is_lector else "Student"
        context['profile'] = profile
        context['full_name'] = profile.get_full_name
        context['image'] = image if image else ''
        context['bio'] = bio if bio else 'n/a'
        context['age'] = age if age else 'n/a'
        context['course'] = self.object.profile.course

        return context


class ProfileCreateOrEditPage(generic.UpdateView):          # profile edit
    model = Profile
    form_class = ProfileCreateOrEditForm
    template_name = 'profile/profile-manage.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_type'] = 'Create' if self.object.first_name == 'Unnamed' else 'Edit'

        return context


class ProfileDeletePage(generic.DeleteView):        # profile delete
    model = Profile
    form_class = ProfileDeleteForm
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('logout')

    def get_initial(self):
        return self.get_object().__dict__

    def form_valid(self, form):
        profile_pk = self.get_object().pk
        user = CustomUser.objects.get(pk=profile_pk)
        user.is_active = False
        user.save()
        return super().form_valid(form)
