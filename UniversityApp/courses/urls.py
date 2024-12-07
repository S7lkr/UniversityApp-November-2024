from django.urls import path, include
from UniversityApp.courses import views

urlpatterns = [
    path('all/', views.CoursesAllPage.as_view(), name='courses-all'),
    path('create/', views.CourseCreatePage.as_view(), name='course-create'),
    path('categories/', include([
        path('', views.CoursesCategoriesPage.as_view(), name='courses-categories'),
        path('<slug:category_slug>/', include([
            path('', views.CoursesFromCategoryPage.as_view(), name='courses-from-category'),
            path('<int:course_pk>/', include([
                path('details/', views.CourseDetailsPage.as_view(), name='course-details'),
                path('edit/', views.CourseEditPage.as_view(), name='course-edit'),
                path('delete/', views.CourseDeletePage.as_view(), name='course-delete'),
            ])),
        ])),
    ])),
]
