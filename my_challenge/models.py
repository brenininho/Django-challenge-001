from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return "%s" % self.name


class Article(models.Model):
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, blank=True)
    firstParagraph = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=100, blank=True)
    category = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.author, self.title)


class Category(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return "%s" % self.name

