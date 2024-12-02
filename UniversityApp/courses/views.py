from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.courses import forms
from UniversityApp.courses.models import Course
from UniversityApp.common.forms import AddCommentForm


class CoursesCategoriesPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'courses/courses_categories.html'
    login_url = reverse_lazy('login')


class CoursesAllPage(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    login_url = reverse_lazy('login')


class CoursesFromCategoryPage(generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'courses'

    def get_queryset(self):
        # get 'course.category' dynamically from the slug (.../web-design/) in the url
        category_lower = self.request.get_full_path().split('/')[3].replace("-", " ")
        category = (" ".join((word.capitalize() for word in category_lower.split(" "))))
        queryset = super().get_queryset().filter(category=category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['courses']:
            context['category'] = self.object_list.first().category
        return context


class CourseCreatePage(LoginRequiredMixin, generic.CreateView):
    model = Course
    form_class = forms.CourseCreateForm
    slug_url_kwarg = 'category_slug'
    template_name = 'courses/course-create-page.html'
    success_url = reverse_lazy('courses-all')
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not (self.request.user.profile.is_lector or self.request.user.is_superuser):
            return render(request, 'errors/403.html', status=403)
        return super().dispatch(request, *args, **kwargs)


class CourseDetailsPage(generic.DetailView):
    model = Course
    slug_url_kwarg = 'category_slug'
    template_name = 'courses/course-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        profile = self.request.user.profile
        studs_cnt = self.object.profiles.count()
        context['lector'] = course.lector if course.lector else 'N/A'
        context['students_count'] = studs_cnt - 1 if profile.is_lector and profile.course_id == course.pk else studs_cnt
        context['comment_form'] = AddCommentForm
        context['comments'] = self.object.comment_set.all()
        return context


class CourseEditPage(generic.UpdateView):
    model = Course
    slug_url_kwarg = 'category_slug'
    form_class = forms.CourseEditForm
    template_name = 'courses/course-edit-page.html'
    # success_url = reverse_lazy('courses-all')

    def get_success_url(self):
        return reverse_lazy('course-details', kwargs={'pk': self.object.pk, 'category_slug': self.object.slug})


class CourseDeletePage(generic.DeleteView):
    model = Course
    slug_url_kwarg = 'category_slug'
    form_class = forms.CourseDeleteForm
    template_name = 'courses/course-delete-page.html'
    success_url = reverse_lazy('courses-all')

    def get_initial(self) -> dict:
        return self.get_object().__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
