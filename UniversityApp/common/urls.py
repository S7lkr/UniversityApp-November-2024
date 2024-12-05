from django.urls import path, include
from UniversityApp.common.views import HomePage, course_user_add, course_user_remove, lector_remove, comment_add_view, \
    AboutTeam, AboutPage, AboutStudents

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('courses/categories/<slug:category_slug>/', include([
        path('<int:course_pk>/details/', include([
            path('user-add/', course_user_add, name="user-add"),
            path('user-remove/', course_user_remove, name='user-remove'),
            path('lector-remove/', lector_remove, name='lector-remove'),
            path('add-comment/', comment_add_view, name='add-comment'),
        ])),
    ])),
    path('about/', include([
        path('', AboutPage.as_view(), name='about'),
        path('team/', AboutTeam.as_view(), name='about-team'),
        path('students/', AboutStudents.as_view(), name='about-students'),
    ]))
]
