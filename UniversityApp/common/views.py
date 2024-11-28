from django.shortcuts import render, redirect
from django.views import generic

from UniversityApp.accounts.models import Profile
from UniversityApp.courses.models import Course


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
