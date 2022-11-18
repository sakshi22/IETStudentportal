from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Query(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    upvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.title)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.body[:50])