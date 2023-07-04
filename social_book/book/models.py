from django.db import models

class UploadedBook(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploaded-files/')
    description = models.TextField()
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    year_published = models.PositiveIntegerField()

def __str__(self):
    return self.title
