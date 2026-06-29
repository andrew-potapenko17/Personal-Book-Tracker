from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    STATUSES = {
        'want_to_read': 'Want to read',
        'reading': 'Reading',
        'finished': 'Finished',
    }

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(choices=STATUSES)
    rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)