from django.urls import path, include
from UniversityApp.lessons.views import lesson_add_view

urlpatterns = [
    path('courses/categories/<slug:category_slug>/', include([
        path('<int:course_pk>/details/', include([
            path('lesson-add/', lesson_add_view, name='lesson-add'),
        ])),
    ])),
]
