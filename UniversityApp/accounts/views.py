from django.contrib.auth import get_user_model, login
from UniversityApp.accounts.forms import UserRegisterForm, ProfileCreateOrEditForm
from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from UniversityApp.accounts.models import Profile
from UniversityApp.courses.models import Course

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
    model = User
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_name = self.request.user.profile.last_name
        image = self.request.user.profile.personal_image
        bio = self.request.user.profile.bio
        age = self.request.user.profile.age
        course_id = self.request.user.profile.course_id

        context['user_type'] = "Lector" if self.request.user.profile.is_lector else "Student"
        context['last_name'] = last_name if last_name else ''
        context['image'] = image if image else ''
        context['bio'] = bio if bio else 'n/a'
        context['age'] = age if age else 'n/a'
        context['course'] = Course.objects.get(pk=course_id) if course_id else 'No'

        return context


class ProfileCreateOrEditPage(generic.UpdateView):          # profile edit
    model = Profile
    form_class = ProfileCreateOrEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeletePage(generic.DeleteView):        # profile delete
    pass
