from django.views import generic

from UniversityApp.library.models import Book, Journal


class LibraryCategories(generic.TemplateView):
    template_name = 'about/library/literature-categories.html'


class LibraryBooksPage(generic.ListView):
    model = Book
    template_name = 'about/library/books.html'


class LibraryJournalsPage(generic.ListView):
    model = Journal
    template_name = 'about/library/journals.html'
