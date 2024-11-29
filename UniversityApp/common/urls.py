from django.urls import path
from UniversityApp.common.views import HomePage, course_user_add, course_user_remove, lector_remove, comment_add_view

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('user-add/<slug:course_slug>/', course_user_add, name="user-add"),
    path('user-remove/<slug:course_slug>', course_user_remove, name='user-remove'),
    path('lector-remove/<slug:course_slug>/', lector_remove, name='lector-remove'),
    path('add-comment/<slug:course_slug>/', comment_add_view, name='add-comment'),
]
