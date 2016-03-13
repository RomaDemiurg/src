from django.db import models


class Article(models.Model):
    """
    `Article` Model, that represents articles in a Blog.

    Properties:
        1. title
        2. content
        3. created
        4. updated

    Methods:
        1. __str__(self)
        2. title
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
