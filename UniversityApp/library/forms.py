from django import forms
from UniversityApp.library.models import Book, Magazine
from UniversityApp.mixins import PlaceholderMixin


# ------------ Book Forms -------------- #

class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('author', 'author_name')
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BookAddForm(PlaceholderMixin, BookBaseForm):
    pass


class BookDeleteForm(BookBaseForm):
    class Meta(BookBaseForm.Meta):
        fields = ()


# ------------ Magazine Forms -------------- #

class MagazineBaseForm(forms.ModelForm):
    class Meta:
        model = Magazine
        exclude = ('author',)
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MagazineAddForm(PlaceholderMixin, MagazineBaseForm):
    pass


class MagazineDeleteForm(BookBaseForm):
    class Meta(BookBaseForm.Meta):
        fields = ()
