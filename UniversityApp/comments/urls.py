from django.urls import path, include

from UniversityApp.comments.views import comment_add_view, CommentEditView, CommentDeleteView

urlpatterns = [
    path('courses/categories/<slug:category_slug>/', include([
        path('<int:course_pk>/details/', include([
            path('comment-add/', comment_add_view, name='add-comment'),
            path('<int:comment_pk>/', include([
                path('comment-edit/', CommentEditView.as_view(), name='edit-comment'),
                path('comment-delete/', CommentDeleteView.as_view(), name='delete-comment'),
            ])),
        ])),
    ])),
]
