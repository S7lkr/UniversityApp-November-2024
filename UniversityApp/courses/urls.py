from django.urls import path, include
from UniversityApp.courses import views

urlpatterns = [
    path('categories/', include([
        path('', views.CoursesCategoriesPage.as_view(), name='categories'),
        path('Web-Design/', views.CoursesPage.as_view(), name='courses-wd'),
        path('Graphic-Design/', views.CoursesPage.as_view(), name='courses-gd'),
        path('Video-Editing/', views.CoursesPage.as_view(), name='courses-ve'),
        path('Online-Marketing/', views.CoursesPage.as_view(), name='courses-om'),
    ])),
]
