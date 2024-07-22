from django.db import models

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title