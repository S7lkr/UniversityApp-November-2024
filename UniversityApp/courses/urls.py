from django.urls import path, include
from UniversityApp.courses import views

urlpatterns = [
    path('all/', views.CoursesAllPage.as_view(), name='courses-all'),
    path('create/', views.CourseCreatePage.as_view(), name='course-create'),
    path('categories/', include([
        path('', views.CoursesCategoriesPage.as_view(), name='categories'),
        path('Web-Design/', include([
            path('', views.CoursesFromCategoryPage.as_view(), name='courses-wd'),
            path('<slug:course_slug>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='course-details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-edit'),
                path('delete/', views.CourseDeletePage.as_view(), name='course-delete'),
            ])),
        ])),
        path('Graphic-Design/', include([
            path('', views.CoursesFromCategoryPage.as_view(), name='courses-gd'),
            path('<slug:course_slug>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='course-details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-edit'),
                path('delete/', views.CourseDeletePage.as_view(), name='course-delete'),
            ])),
        ])),
        path('Video-Editing/', include([
            path('', views.CoursesFromCategoryPage.as_view(), name='courses-ve'),
            path('<slug:course_slug>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='course-details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-edit'),
                path('delete/', views.CourseDeletePage.as_view(), name='course-delete'),
            ])),
        ])),
        path('Online-Marketing/', include([
            path('', views.CoursesFromCategoryPage.as_view(), name='courses-om'),
            path('<slug:course_slug>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='course-details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-edit'),
                path('delete/', views.CourseDeletePage.as_view(), name='course-delete'),
            ])),
        ])),
    ])),
]

