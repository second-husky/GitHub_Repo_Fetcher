from django.db import models

# Create your models here.
class GitHubRepo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    repository = models.TextField()

    def __str__(self):
        return self.username[:50]
