import re
from books.models import Books
from books.usecases import *
from books.usecases import get_saved_books
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from smtplib import SMTPException
from django.utils.translation import activate, get_language, gettext_lazy as _


from django.core.mail import send_mail
from django.conf import settings
from .forms import SendEmailForm
from .usecases import *


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


def wishlist_view(request):
    test = _("Hello world")
    context = {
        "books": get_saved_books(request),
        "test": test
    }
    return render(request, 'wishlist.html', context)


def translate(request, language:str):
    current_lang = get_language()
    try:
        activate(language)
        messages.success(request, _("Language changed successfully"))
    except:
        activate(current_lang)
        messages.error(request, _("Invalid language"))

    return redirect('profile')


@permission_required('books.can_change_book', raise_exception=True)
def delete_from_wl(request, book_id: int):
    book = Books.objects.filter(id=book_id).first()
    delete_book_from_wl(request, book_id)

    messages.success(
        request, f"Successfully deleted {book.title} from wishlist")
    return redirect('wishlist_view')




@login_required
def send_email_view(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            email   = form.cleaned_data['email']
            title   = form.cleaned_data['title']
            message = form.cleaned_data['message']
            try:
                send_mail(title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
                messages.success(request, "Email sent successfully")
                return redirect('home_page')
            except SMTPException as error:
                messages.error(request, f"Error while sending email: {error}")
                return redirect('send_email_view')
        else:
            messages.error(request, f"Invalid form: {form.errors}")
            context = { 'form': form }
            return render(request, 'email_template.html', context)

    form = SendEmailForm()
    context = { 'form': form }
    return render(request, 'email_template.html', context)