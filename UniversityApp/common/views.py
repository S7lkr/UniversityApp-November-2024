from django.shortcuts import render
from django.views import generic
from UniversityApp.courses.models import Course


class HomePage(generic.TemplateView):
    template_name = 'index.html'


def add_user_to_course(request, course_slug):
    course_id = Course.objects.get(slug=course_slug).pk
    profile = request.user.profile
    profile.course_id = course_id
    print(request.user)
    print(course_slug)

    if course_slug:
        profile.save()

    context = {
        'slug_url_kwarg': course_slug,
    }

    return render(request, 'index.html', context)
