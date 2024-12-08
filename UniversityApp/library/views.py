from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.library.forms import BookAddForm, BookDeleteForm
from UniversityApp.library.models import Book, Magazine


class LibraryCategories(generic.TemplateView):
    template_name = 'about/library/literature-categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_cnt'] = Book.objects.count()
        context['magazines_cnt'] = Magazine.objects.count()
        return context


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


# ----------- Magazine views -------------

class MagazinesPage(generic.ListView):
    model = Magazine
    template_name = 'about/library/journals.html'


class MagazineAddPage(generic.CreateView):
    model = Magazine
    form_class = None
    template_name = None
    success_url = None


class MagazineDetailsPage(generic.DetailView):
    model = Magazine
    template_name = None
    pk_url_kwarg = 'magazine_id'


class MagazineEditPage(generic.UpdateView):
    model = Magazine
    form_class = None
    pk_url_kwarg = 'magazine_id'
    template_name = None
    success_url = None


class MagazineDeletePage(generic.DeleteView):
    model = Magazine
    form_class = None
    pk_url_kwarg = 'magazine_id'
    template_name = None
    success_url = None
