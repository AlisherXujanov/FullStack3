from math import exp
import os
from datetime import datetime
from smtplib import SMTPException

from django.contrib.auth.models import User
from django.db import IntegrityError, models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

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


class Genre(models.Model):
    slug = models.SlugField(unique=True)  # this is for url
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Books(models.Model):
    title: str = models.CharField(max_length=50)
    description: str = models.TextField()
    author: User = models.ForeignKey(User,
                                     on_delete=models.SET_NULL, null=True, blank=True)
    genre: Genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True)
    is_available: bool = models.BooleanField(default=True)
    price: float = models.DecimalField(max_digits=5, decimal_places=2)
    created: datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        default='books/book_default_img.png', upload_to="books")

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

        # We have to save the form first before getting the image path
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def delete(self, *args, **kwargs):
        image_url = self.image.url
        if image_url != '/media/books/book_default_img.png':
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['is_available', 'price']),
        ]
        permissions = [('can_change_book', 'Can change book')]


@receiver(post_save, sender=Books)
def print_info_of_book(sender, instance, created, **kwargs):
    if created:
        print("--------------------------------------------------")
        print(f'Book instance named: {instance.title} was created')
        print("--------------------------------------------------")

        try:
            send_mail(
                f'Book instance named: {instance.title} was created',
                'In your project Alisher Company Fullstack Developer new book was created',
                settings.EMAIL_HOST_USER,
                ['alisherxujanov163@gmail.com'],
                fail_silently=False,
            )
        except SMTPException as error:
            print("--------------------------------------------")
            print("Error while sending email: ", error)
            print("--------------------------------------------")
