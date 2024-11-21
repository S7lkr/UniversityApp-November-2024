from django.views import generic


class HomePage(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        pass
