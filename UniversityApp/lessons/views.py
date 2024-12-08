from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.courses.models import Course
from UniversityApp.lessons.forms import LessonAddForm, LessonDeleteForm
from UniversityApp.lessons.models import Lesson


def lesson_add_view(request, category_slug: str, course_pk: int):
    if request.POST:
        course = Course.objects.get(pk=course_pk)
        form = LessonAddForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.readme = str(lesson.readme.split(';'))
            lesson.save()
        return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")
    return render(request, template_name=None, context={'form': LessonAddForm()})


# def lesson_edit_view(request, category_slug: str, course_pk: int, lesson_pk: int):
#     if request.POST:
#         pass

class LessonEditView(generic.UpdateView):
    model = Lesson
    form_class = LessonAddForm
    pk_url_kwarg = 'lesson_pk'
    template_name = 'courses/course_details/lessons/lesson-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_slug'] = self.object.course.slug
        context['course_pk'] = self.object.course.pk
        return context

    def get_success_url(self):
        return reverse_lazy(
            'course-details',
            kwargs={
                'category_slug': self.object.course.slug,
                'course_pk': self.object.course_id,
            }
        )


class LessonDeleteView(generic.DeleteView):
    model = Lesson
    form_class = LessonDeleteForm
    pk_url_kwarg = 'lesson_pk'
    template_name = 'courses/course_details/lessons/lesson-delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_slug'] = self.object.course.slug
        context['course_pk'] = self.object.course.pk
        context['lesson_name'] = self.object.title

        return context

    def get_success_url(self):
        return reverse_lazy(
            'course-details',
            kwargs={
                'category_slug': self.object.course.slug,
                'course_pk': self.object.course_id,
            }
        )
