from django.db import models

# Create your models here.
from django.db import models

class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)