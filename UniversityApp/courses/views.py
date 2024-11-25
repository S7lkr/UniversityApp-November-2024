from django.views import generic
from UniversityApp.courses.models import Course


class CoursesCategoriesPage(generic.TemplateView):
    template_name = 'courses_categories.html'


class CoursesPage(generic.ListView):
    model = Course
    template_name = 'courses.html'
    slug_url_kwarg = 'category'
    context_object_name = 'courses'

    def get_queryset(self):
        # get 'course category' dynamically (from url)
        category_url = self.request.get_full_path().split('/')[3].replace("-", " ")
        queryset = super().get_queryset().filter(category=category_url)
        return queryset
