from django.urls import path
from UniversityApp.common.views import HomePage, course_user_add, course_user_remove

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('user-add/<slug:course_slug>/', course_user_add, name="user-add"),
    path('user-remove/', course_user_remove, name='user-remove'),
]
