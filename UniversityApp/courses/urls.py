from django.urls import path, include
from UniversityApp.courses import views

urlpatterns = [
    path('categories/', include([
        path('', views.CoursesCategoriesPage.as_view(), name='categories'),
        path('Web-Design/', include([
            path('', views.CoursesPage.as_view(), name='courses-wd'),
            path('create/', views.CourseCreatePage.as_view(), name='courses-wd-create'),
            path('<int:pk>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-wd-edit'),
            ]))
        ])),
        path('Graphic-Design/', views.CoursesPage.as_view(), name='courses-gd'),
        path('Video-Editing/', views.CoursesPage.as_view(), name='courses-ve'),
        path('Online-Marketing/', views.CoursesPage.as_view(), name='courses-om'),
    ])),
]
