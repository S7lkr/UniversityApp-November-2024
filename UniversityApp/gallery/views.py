# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.gallery.models import Album, Photo
from UniversityApp.gallery.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, PhotoAddForm, \
    PhotoDeleteForm


# ------------- Album Views ----------- #

class AlbumsShowPage(generic.ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'about/gallery/albums/albums.html'
    # paginate_by = 3


class AlbumAddPage(generic.CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'about/gallery/albums/album-create.html'
    success_url = reverse_lazy('albums')


class AlbumEditPage(generic.UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'album_id'
    template_name = 'about/gallery/albums/album-edit.html'
    success_url = reverse_lazy('albums')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


class AlbumDeletePage(generic.DeleteView):
    model = Album
    pk_url_kwarg = 'album_id'
    form_class = AlbumDeleteForm
    template_name = 'about/gallery/albums/album-delete.html'
    success_url = reverse_lazy('albums')


# ------------- Photo Views ----------- #

class PhotosShowPage(generic.DetailView):
    model = Album
    pk_url_kwarg = 'album_id'
    template_name = 'about/gallery/photos/photos.html'


class PhotoAddPage(generic.CreateView):
    model = Photo
    form_class = PhotoAddForm
    pk_url_kwarg = 'album_id'
    template_name = 'about/gallery/photos/photo-add.html'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.album_id = self.kwargs['album_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('photos', kwargs={'album_id': self.object.album_id})


class PhotoDeletePage(generic.DeleteView):
    model = Photo
    form_class = PhotoDeleteForm
    template_name = 'about/gallery/photos/photo-delete.html'
    pk_url_kwarg = 'photo_id'

    def get_success_url(self):
        return reverse_lazy('photos', kwargs={'album_id': self.object.album.pk})
