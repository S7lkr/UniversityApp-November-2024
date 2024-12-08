from django.views import generic
from UniversityApp.accounts.models import Profile
from UniversityApp.courses.models import Course
from django.shortcuts import redirect


class HomePage(generic.TemplateView):
    template_name = 'index.html'


def course_user_add(request, category_slug: str, course_pk: int):
    course = Course.objects.get(pk=course_pk)
    profile = request.user.profile
    profile.course_id = course.pk
    if profile.is_lector:
        course.lector = profile.get_full_name()
    course.save()
    profile.save()
    return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")


def course_user_remove(request, category_slug: str, course_pk: int):
    course = Course.objects.get(pk=course_pk)
    profile = request.user.profile
    profile.course_id = None
    if profile.is_lector:
        course.lector = None
    course.save()
    profile.save()
    return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")


def lector_remove(request, category_slug: str, course_pk: int):
    course = Course.objects.get(pk=course_pk)
    l_first_name = course.lector.split(" ")[0]
    l_last_name = course.lector.split(" ")[1]
    profile = Profile.objects.get(first_name=l_first_name, last_name=l_last_name)
    profile.course_id = None
    course.lector = None
    course.save()
    profile.save()
    return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")


class AboutPage(generic.TemplateView):
    template_name = 'about/about.html'


class AboutTeam(generic.ListView):
    model = Profile
    template_name = 'about/lectors.html'
    context_object_name = 'lectors'

    def get_queryset(self):
        lectors = Profile.objects.filter(is_lector=True)
        return lectors


class AboutStudents(generic.ListView):
    model = Profile
    template_name = 'about/students.html'
    context_object_name = 'students'

    def get_queryset(self):
        students = Profile.objects.filter(is_lector=False)
        return students
