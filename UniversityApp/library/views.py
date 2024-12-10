from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from UniversityApp.library.forms import BookAddForm, BookDeleteForm, MagazineAddForm, MagazineDeleteForm
from UniversityApp.library.models import Book, Magazine


class LibraryCategories(generic.TemplateView):
    template_name = 'library/literature-categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_cnt'] = Book.objects.count()
        context['magazines_cnt'] = Magazine.objects.count()
        return context


# ---------- Book views ----------

class BooksPage(generic.ListView):
    model = Book
    template_name = 'library/books/books.html'


class BookAddPage(generic.CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'library/books/book-add.html'
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.author = self.request.user
        book.author_name = self.request.user.profile.get_full_name()
        book.save()
        return super().form_valid(form)


class BookDetailsPage(LoginRequiredMixin, generic.DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'library/books/book-details.html'
    login_url = reverse_lazy('login')


class BookEditPage(generic.UpdateView):
    model = Book
    form_class = BookAddForm
    pk_url_kwarg = 'book_id'
    template_name = 'library/books/book-edit.html'

    def get_success_url(self):
        return reverse_lazy('book-details', kwargs={'book_id': self.object.pk})


class BookDeletePage(generic.DeleteView):
    model = Book
    form_class = BookDeleteForm
    pk_url_kwarg = 'book_id'
    template_name = 'library/books/book-delete.html'
    success_url = reverse_lazy('books')


# ----------- Magazine views -------------

class MagazinesPage(generic.ListView):
    model = Magazine
    template_name = 'library/magazines/magazines.html'


class MagazineAddPage(generic.CreateView):
    model = Magazine
    form_class = MagazineAddForm
    template_name = 'library/magazines/magazine-add.html'
    success_url = reverse_lazy('magazines')


class MagazineDetailsPage(LoginRequiredMixin, generic.DetailView):
    model = Magazine
    template_name = 'library/magazines/magazine-details.html'
    pk_url_kwarg = 'magazine_id'
    login_url = reverse_lazy('login')


class MagazineEditPage(generic.UpdateView):
    model = Magazine
    form_class = MagazineAddForm
    pk_url_kwarg = 'magazine_id'
    template_name = 'library/magazines/magazine-edit.html'

    def get_success_url(self):
        return reverse_lazy('magazine-details', kwargs={'magazine_id': self.object.pk})


class MagazineDeletePage(generic.DeleteView):
    model = Magazine
    form_class = MagazineDeleteForm
    pk_url_kwarg = 'magazine_id'
    template_name = 'library/magazines/magazine-delete.html'
    success_url = reverse_lazy('magazines')
