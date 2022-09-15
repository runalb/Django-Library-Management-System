from django.db import models

# Create your models here.

class LibraryModel(models.Model):
    book_name  = models.CharField(max_length=50)
    author_name  = models.CharField(max_length=50)

    def __str__(self):
        return f"ID: {self.id}, Book Name: {self.book_name}, Author Name: {self.author_name}"
