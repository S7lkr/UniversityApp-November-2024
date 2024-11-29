from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from UniversityApp.accounts.models import Profile
from UniversityApp.common.forms import AddCommentForm
from UniversityApp.courses.models import Course
from django.views import generic
from django.shortcuts import redirect


class HomePage(generic.TemplateView):
    template_name = 'index.html'


def course_user_add(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    profile = request.user.profile
    profile.course_id = course.pk
    if profile.is_lector:
        course.lector = profile.get_full_name()
    course.save()
    profile.save()
    return redirect(to=request.META.get('HTTP_REFERER'))
    # return redirect(to='http://localhost:8000/courses/all/')


def course_user_remove(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    profile = request.user.profile
    profile.course_id = None
    if profile.is_lector:
        course.lector = None
    course.save()
    profile.save()
    return redirect(to=request.META.get('HTTP_REFERER'))
    # return redirect(to='http://localhost:8000/courses/all/')


def lector_remove(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    l_first_name = course.lector.split(" ")[0]
    l_last_name = course.lector.split(" ")[1]
    profile = Profile.objects.get(first_name=l_first_name, last_name=l_last_name)
    profile.course_id = None
    course.lector = None
    course.save()
    profile.save()

    return redirect(to=request.META.get('HTTP_REFERER'))       # stays on the same path
    # return redirect(to='http://localhost:8000/courses/all/')


@login_required
def comment_add_view(request, course_slug: str):
    if request.POST:
        course = Course.objects.get(slug=course_slug)
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.course = course
            comment.save()
    return redirect(request.META.get('HTTP_REFERER') + f"#{course_slug}")
