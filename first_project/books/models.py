from datetime import datetime

from django.db import IntegrityError, models
from users.models import User

# models.SET_NULL   =>   if the user is deleted,
#                        the book will still exist but the author
#                        will be set to null (null=None)
# -----------------------------------------------------
# models.CASCADE    =>   if the user is deleted,
#                        the book will be deleted as well
# -----------------------------------------------------
# models.PROTECT    =>   if the user is deleted,
#                        the book will not be deleted and
#                        an error will be raised
# -----------------------------------------------------
# ORM = Object Relational Mapper
# l = []
# Books.objects.filter(user__first_name__in=l).order_by("created")


class BooksManager(models.Manager):
    pass


class NullPriceException(Exception):
    pass


class Books(models.Model):
    title: str = models.CharField(max_length=50)
    description: str = models.TextField()
    author: User = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    genre: str = models.CharField(max_length=25)
    is_available: bool = models.BooleanField(default=True)
    price: float = models.DecimalField(max_digits=5, decimal_places=2)
    created: datetime = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # default
    c_objects = BooksManager()  # custom manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.genre == None or self.genre == "":
            raise IntegrityError("Genre cannot be null")
        if self.price == 0:
            raise NullPriceException

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
