"""
URL configuration for UniversityApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from UniversityApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('UniversityApp.accounts.urls')),
    path('', include('UniversityApp.common.urls')),
    path('courses/', include('UniversityApp.courses.urls')),
    path('', include('UniversityApp.lessons.urls')),
    path('', include('UniversityApp.comments.urls')),
    path('library/', include('UniversityApp.library.urls')),
    path('gallery/', include('UniversityApp.gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
