from django.shortcuts import redirect, render
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
    return render(request, template_name=None, context={'form': LessonAddForm()})
