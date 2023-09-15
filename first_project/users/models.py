from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.first_name + self.last_name

