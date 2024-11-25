from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.courses.forms import CourseForm
from UniversityApp.courses.models import Course


class CoursesCategoriesPage(generic.TemplateView):
    template_name = 'courses/courses_categories.html'


class CoursesPage(generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    slug_url_kwarg = 'category'
    context_object_name = 'courses'

    def get_queryset(self):
        # get 'course category' dynamically (from url)
        category_url = self.request.get_full_path().split('/')[3].replace("-", " ")
        queryset = super().get_queryset().filter(category=category_url)
        return queryset


class CourseCreatePage(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course-create-page.html'
    success_url = reverse_lazy('courses-wd')


class CourseEditPage(generic.UpdateView):
    model = Course
    form_class = CourseForm
    pk_url_kwarg = 'pk'
    template_name = 'courses/course-edit-page.html'
    success_url = reverse_lazy('courses-wd')


class CourseDetailsPage(generic.DetailView):
    model = Course
    pk_url_kwarg = 'pk'
    template_name = 'courses/course-details-page.html'
