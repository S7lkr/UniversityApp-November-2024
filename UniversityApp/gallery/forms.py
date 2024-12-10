from django import forms
from UniversityApp.gallery.models import Album, Photo
from UniversityApp.mixins import DisabledFieldsMixin


# ------------- Album Forms ----------- #

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'cover')


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ()


# ------------- Photo Forms ----------- #

class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)


class PhotoAddForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    pass


class PhotoDeleteForm(PhotoBaseForm):

    class Meta(PhotoBaseForm.Meta):
        fields = ()
