from django.db import models
from django.core.validators import MinValueValidator

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title.title()} : {self.description}'


