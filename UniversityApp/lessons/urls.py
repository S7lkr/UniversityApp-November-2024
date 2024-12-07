from django.urls import path, include
from UniversityApp.lessons.views import lesson_add_view, LessonEditView, LessonDeleteView

urlpatterns = [
    path('courses/categories/<slug:category_slug>/', include([
        path('<int:course_pk>/details/', include([
            path('', include([
                path('lesson-add/', lesson_add_view, name='lesson-add'),
                path('<int:lesson_pk>/', include([
                    path('lesson-edit/', LessonEditView.as_view(), name='lesson-edit'),
                    path('delete/', LessonDeleteView.as_view(), name='lesson-delete'),
                ])),
            ])),
        ])),
    ])),
]
