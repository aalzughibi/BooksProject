from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class contact(models.Model):
    name = models.CharField(max_length = 400)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name + '( '+self.email+' )'


class Book(models.Model):
    name = models.CharField(max_length =500)
    isbn = models.CharField(max_length = 20)
    author = models.CharField(max_length = 400)
    publish_on =models.DateTimeField(default=timezone.now)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='book_pic')
    about = models.TextField()

    def __str__(self):
        return self.name


class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    mobile = models.CharField(max_length = 10)
    genders = (('M','Male'),('F','Female'))
    gender = models.CharField(max_length=1,choices = genders)

    def __str__(self):
        return self.user.username