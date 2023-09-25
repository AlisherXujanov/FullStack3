from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

# @login_required
# def home(request):
#     return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Do something
        return context
