from django.urls import path, include
from UniversityApp.library import views

urlpatterns = [
    path('categories/', views.LibraryCategories.as_view(), name='lib-categories'),
    path('books/', include([
        path('', views.LibraryBooksPage.as_view(), name='books'),
    ])),
    path('journals/', include([
        path('', views.LibraryJournalsPage.as_view(), name='journals'),
    ])),
]
