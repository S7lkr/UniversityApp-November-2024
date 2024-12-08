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
    path('magazines/', include([
        path('', views.MagazinesPage.as_view(), name='magazines'),
        path('magazine-add/', views.MagazineAddPage.as_view(), name='magazine-add'),
        path('<int:magazine_id>/', include([
            path('magazine-details/', views.MagazineDetailsPage.as_view(), name='magazine-details'),
            path('magazine-edit/', views.MagazineEditPage.as_view(), name='magazine-edit'),
            path('magazine-delete/', views.MagazineDeletePage.as_view(), name='magazine-delete'),
        ])),
    ])),
]
