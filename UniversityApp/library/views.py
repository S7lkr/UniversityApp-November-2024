from django.urls import reverse_lazy
from django.views import generic

from UniversityApp.library.forms import BookAddForm, BookDeleteForm
from UniversityApp.library.models import Book, SoftwareJournal


class LibraryCategories(generic.TemplateView):
    template_name = 'about/library/literature-categories.html'


# ---------- Book views ----------

class BooksPage(generic.ListView):
    model = Book
    template_name = 'about/library/books.html'


class BookAddPage(generic.CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'about/library/books/book-add.html'
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.author = self.request.user
        book.save()
        return super().form_valid(form)


class BookDetailsPage(generic.DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'about/library/books/book-details.html'


class BookEditPage(generic.UpdateView):
    model = Book
    form_class = BookAddForm
    pk_url_kwarg = 'book_id'
    template_name = 'about/library/books/book-edit.html'

    def get_success_url(self):
        return reverse_lazy('book-details', kwargs={'book_id': self.object.pk})


class BookDeletePage(generic.DeleteView):
    model = Book
    form_class = BookDeleteForm
    pk_url_kwarg = 'book_id'
    template_name = 'about/library/books/book-delete.html'

    def get_success_url(self):
        return reverse_lazy('book-details', kwargs={'book_id': self.object.pk})


# ----------- SoftwareJournal views -------------

class SoftwareJournalsPage(generic.ListView):
    model = SoftwareJournal
    template_name = 'about/library/journals.html'
