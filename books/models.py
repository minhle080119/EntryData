from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30)
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})