from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.courses import forms
from UniversityApp.courses.models import Course
from UniversityApp.comments.forms import CommentAddForm
from UniversityApp.lessons.forms import LessonAddForm


class CoursesCategoriesPage(generic.TemplateView):
    template_name = 'courses/courses_categories.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_design_count'] = Course.objects.filter(slug='web-design').count()
        context['graphic_design_count'] = Course.objects.filter(slug='graphic-design').count()
        context['video_editing_count'] = Course.objects.filter(slug='video-editing').count()
        context['online_marketing_count'] = Course.objects.filter(slug='online-marketing').count()

        return context


class CoursesAllPage(generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    login_url = reverse_lazy('login')

    # Authentication control:
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['courses/courses.html',]
        return ['courses/courses-not-auth.html']


class CoursesFromCategoryPage(generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'courses'

    def get_queryset(self):
        # get 'course.category' dynamically from slug ".../web-design/.." in the url
        category_lower = self.request.get_full_path().split('/')[3].replace("-", " ")
        category = (" ".join((word.capitalize() for word in category_lower.split(" "))))
        queryset = super().get_queryset().filter(category=category)
        return queryset

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['courses/courses.html',]
        return ['courses/courses-not-auth.html']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['courses']:
            context['category'] = self.object_list.first().category
        return context


class CourseCreatePage(LoginRequiredMixin, generic.CreateView):
    model = Course
    form_class = forms.CourseCreateForm
    slug_url_kwarg = 'category_slug'
    template_name = 'courses/course_management/course-create-page.html'
    success_url = reverse_lazy('courses-all')
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if 'courses.add_course' not in self.request.user.get_group_permissions():
            return render(request, 'errors/403.html', status=403)
        return super().dispatch(request, *args, **kwargs)


class CourseDetailsPage(generic.DetailView):
    model = Course
    pk_url_kwarg = 'course_pk'
    slug_url_kwarg = 'category_slug'
    template_name = 'courses/course_details/course-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        studs_cnt = self.object.profiles.count()

        context['lector'] = course.lector if course.lector else 'N/A'
        context['students_count'] = studs_cnt if not course.lector else studs_cnt - 1
        context['add_lesson_form'] = LessonAddForm
        context['lessons'] = course.lessons.all()
        context['comment_form'] = CommentAddForm
        context['comments'] = self.object.comments.all()

        return context


class CourseEditPage(generic.UpdateView):
    model = Course
    pk_url_kwarg = 'course_pk'
    slug_url_kwarg = 'category_slug'
    form_class = forms.CourseEditForm
    template_name = 'courses/course_management/course-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'course-details',
            kwargs={'category_slug': self.object.slug, 'course_pk': self.object.pk}
        )

    def form_valid(self, form):
        self.object.slug = slugify(self.object.category)
        return super().form_valid(form)


class CourseDeletePage(generic.DeleteView):
    model = Course
    slug_url_kwarg = 'category_slug'
    form_class = forms.CourseDeleteForm
    template_name = 'courses/course_management/course-delete-page.html'
    success_url = reverse_lazy('courses-all')

    def get_initial(self) -> dict:
        return self.get_object().__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
