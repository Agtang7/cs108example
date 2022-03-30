##### quotes/models.py #####

from django.urls import reverse

class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    # ... other methods here 

    def get_absolute_url(self):
        '''Return a URL to display this quote object.'''
        return reverse("quote", kwargs={"pk": self.pk})