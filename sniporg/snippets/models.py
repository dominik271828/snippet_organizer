from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lang(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"Lang: {self.name}"

class Snippet(models.Model):
    # TODO: maybe getenv?
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=1000)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
