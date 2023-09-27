from books.usecases import *
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books_ids = []
        if wish_list := Session(self.request).get(WISH_LIST, []):
            books_ids = wish_list.get("book_ids", [])

        context.update({
            "books_ids": books_ids
        })
        # Do something
        return context
