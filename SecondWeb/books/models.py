from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    summary = RichTextUploadingField()
    publication_date = models.DateField()

    @property
    def __str__(self):
        return self.title

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    summary = RichTextUploadingField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()
    summary = RichTextUploadingField()

    def __str__(self):
        return self.name