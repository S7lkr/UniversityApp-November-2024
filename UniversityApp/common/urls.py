from django.urls import path
from UniversityApp.common.views import HomePage, add_user_to_course

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add-user-to-course/<slug:course_slug>/', add_user_to_course, name="add-user-to-course"),
]
