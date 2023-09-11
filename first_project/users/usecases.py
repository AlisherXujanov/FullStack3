from .forms import UserForm
from .models import User


def get_users_context():
    context = {
        'form': UserForm(),
        "users": User.objects.all()
    }
    return context
