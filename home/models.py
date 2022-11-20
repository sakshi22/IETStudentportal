from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BRANCH = (
    ('all', 'ALL'),
    ('cs', 'CS'),
    ('it', 'IT'),
    ('tc', 'ETC'),
    ('ei', 'EI'),
    ('cv', 'CIVIL'),
    ('me', 'MECH'),
)

YEAR = (
    ('all', 'ALL'),
    ('1', 'I Year'),
    ('2', 'II Year'),
    ('3', 'III Year'),
    ('4', 'IV Year'),
)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=6, choices=BRANCH, default='all')
    year = models.CharField(max_length=6, choices=YEAR, default='all')
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, blank=True, upload_to='files/')

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.title)


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.body[:50])