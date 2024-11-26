from django.shortcuts import render, redirect
from django.views import generic
from UniversityApp.courses.models import Course


class HomePage(generic.TemplateView):
    template_name = 'index.html'


def course_user_add(request, course_slug):
    course_id = Course.objects.get(slug=course_slug).pk
    profile = request.user.profile
    profile.course_id = course_id
    profile.save()

    return redirect(to='http://localhost:8000/courses/all-courses/')


def course_user_remove(request):
    profile = request.user.profile
    profile.course_id = None
    profile.save()

    return redirect(to='http://localhost:8000/courses/all-courses/')

