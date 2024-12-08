from UniversityApp.comments.models import Comment
from UniversityApp.courses.models import Course
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from UniversityApp.comments.forms import CommentAddForm, CommentEditForm, CommentDeleteForm


@login_required
def comment_add_view(request, category_slug: str, course_pk: int):
    if request.POST:
        course = Course.objects.get(pk=course_pk)
        form = CommentAddForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.course = course
            comment.save()
    return redirect(request.META.get('HTTP_REFERER') + f"#{course_pk}")


class CommentEditView(generic.UpdateView):
    model = Comment
    form_class = CommentEditForm
    pk_url_kwarg = 'comment_pk'
    template_name = 'courses/course_details/comments/comment-edit.html'

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
                'course_pk': self.object.course.pk,
            }
        )


class CommentDeleteView(generic.DeleteView):
    model = Comment
    form_class = CommentDeleteForm
    pk_url_kwarg = 'comment_pk'
    template_name = 'courses/course_details/comments/comment-delete.html'

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
                'course_pk': self.object.course.pk,
            }
        )

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
