from django.shortcuts import render

# Create your views here.
from .models import Quote, Person ## NOTE THE ADDITIONAL IMPORT

##########################################################################################
##New Detail view for one Person:
class PersonPageView(DetailView):
    '''Show all quotes and all images for one person.'''

    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'