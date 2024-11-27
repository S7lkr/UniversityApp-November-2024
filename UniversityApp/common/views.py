from django.shortcuts import render, redirect
from django.views import generic
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

    return redirect(to='http://localhost:8000/courses/all-courses/')


def course_user_remove(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    profile = request.user.profile
    profile.course_id = None
    if profile.is_lector:
        course.lector = None
    course.save()
    profile.save()

    return redirect(to='http://localhost:8000/courses/all-courses/')

