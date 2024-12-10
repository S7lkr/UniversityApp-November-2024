from django.urls import path, include
from UniversityApp.gallery import views

urlpatterns = [
    path('albums/', include([
        path('', views.AlbumsShowPage.as_view(), name='albums'),
        path('add/', views.AlbumAddPage.as_view(), name='album-add'),
        path('<int:album_id>/', include([
            path('photos/', include([
                path('', views.PhotosShowPage.as_view(), name='photos'),
                path('photo-add/', views.PhotoAddPage.as_view(), name='photo-add'),
                path('<int:photo_id>/', include([
                    path('photo-delete/', views.PhotoDeletePage.as_view(), name='photo-delete'),
                ])),
            ])),
            path('album-edit/', views.AlbumEditPage.as_view(), name='album-edit'),
            path('album-delete/', views.AlbumDeletePage.as_view(), name='album-delete'),
        ])),
    ])),
]
