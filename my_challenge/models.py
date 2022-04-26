from django.db import models
from uuid import uuid4


def upload_image(instance, filename):
    return f"{instance.id}-{filename}"


class Author(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(blank=True, upload_to=upload_image)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)

    def __str__(self):
        return "%s" % self.name


class Article(models.Model):
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    first_paragraph = models.TextField(blank=True)
    body = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)

    def __str__(self):
        return "%s, %s" % (self.author, self.title)
