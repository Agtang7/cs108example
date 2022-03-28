from .models import Quote
from django.views.generic import ListView, DetailView

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Quote # retrieve objects of type Quote from the database
    template_name = 'quotes/home.html'
    context_object_name = 'quotes' # how to find the data in the template file

class QuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'