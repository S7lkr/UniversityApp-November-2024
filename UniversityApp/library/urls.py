from django.urls import path, include
from UniversityApp.library import views

urlpatterns = [
    path('categories/', views.LibraryCategories.as_view(), name='lib-categories'),
    path('books/', include([
        path('', views.BooksPage.as_view(), name='books'),
        path('book-add/', views.BookAddPage.as_view(), name='book-add'),
        path('<int:book_id>/', include([
            path('book-details/', views.BookDetailsPage.as_view(), name='book-details'),
            path('book-edit/', views.BookEditPage.as_view(), name='book-edit'),
            path('book-delete/', views.BookDeletePage.as_view(), name='book-delete'),
        ])),
    ])),
    path('journals/', include([
        path('', views.SoftwareJournalsPage.as_view(), name='journals'),
    ])),
]
