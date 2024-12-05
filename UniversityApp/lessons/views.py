from django.shortcuts import redirect
from django.urls import reverse_lazy

# from django.views.generic import CreateView
from UniversityApp.courses.models import Course
from UniversityApp.lessons.forms import LessonAddForm
# from UniversityApp.lessons.models import Lesson


def lesson_add_view(request, category_slug: str, course_pk: int):
    if request.POST:
        course = Course.objects.get(pk=course_pk)
        form = LessonAddForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.readme = str(lesson.readme.replace(', ', ',').split(","))
            lesson.save()
        return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")


# class LessonAddView(CreateView):
#     model = Lesson
#     form_class = LessonAddForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['add_lesson_form'] = None
