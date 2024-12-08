from django import forms
from UniversityApp.library.models import Book
from UniversityApp.mixins import PlaceholderMixin


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('author',)
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BookAddForm(PlaceholderMixin, BookBaseForm):
    pass


class BookDeleteForm(BookBaseForm):
    class Meta(BookBaseForm.Meta):
        fields = ()
